myinput = open('input_11.txt').readline().strip()

stones = myinput.split()

stones = [int(stone) for stone in stones]

print(stones)

for i in range(25):
    newstones = []
    for stone in stones:
        if stone == 0:
            newstones.append(1)
        elif len(str(stone))%2 == 0:
            l = str(stone)[:len(str(stone))//2]
            r = str(stone)[len(str(stone))//2:]
            newstones.append(int(l))
            newstones.append(int(r))
        else:
            newstones.append(stone*2024)
    stones = newstones
    # print(stones)
    # input()

print(len(stones))
