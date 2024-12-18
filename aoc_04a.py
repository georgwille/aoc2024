myinput = open('input_04.txt').read()[:-1].split('\n')

def count_xmas(row, col):
    xmas_count = 0
    if not (myinput[row][col] == 'X'):
        return 0
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            has_xmas = True
            for i,letter in enumerate('XMAS'):
                if row+i*dr < 0 or col+i*dc < 0:
                    has_xmas = False
                    break
                try:
                    if not(myinput[row+i*dr][col+i*dc] == letter):
                        has_xmas = False
                        break
                except:
                    has_xmas = False
                    break
            if has_xmas:
                xmas_count += 1
    return xmas_count

total = 0

for r in range(len(myinput)):
    for c in range(len(myinput[0])):
        total += count_xmas(r,c)

print(total)


