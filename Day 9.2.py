import copy
import regex

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

def check_for_free_space(size_of_file: int, rearranged_input: list[str]) -> int | None:
    ''''''

    pattern = ''.join([r'\.' for _ in range(size_of_file)])
    
    re = regex.compile(pattern)
    match = regex.search(re, ''.join([char[0] for char in rearranged_input]))
    
    # this should be the index of the first position of the match
    if match:
        return match.regs[0][0]

    return None 

reformatted_input: list[str] = reformat_input(input)
rearranged_input: list[str] = copy.deepcopy(reformatted_input)
# keep track of files that have been attempted to be moved
file_ids_encountered: set[str] = set([])

# iterate in reverse order
ind: int = len(reformatted_input)
for char in reformatted_input[::-1]:

    ind -= 1
    
    # skip free space & file blocks which are part of files which have already
    # been attempted to be moved
    if char == '.' or char in file_ids_encountered:
        continue

    file_ids_encountered.add(char)

    size_of_file: int = reformatted_input.count(char)
    file: list[str] = [char for _ in range(size_of_file)]

    first_free_space: int | None = check_for_free_space(size_of_file, rearranged_input)

    if not first_free_space or first_free_space > ind:
        continue

    # move the file to the left-most available block of free space that is big enough for it
    # if no free space big enough is available, don't move the file
    rearranged_input[first_free_space: (first_free_space + size_of_file)] = file
    # replace the file's former position with free space
    rearranged_input[((ind + 1) - size_of_file): (ind + 1)] = ['.' for _ in range(size_of_file)]

answer: int = sum([ind * int(char) for ind, char in enumerate(rearranged_input) if char != '.'])
print(answer)