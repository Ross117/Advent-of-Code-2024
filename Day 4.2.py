with open('input.txt') as file:
    input = file.read().split('\n')

offsets: list[list[tuple[int]]] = [
    [(1, 1), (-1, -1)], # diagonal top left - bottom right
    [(-1, 1), (1, -1)], # diagonal bottom left - top right
    [(-1, -1), (1, 1)], # diagonal bottom right - top left
    [(1, -1), (-1, 1)] # diagonal top right- bottom left
]

def found_x_mas(line_ind: int, char_ind: int) -> bool:
    '''
    Test if the A character at the given position
    in the input is part of an X-shaped 'MAS' pattern.
    Return True if it is, False otherwise.
    '''
    x_mas: int = 0

    for offset in offsets:
        try:
            if input[line_ind - offset[0][0]][char_ind - offset[0][1]] \
                + input[line_ind][char_ind] \
                + input[line_ind - offset[1][0]][char_ind - offset[1][1]]  == 'MAS':
                
                # need to discard any matches found through using negative indexes
                check_for_negative_indexes: list[int] = list(filter(lambda x: x < 0, [line_ind, 
                    char_ind,
                    line_ind - offset[0][0],
                    char_ind - offset[0][1],
                    line_ind - offset[1][0],
                    char_ind - offset[1][1]
                    ]))
                
                if len(check_for_negative_indexes) == 0:
                        x_mas += 1
        except IndexError:
            continue

    if x_mas == 2:
        return True
    else:
        return False

matches: int = 0

for line_ind, line in enumerate(input):
    for char_ind, char in enumerate(line):
        if char == 'A':
            if found_x_mas(line_ind, char_ind):
                matches += 1

answer: int = matches
print(answer)