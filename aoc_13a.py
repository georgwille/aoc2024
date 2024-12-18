myinput = open('input_13_sample.txt').read()[:-1].split('\n\n')

total = 0

for item in myinput:
    l1, l2, l3 = item.split('\n')
    l1 = l1[11:]
    l2 = l2[11:]
    l3 = l3[9:]
    x1 = int(l1.split(',')[0])
    y1 = int(l1.split('+')[2])
    x2 = int(l2.split(',')[0])
    y2 = int(l2.split('+')[2])
    xs = int(l3.split(',')[0])
    ys = int(l3.split('=')[1])
    found = False
    for a in range(101):
        for b in range(101):
            if a*x1+b*x2 == xs and a*y1+b*y2==ys:
                total += 3*a+b
                print(x1,y1,a,b)
                found = True
                break
        if found:
            break

print(total)
