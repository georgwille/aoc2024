import re

myinput = open('input_03.txt').read()[:-1].split('\n')

myinput = ''.join(myinput)

total = 0

for line in myinput:
    result = re.findall(r'mul\(\d{1,3},\d{1,3}\)',line)
    for item in result:
        left,right = item.split(',')
        total += int(left[4:])*int(right[:-1])

print(total)
