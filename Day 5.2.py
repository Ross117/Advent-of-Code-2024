with open('input.txt') as file:
    input = file.read().split('\n\n')

order_rules: list[list[int]] = [[int(val[0]), int(val[1])] for val in [val.split('|') for val in input[0].split('\n')]]
updates: list[list[int]] = [[int(val) for val in val.split(',')] for val in input[1].split('\n')]

incorrect_order_updates = []

for update in updates:
    right_order = True
    for ind, pagenumber in enumerate(update[:-1]):
        if [update[ind + 1], pagenumber] in order_rules:
            right_order = False
            break
    if not right_order:
        incorrect_order_updates.append(update)

def reorder(update):

    fixed_update = [0 for val in update]

    for pagenumber in update:
        new_index = 0
        for i in range(len(update)):
            if update[i] == pagenumber:
                continue
            elif [update[i], pagenumber] in order_rules:
                new_index += 1
        fixed_update[new_index] = pagenumber

    return fixed_update

fixed_updates = [reorder(incorrect_order_update) for incorrect_order_update in incorrect_order_updates]
answer = sum([fixed_update[int((len(fixed_update) - 1) / 2)] for fixed_update in fixed_updates])
    
print(answer)