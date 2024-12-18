myinput = open('input_09.txt').readline().strip()+'0'

disk = []

print(len(myinput))

fileID = 0

for i in range(len(myinput)//2):
    disk.extend([fileID]*int(myinput[2*i]))
    disk.extend([-1]*int(myinput[2*i+1]))
    fileID += 1

while True:
    try:
        next_gap = disk.index(-1)
    except ValueError:
        break
    if next_gap == len(disk) - 1:
        disk.pop()
        break
    while True:
        last_filechunk = disk.pop()
        if last_filechunk > -1:
            break
    disk[next_gap] = last_filechunk

checksum = 0

for i,entry in enumerate(disk):
    checksum += i*entry

print(checksum)