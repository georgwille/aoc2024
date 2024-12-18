myinput = open('input_14.txt').read()[:-1].split('\n')

bots = []

for line in myinput:
    p,v = line.split(' ')
    x,y = p[2:].split(',')
    vx,vy = v[2:].split(',')
    bots.append([int(x),int(y),int(vx),int(vy)])

print(bots)

steps = 100
xs = 101
ys = 103

q = [[0,0],[0,0]]

for i,(x,y,vx,vy) in enumerate(bots):
    xn = (x + steps*vx) % xs
    yn = (y + steps*vy) % ys

    bots[i]=[xn,yn,vx,vy]

    if xn == xs//2 or yn == ys//2:
        continue

    qx = (2*xn) // xs
    qy = (2*yn) // ys

    q[qx][qy] += 1

print(bots)

print(q, q[0][0]*q[0][1]*q[1][0]*q[1][1])
