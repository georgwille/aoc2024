infile = open('input_01.txt').read().split('\n')[:-1]

leftlist=[]
rightlist=[]

for line in infile:
    l,r = line.split('   ')
    leftlist.append(int(l))
    rightlist.append(int(r))

total = 0

for value in leftlist:
    total += rightlist.count(value)*value

print(total)
