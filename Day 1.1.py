with open('input.txt') as file:
    input = file.read().split('\n')

left_list: list[int] = sorted([int(val.split('   ')[0]) for val in input])
right_list: list[int] = sorted([int(val.split('   ')[1]) for val in input])

distance: int = 0

for i in range(len(left_list)):
    distance += abs(left_list[i] - right_list[i])

answer: int = distance

print(answer)