myinput = open('input_02.txt').read()[:-1].split('\n')

print(myinput)

safecount = 0

for line in myinput:
    line_is_safe = True
    numbers = [int(x) for x in line.split(' ')]
    print(numbers)
    # total = 0
    if numbers[1] > numbers[0]:
        slope = 1
    elif numbers[1] < numbers[0]:
        slope = -1
    else:
        slope = 0
        continue
    for idx in range(len(numbers)-1):
        if not(0 < (numbers[idx+1]-numbers[idx])//slope < 4):
            line_is_safe = False
            print("fail: ",idx)
            break
    if line_is_safe:
        safecount += 1

print(safecount)
