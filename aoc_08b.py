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
            dr = rj-ri
            dc = cj-ci
            for mul in range(-50,50):
                ra = ri+mul*dr
                ca = ci+mul*dc
                if 0<=ra<nrows and 0<=ca<ncols:
                    antinodes.add((ra,ca))

print(len(antinodes))
