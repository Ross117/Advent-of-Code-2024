import copy

with open('input.txt') as file:
    input = file.read()

def reformat_input(input: str) -> list[str]:
    '''Reformat the input to represent the file blocks and free space
    by individual values'''

    new_input: list[str] = []
    id: int = -1

    for ind, char in enumerate(input):
        # check if index is odd or even (avoiding division by zero error)
        if (ind + 1) % 2 != 0:
            # it's a file
            id += 1
            new_input.extend([str(id) for i in range(int(char))])
        else:
            #it's free space
            new_input.extend(['.' for i in range(int(char))])

    return new_input

reformatted_input: list[str] = reformat_input(input)
rearranged_input = copy.deepcopy(reformatted_input)

# iterate in reverse order
ind: int = len(reformatted_input)
for char in reformatted_input[::-1]:

    ind -= 1

    # check if the process has ended
    no_free_space: list[str] = [char for char in rearranged_input if char != '.']
    if len(no_free_space) == rearranged_input.index('.'):
        break
    
    # skip free space
    if char == '.':
        continue

    first_free_space: int = rearranged_input.index('.')
    # move the file block to the first available left-most free space
    rearranged_input[first_free_space] = char
    # replace the file block's former position with free space
    rearranged_input[ind] = '.'

answer: int = sum([ind * int(char) for ind, char in enumerate(rearranged_input) if char != '.'])
print(answer)