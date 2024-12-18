from collections import defaultdict

myinput = open('input_08.txt').read()[:-1].split('\n')

nrows = len(myinput)
ncols = len(myinput[0])

antenna = defaultdict(list)

for r,line in enumerate(myinput):
    for c,char in enumerate(line):
        if char in '#.':
            continue
        antenna[char].append((r,c))

antinodes = set()

for ant,pos in antenna.items():
    for i,(ri,ci) in enumerate(pos):
        for j,(rj,cj) in enumerate(pos[i+1:],i+1):
            print(ri,ci,rj,cj)
            dr = rj-ri
            dc = cj-ci
            ra = ri-dr
            ca = ci-dc
            rb = rj+dr
            cb = cj+dc
            if 0<=ra<nrows and 0<=ca<ncols:
                antinodes.add((ra,ca))
            if 0<=rb<nrows and 0<=cb<ncols:
                antinodes.add((rb,cb))

print(len(antinodes))
