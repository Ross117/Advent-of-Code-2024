with open('input.txt') as file:
    input = file.read().split('\n')

left_list: list[int] = sorted([int(val.split('   ')[0]) for val in input])
right_list: list[int] = sorted([int(val.split('   ')[1]) for val in input])

answer: int = sum(abs(x - y) for x, y in zip(left_list, right_list))

print(answer)
