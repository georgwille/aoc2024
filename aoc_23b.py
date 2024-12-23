from collections import defaultdict
myinput = open('input_23.txt').read().strip().split()

c1 = defaultdict(set)

for line in myinput:
    n1,n2 = line.split('-')
    c1[n1].add(n2)
    c1[n2].add(n1)

expanded = True

solutions = set(c1.keys())

while expanded:
    expanded = False
    new_sol = set()
    for sol in solutions:
        neighbors_to_all = set(c1.keys())
        for node in sol.split(','):
            neighbors_to_all = neighbors_to_all & c1[node]
        if not neighbors_to_all:
            continue
        expanded = True
        for neighbor in neighbors_to_all:
            new_sol.add(','.join(sorted(sol.split(',')+[neighbor])))
        solutions = new_sol

print(solutions)
