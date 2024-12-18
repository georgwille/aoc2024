rules, updates = open('input_05.txt').read()[:-1].split('\n\n')

rules = rules.split('\n')
rules = [(rule.split('|')[0],rule.split('|')[1]) for rule in rules]

updates = updates.split('\n')
updates = [item.split(',') for item in updates]

left_of = {}
right_of = {}

for l,r in rules:
    if l in right_of:
        right_of[l].append(r)
    else:
        right_of[l] = [r]
    if r in left_of:
        left_of[r].append(l)
    else:
        left_of[r] = [l]

valid_count = 0

for update in updates:
    update_is_valid = False
    flip_needed = False
    while not update_is_valid:
        update_is_valid = True
        for ii,l in enumerate(update[:-1]):
            for jj,r in enumerate(update[ii+1:]):
                if r in left_of.get(l,[]) or l in right_of.get(r,[]):
                    update_is_valid = False
                    flip_needed = True
                    temp = update[jj+ii+1]
                    del update[jj+ii+1]
                    update.insert(ii,temp)
                    # print(update)
                    break
            if not update_is_valid:
                break
    if flip_needed:
        valid_count += int(update[len(update)//2])

print(valid_count)