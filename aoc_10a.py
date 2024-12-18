myinput=open('input_10.txt').read()[:-1].split('\n')

def value_of(r,c):
    if myinput[r][c] == '9':
        return set([(r,c)])
    value = set()
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        if not 0<=r+dr<len(myinput):
            continue
        if not 0<=c+dc<len(myinput[0]):
            continue
        if myinput[r+dr][c+dc] == str(int(myinput[r][c])+1):
            value = value | value_of(r+dr,c+dc)
    return value

total = 0

for r,line in enumerate(myinput):
    for c,char in enumerate(line):
        if char == '0':
            total += len(value_of(r,c))

print(total)
