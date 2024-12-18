fieldraw, moves = open('input_15.txt').read()[:-1].split('\n\n')

fieldraw = fieldraw.split()
moves = ''.join(moves.split())

field = {}

for r,line in enumerate(fieldraw):
    for c,char in enumerate(line):
        if char =="@":
            rbot = r
            cbot = c
            field[(r,c)]='.'
            continue
        field[(r,c)]=char

def behind_stack(r,c,dr,dc):
    offset = 0
    while True:
        offset += 1
        test = field[(r+offset*dr,c+offset*dc)]
        if test == 'O':
            continue
        else:
            break
    return r+offset*dr,c+offset*dc,test

for m in moves:
    dr,dc = [(0,-1),(0,1),(-1,0),(1,0)]['<>^v'.index(m)]
    newr, newc, stuff = behind_stack(rbot,cbot,dr,dc)
    if stuff == '.':
        rbot += dr
        cbot += dc
        field[(rbot,cbot)],field[(newr,newc)] = field[(newr,newc)],field[(rbot,cbot)]

total = 0
for (r,c),char in field.items():
    if char == 'O':
        total += 100*r+c

print(total)
