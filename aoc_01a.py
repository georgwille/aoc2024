infile = open('input_01.txt').read().split('\n')[:-1]

leftlist=[]
rightlist=[]

for line in infile:
    l,r = line.split('   ')
    leftlist.append(int(l))
    rightlist.append(int(r))

leftlist.sort()
rightlist.sort()

total = 0

for idx, lvalue in enumerate(leftlist):
    total += abs(lvalue-rightlist[idx])

print(total)
