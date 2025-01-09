import regex as re

with open('input.txt') as file:
    input = file.read().replace('\n', '')

reg_ex_for_numbers = re.compile(r"mul\((\d{1,3},\d{1,3})\)")
matches = re.findall(reg_ex_for_numbers, input)

answer = sum([int(val.split(',')[0]) * int(val.split(',')[1]) for val in matches])

print(answer)