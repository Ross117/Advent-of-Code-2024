with open('input.txt') as file:
    input = file.read().split('\n\n')

order_rules: list[list[int]] = [[int(val[0]), int(val[1])] for val in [val.split('|') for val in input[0].split('\n')]]
updates: list[list[int]] = [[int(val) for val in val.split(',')] for val in input[1].split('\n')]

middle_numbers = []

for update in updates:
    right_order = True
    for ind, pagenumber in enumerate(update[:-1]):
        if [update[ind + 1], pagenumber] in order_rules:
            right_order = False
            break
    if right_order:
        middle_numbers.append(update[int((len(update) - 1) / 2)])

answer = sum(middle_numbers)
print(answer)