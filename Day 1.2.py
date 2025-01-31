from collections import Counter

with open('input.txt') as file:
    input = file.read().split('\n')

left_list: list[int] = sorted([int(val.split('   ')[0]) for val in input])
right_list: list[int] = sorted([int(val.split('   ')[1]) for val in input])

right_list_count = Counter(right_list)

answer = sum(x * right_list_count[x] for x in left_list)

print(answer)
