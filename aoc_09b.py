myinput = open('input_09.txt').readline().strip()+'0'

disk = []
flen = []
fpos = []

fileID = 0

for i in range(len(myinput)//2):
    flen.append([])
    fpos.append([])
    flen[fileID] = int(myinput[2*i])
    fpos[fileID] = len(disk)
    disk.extend([fileID]*int(myinput[2*i]))
    disk.extend([-1]*int(myinput[2*i+1]))
    fileID += 1

disk.extend([-1]*10)

# print(flen)
# print(fpos)
# print(disk)

def next_gap(offset):
    try:
        gpos = disk.index(-1, offset)
    except ValueError:
        gpos = 10**10
        glen = 0
        return gpos, glen
    glen = 0
    while gpos+glen < len(disk) and disk[gpos+glen] == -1:
        glen += 1
    return gpos, glen

# print(disk)

for fileID in reversed(range(len(flen))):
    # print(fileID)
    offset = 0
    glen = 0
    gpos = 0
    while glen < flen[fileID] and gpos < fpos[fileID]:
        gpos, glen = next_gap(gpos+glen+1)
    if gpos >= fpos[fileID]:
        continue
    else:
        for i in range(flen[fileID]):
            disk[gpos+i] = fileID
            disk[fpos[fileID]+i] = -1
        fpos[fileID] = gpos
    # print(disk)
    # input()

# print(disk)

checksum = 0

for i,entry in enumerate(disk):
    if entry == -1:
        continue
    checksum += i*entry

print(checksum)
