myinput = open('input_13.txt').read()[:-1].split('\n\n')

offset = 10000000000000
# offset = 0
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
    xs = int(l3.split(',')[0])+offset
    ys = int(l3.split('=')[1])+offset
    
    if x2*y1-x1*y2 == 0:
        print("Determinant is zero")
        continue

    if (xs*y1-x1*ys) % (x2*y1-x1*y2) == 0:
        b = (xs*y1-x1*ys) // (x2*y1-x1*y2)
    else:
        continue

    if (xs*y2-x2*ys) % (x1*y2-x2*y1) == 0:
        a = (xs*y2-x2*ys) // (x1*y2-x2*y1)
    else:
        continue

    if a>=0 and b>=0:
        total += 3*a+b
        # print(x1,y1,a,b)
    else:
        print("Negative coefficient(s).")

print(total)
