from collections import defaultdict
myinput = open('input_23.txt').read().strip().split()

c1 = defaultdict(set)
c2 = defaultdict(set)

for line in myinput:
    n1,n2 = line.split('-')
    c1[n1].add(n2)
    c1[n2].add(n1)

for n1,nodes in c1.items():
    for node in nodes:
        c2[n1] = c2[n1].union(c1[node])
        c2[n1].remove(n1)

triple = set()

for n1,nodes in c1.items():
    if not n1.startswith('t'):
        continue
    for n2 in nodes:
        for n3 in c1[n2]:
            if n3 in c1[n1]:
                result = ''.join(sorted([n1,n2,n3]))
                triple.add(result)

print(len(triple))
