import numpy as np
from collections import defaultdict

myinput = open('input_22.txt').read().strip().split('\n')
n = np.zeros((len(myinput),2001),dtype='int64')
prune = 16777215

def next_secret(n):
    t1 = n << 6
    t1 = t1 ^ n
    t1 = t1 & prune
    t2 = t1 >> 5
    t2 = t2 ^ t1
    t2 = t2 & prune
    t3 = t2 << 11
    t3 = t3 ^ t2
    t3 = t3 & prune
    return t3

for b,line in enumerate(myinput):
    secret = int(line)
    n[b,0] = secret
    for c in range(1,2001):
        n[b,c] = next_secret(n[b,c-1])

print(np.sum(n[:,2000]))

d = (n[:,1:]%10)-(n[:,:-1]%10)
best_so_far = 0
keysum = defaultdict(int)

for b in range(len(myinput)):
    key_seen = set()
    for idx in range(1997):
        key = tuple(d[b,idx:idx+4])
        if key in key_seen:
            continue
        else:
            keysum[key] += (n[b,idx+4]%10)
            best_so_far = max(best_so_far, keysum[key])
            key_seen.add(key)

print(best_so_far)
