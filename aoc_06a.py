myinput = open('input_06.txt').read()[:-1].split('\n')

for r,line in enumerate(myinput):
    for c,char in enumerate(line):
        if char == '^':
            row = r
            col = c

turnright = {(-1,0):(0,1),
             (0,1):(1,0),
             (1,0):(0,-1),
             (0,-1):(-1,0)}

visited = set()
visited.add((row,col))
direction = (-1,0)

while True:
    newrow = row+direction[0]
    newcol = col+direction[1]
    if not (0<=newrow<len(myinput)) or not(0<=newcol<len(myinput[0])):
        break
    if myinput[newrow][newcol] == '#':
        direction = turnright[direction]
        continue
    else:
        row, col = newrow, newcol
        visited.add((row,col))

print(len(visited))
