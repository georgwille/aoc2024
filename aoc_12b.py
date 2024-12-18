myinput = open('input_12.txt').read()[:-1].split('\n')

R = len(myinput)
C = len(myinput[0])
border = '#'*len(myinput[0])
myinput = [border]+myinput+[border]
for i,item in enumerate(myinput):
    myinput[i]='#'+item+'#'

R += 2
C += 2 

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
        thisarea = 0
        minr, maxr, minc, maxc = 10**5,-1,10**5,-1
        while todo:
            rr,cc = todo.pop(0)
            minr = min(minr,rr)
            maxr = max(maxr,rr)
            minc = min(minc,cc)
            maxc = max(maxc,cc)
            thisarea += 1
            shadow[rr][cc] = regioncounter
            for drr, dcc in [(1,0),(-1,0),(0,-1),(0,1)]:
                if myinput[r][c] != myinput[rr+drr][cc+dcc]:
                    continue
                if shadow[rr+drr][cc+dcc]:
                    continue
                if (rr+drr, cc+dcc) not in todo:
                    todo.append((rr+drr,cc+dcc))

        regions[regioncounter] = (thisarea,minr,maxr,minc,maxc)

for region,(area,minr,maxr,minc,maxc) in regions.items():
    corners = 0
    for r in range(minr-1,maxr+1):
        for c in range(minc-1,maxc+1):
            check = 0 # here comes the clever bit
            for dr,dc,s in [(0,0,1),(0,1,-1),(1,1,1),(1,0,-1)]:
                check += s*(shadow[r+dr][c+dc]==region)
            corners += abs(check)
    totalcost += corners*area

print(totalcost)
