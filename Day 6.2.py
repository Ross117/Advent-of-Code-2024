import copy

with open('input.txt') as file:
    input = file.read().split('\n')

input_cleaned: list[list[str]] = [[val for val in row] for row in input]
start_index: list[int] = [[input_cleaned.index(row), row.index('^')] for row in input_cleaned if '^' in row][0]

def in_map(row_ind: int, col_ind: int) -> bool:
    '''Check if the given indexes both exist
    in the input'''

    if row_ind < 0 \
        or row_ind > len(input_cleaned) - 1 \
        or col_ind < 0 \
        or col_ind > len(input_cleaned[0]) - 1:
        return False
    
    return True


infinite_loops = 0

# for every '.' character in the input, replace it with '#' and see if this produces an infinite loop
for row_ind, row in enumerate(input_cleaned):
    for col_ind, col in enumerate(input_cleaned):
        amended_input = copy.deepcopy(input_cleaned)
        
        if amended_input[row_ind][col_ind] == '#' or amended_input[row_ind][col_ind] == '^':
            continue
        else:
           amended_input[row_ind][col_ind] = '#'

        iterations = 0
        position: list[int] = start_index
        in_area: bool = True
        direction: str = 'up'

        while in_area:
            
            if direction == 'up':
                if in_map(position[0] - 1, position[1]):
                    if amended_input[position[0] - 1][position[1]] == '#':
                        direction = 'right'
                    else:
                        position = [position[0] - 1, position[1]]
                else: 
                    in_area = False

            if direction == 'down':
                if in_map(position[0] + 1, position[1]):
                    if amended_input[position[0] + 1][position[1]] == '#':
                        direction = 'left'
                    else:
                        position = [position[0] + 1, position[1]]
                else: 
                    in_area = False
            
            if direction == 'left':
                if in_map(position[0], position[1] - 1):
                    if amended_input[position[0]][position[1] - 1] == '#':
                        direction = 'up'
                    else:
                        position = [position[0], position[1] - 1]
                else: 
                    in_area = False
            
            if direction == 'right':
                if in_map(position[0] - 1, position[1] + 1):
                    if amended_input[position[0]][position[1] + 1] == '#':
                        direction = 'down'
                    else:
                        position = [position[0], position[1] + 1]
                else: 
                    in_area = False

            if in_area:
                iterations += 1
                # assume this equates to an infinite loop
                if iterations > len(input) * len(input):
                    infinite_loops += 1
                    in_area = False
                
answer = infinite_loops
print(answer)