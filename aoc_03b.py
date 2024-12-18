import re

myinput = open('input_03_sample_a.txt').read()[:-1].split('\n')

myinput = ''.join(myinput)
myinput = 'do()'+myinput+'don\'t()'
total = 0

filtered = re.findall(r"do\(\).+?don\'t\(\)",myinput)

for line in filtered:
    result = re.findall(r'mul\(\d{1,3},\d{1,3}\)',line)
    for item in result:
        left,right = item.split(',')
        total += int(left[4:])*int(right[:-1])

print(total)
