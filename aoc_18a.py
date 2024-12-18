# recycled and adapted from 2021/15
import heapq

blocked = set()

with open('input_18.txt') as fin:
    for i,line in enumerate(fin):
        if i > 1023:
            break
        x,y = [int(_) for _ in line.strip().split(',')]
        blocked.add((x,y))

start = (0,0)
xmax = 70
ymax = 70

# here comes a cheap implementation of A*

openlist = {start:[0, None]} #   (x,y): [cost to here, parent]
closedlist = {} #                (x,y): [cost to here, parent]
olheap = []
heapq.heappush(olheap, [0,start])

while openlist:
    while True:
        current = heapq.heappop(olheap)[1]
        if current in openlist:
            break

    closedlist[current] = openlist.pop(current)

    if current == (xmax,ymax):
        print(closedlist[current][0])
        break

    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        xn = current[0]+dx
        yn = current[1]+dy
        if not (0<=xn<=xmax and 0<=yn<=ymax):
            continue
        if (xn,yn) in blocked:
            continue
        if (xn,yn) in closedlist:
            continue
        thiscost = closedlist[current][0]+1
        if (xn,yn) in openlist and thiscost >= openlist[(xn,yn)][0]:
            continue
        openlist[(xn,yn)] = [thiscost, current]
        heapq.heappush(olheap,[thiscost,(xn,yn)])
