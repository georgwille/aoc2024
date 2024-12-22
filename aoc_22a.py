myinput = open('input_22.txt').read().strip().split('\n')

def next_secret(n):
    t1 = n * 64
    t1 = t1 ^ n
    t1 = t1 % 16777216
    t2 = t1 // 32
    t2 = t2 ^ t1
    t2 = t2 % 16777216
    t3 = t2 * 2048
    t3 = t3 ^ t2
    t3 = t3 % 16777216
    return t3

total = 0

for line in myinput:
    secret = int(line)
    for c in range(2000):
        secret = next_secret(secret)
    total += secret

print(total)
