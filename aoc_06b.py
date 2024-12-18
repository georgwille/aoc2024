myinput = open('input_06.txt').read()[:-1].split('\n')

for r,line in enumerate(myinput):
    for c,char in enumerate(line):
        if char == '^':
            startrow = r
            startcol = c

turnright = {(-1,0):(0,1),
             (0,1):(1,0),
             (1,0):(0,-1),
             (0,-1):(-1,0)}

def has_loop(brow, bcol):
    
    row, col = startrow, startcol
    visited = set()
    direction = (-1,0)
    visited.add((startrow,startcol,direction))

    while True:
        newrow = row+direction[0]
        newcol = col+direction[1]
        if not (0<=newrow<len(myinput)) or not(0<=newcol<len(myinput[0])):
            return False
        if myinput[newrow][newcol] == '#' or (newrow, newcol) == (brow,bcol):
            direction = turnright[direction]
            continue
        else:
            row, col = newrow, newcol
            if (row, col, direction) in visited:
                return True
            visited.add((row,col,direction))

loopcount = 0

for row in range(len(myinput)):
    for col in range(len(myinput[0])):
        if myinput[row][col] == '#':
            continue
        if has_loop(row, col):
            loopcount += 1

print(loopcount)
