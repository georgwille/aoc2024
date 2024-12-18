myinput = open('input_04.txt').read()[:-1].split('\n')

def count_xmas(row, col):
    xmas_count = 0
    if not (myinput[row][col] == 'A'):
        return 0
    for dr1,dc1 in [(-1,-1),(1,1)]:
        for dr2,dc2 in [(-1,1),(1,-1)]:
            if not (myinput[row+dr1][col+dc1] == "M" and myinput[row-dr1][col-dc1] == "S"):
                continue
            if not (myinput[row+dr2][col+dc2] == "M" and myinput[row-dr2][col-dc2] == "S"):
                continue
            xmas_count += 1
    return xmas_count

total = 0

for r in range(1,len(myinput)-1):
    for c in range(1,len(myinput[0])-1):
        total += count_xmas(r,c)

print(total)


