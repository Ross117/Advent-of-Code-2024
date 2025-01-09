import regex as re

with open('input.txt') as file:
    input = file.read().replace('\n', '')

# remove from the input string all sections which start with don't() up until do()
reg_ex_for_removal = re.compile(r"don\'t\(\).*?(?=do\(\))")
input_cleaned = re.sub(reg_ex_for_removal, '', input)

reg_ex_for_numbers = re.compile(r"mul\((\d{1,3},\d{1,3})\)")
matches = re.findall(reg_ex_for_numbers, input_cleaned)

answer = sum([int(val.split(',')[0]) * int(val.split(',')[1]) for val in matches])

print(answer)