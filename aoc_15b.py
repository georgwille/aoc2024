import os
fieldraw, moves = open('input_15.txt').read()[:-1].split('\n\n')

fieldraw = fieldraw.split()
moves = ''.join(moves.split())

field = {}

def printfield():
    field[(rbot,cbot)]='@'
    for r in range(len(fieldraw)):
        for c in range(len(fieldraw[0]*2)):
            print(field[(r,c)],end='')
        print()
    field[(rbot,cbot)]='.'

for r,line in enumerate(fieldraw):
    for c,char in enumerate(line):
        if char =="@":
            rbot = r
            cbot = 2*c
            field[(r,2*c)]='.'
            field[(r,2*c+1)]='.'
            continue
        elif char == 'O':
            field[(r,2*c)]="["
            field[(r,2*c+1)]="]"
        else:
            field[(r,2*c)]=char
            field[(r,2*c+1)]=char

# printfield()

def whatmoves(r,c):
    '''what moves if I'm at (r,c) and push in direction (dr,dc)

    result: movement is possible (True/False)
            list of coordinates that will move if possible
    '''
    f = field[(r+dr,c+dc)]

    if f == '.':
        return True,[]
    if f == '#':
        return False,[]

    offset = 1 if f == '[' else -1
    sub_can_move, sub_crates = whatmoves(r+dr,c+dc+offset)
    sub2_can_move, sub2_crates = (True,[]) if dr==0 else whatmoves(r+dr,c+dc)

    return sub_can_move and sub2_can_move, [(r+dr,c+dc),(r+dr,c+dc+offset)]+sub_crates+sub2_crates


for m in moves:
    dr,dc = [(0,-1),(0,1),(-1,0),(1,0)]['<>^v'.index(m)]
    can_move,crates = whatmoves(rbot,cbot)
    crates = set(crates)
    if can_move:
        rbot += dr
        cbot += dc
        temp = {}
        for crate in crates:
            temp[crate]=field[crate]
            field[crate]='.'
        for crate in temp:
            field[(crate[0]+dr,crate[1]+dc)]=temp[crate]
    # os.system('cls')
    # printfield()


total = 0
for (r,c),char in field.items():
    if char == '[':
        total += 100*r+c

# printfield()

print(total)
