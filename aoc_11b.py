import functools

myinput = open('input_11.txt').readline().strip()

stones = myinput.split()

stones = [int(stone) for stone in stones]

print(stones)

cache = {}

@functools.cache
def size(stone, gen):
    _sum = 0
    if gen == 0:
        return 1
    if stone == 0:
        _sum += size(1,gen-1)
    elif len(str(stone))%2 == 0:
        l = str(stone)[:len(str(stone))//2]
        r = str(stone)[len(str(stone))//2:]
        _sum += size(int(l),gen-1)
        _sum += size(int(r),gen-1)
    else:
        _sum += size(stone*2024,gen-1)
    return _sum

total = 0

for stone in stones:
    total += size(stone,75)

print(total)
