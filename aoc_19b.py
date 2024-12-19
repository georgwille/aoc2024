from functools import cache

towels, patterns = open('input_19.txt').read().strip().split('\n\n')

towels = towels.split(',')
towels = [x.strip() for x in towels]
patterns = patterns.split()

@cache
def count_of(pattern):
    # print(pattern)
    if not pattern:
        return 1
    ways = 0
    lp = len(pattern)
    for towel in towels:
        lt = len(towel)
        if lt > lp:
            continue
        if pattern[:lt] == towel:
            if count_of(pattern[lt:]) == 0:
                continue
            else:
                ways += count_of(pattern[lt:])
    return ways

total = 0

for pattern in patterns:
    count = count_of(pattern)
    # print(pattern, count)
    total += count

print(total)
