myinput = open('input_02.txt').read()[:-1].split('\n')

def is_strictly_valid(numberlist):
    is_valid = True
    if numberlist[1] > numberlist[0]:
        slope = 1
    elif numberlist[1] < numberlist[0]:
        slope = -1
    else:
        slope = 0
        return False
    for idx in range(len(numberlist)-1):
        if not(0 < (numberlist[idx+1]-numberlist[idx])//slope < 4):
            is_valid = False
            # print("fail: ",idx)
            break
    return is_valid


safecount = 0

for rawline in myinput:
    numbers = [int(x) for x in rawline.split(' ')]
    modnumbers = [numbers]
    for idx, value in enumerate(numbers):
        modnumbers.append(numbers[:idx]+numbers[idx+1:])
    line_is_safe = False
    for line in modnumbers:
        if is_strictly_valid(line):
            safecount += 1
            break

print(safecount)
