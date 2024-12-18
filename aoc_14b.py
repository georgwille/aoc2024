myinput = open('input_14.txt').read()[:-1].split('\n')

bots = []

for line in myinput:
    p,v = line.split(' ')
    x,y = p[2:].split(',')
    vx,vy = v[2:].split(',')
    bots.append([int(x),int(y),int(vx),int(vy)])

xs = 101
ys = 103

q = [[0,0],[0,0]]

for step in range(7887,7898):
    for yy in range(ys):
        for xx in range(xs):
            bothere = False
            for bot in bots:
                if ((bot[0] + step*bot[2]) % xs == xx and 
                   (bot[1] + step*bot[3]) % ys == yy):
                    bothere = True
                    break
            if bothere:
                print('#',end='')
            else:
                print('.',end='')
        print()
    input(step)
