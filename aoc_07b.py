myinput = open('input_07.txt')

def number_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

validcount = 0

for line in myinput:
    target,numbers = line[:-1].split(':')
    target = int(target)
    numbers = [int(x) for x in numbers.strip().split(' ')]
    print(target, numbers)
    for op in range(3**(len(numbers)-1)):
        opseq = number_to_base(op,3)
        opseq = [0]*(len(numbers)-1-len(opseq))+opseq
        # print(opseq)
        total = numbers[0]
        for i,number in enumerate(numbers[1:]):
            if opseq[i] == 0:
                total = total + number
            elif opseq[i] == 1:
                total = total * number
            elif opseq[i] == 2:
                total = int(str(total)+str(number))
        if total == target:
            validcount += total
            break

print(validcount)

