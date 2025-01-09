with open('input.txt') as file:
    input = file.read().split('\n')

left_list: list[int] = sorted([int(val.split('   ')[0]) for val in input])
right_list: list[int] = sorted([int(val.split('   ')[1]) for val in input])

similarity_score: int = 0

for i in range(len(left_list)):
    similarity_score += left_list[i] * right_list.count(left_list[i])

answer = similarity_score

print(answer)