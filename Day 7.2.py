import itertools

with open('input.txt') as file:
    input = file.read().split('\n')

input_cleaned: list[list[int | str]] = [[int(val.split(':')[0]), val.split(':')[1]] for val in input]
true_equations: list[int] = []


for equation in input_cleaned:
    test_value = equation[0]
    numbers: list[int] = [int(number) for number in equation[1].strip().split(' ')]

    permutations = list(itertools.product('+*|', repeat=(len(numbers) -1)))
    
    for permutation in permutations:
        running_total = numbers[0]
        for ind, operator in enumerate(permutation):
            if operator == '+':
                running_total += numbers[ind + 1]
            elif operator == '*':
                running_total *= numbers[ind + 1]
            elif operator == '|':
                running_total = int(str(running_total) + str(numbers[ind + 1]))
              
            if running_total > test_value:
                break
        
        if running_total == test_value: 
            true_equations.append(test_value)
            break        

answer = sum(true_equations)
print(answer)