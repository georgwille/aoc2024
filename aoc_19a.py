from functools import cache

towels, patterns = open('input_19.txt').read().strip().split('\n\n')

towels = towels.split(',')
towels = [x.strip() for x in towels]
patterns = patterns.split()

@cache
def made_from(pattern):
    # print(pattern)
    if not pattern:
        return ''
    lp = len(pattern)
    for towel in towels:
        lt = len(towel)
        if lt > lp:
            continue
        if pattern[:lt] == towel:
            check = made_from(pattern[lt:])
            if check == 'X':
                continue
            else:
                return towel+' '+check
    return 'X'

total = 0

for pattern in patterns:
    # print(pattern)
    if made_from(pattern) != 'X':
        total += 1

print(total)
