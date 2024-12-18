myinput = open('input_12.txt').read()[:-1].split('\n')

R = len(myinput)
C = len(myinput[0])
border = '#'*len(myinput[0])
myinput = [border]+myinput+[border]
for i,item in enumerate(myinput):
    myinput[i]='#'+item+'#'

R += 2
C += 2 

def fences(r,c):
    nf = 0
    for dr, dc in [(1,0),(-1,0),(0,-1),(0,1)]:
        if myinput[r][c] != myinput[r+dr][c+dc]:
            nf += 1
    return nf

regions = {}
line = [0]*C
shadow = [line.copy() for i in range(R)]

regioncounter = 0
totalcost = 0

for r in range(1,R-1):
    for c in range(1,C-1):
        if shadow[r][c]:
            continue
        regioncounter += 1
        todo = [(r,c)]
        thisfence = 0
        thisarea = 0
        while todo:
            rr,cc = todo.pop(0)
            thisfence += fences(rr,cc)
            thisarea += 1
            shadow[rr][cc] = regioncounter
            for drr, dcc in [(1,0),(-1,0),(0,-1),(0,1)]:
                if myinput[r][c] != myinput[rr+drr][cc+dcc]:
                    continue
                if shadow[rr+drr][cc+dcc]:
                    continue
                if (rr+drr, cc+dcc) not in todo:
                    todo.append((rr+drr,cc+dcc))

        regions[regioncounter] = (thisarea, thisfence)
        totalcost += thisarea*thisfence

print(totalcost)
