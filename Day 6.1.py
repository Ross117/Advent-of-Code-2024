with open('input.txt') as file:
    input = file.read().split('\n')

start_index: list[int] = [[input.index(row), row.index('^')] for row in input if '^' in row][0]
indexes_visited: list[list[int]] = [start_index]

def in_map(row_ind, col_ind) -> bool:
    '''Check if the given indexes both exist
    in the input'''

    if row_ind < 0 \
        or row_ind > len(input) - 1 \
        or col_ind < 0 \
        or col_ind > len(input[0]) - 1:
        return False
    
    return True

direction: str = 'up'
position: list[int] = start_index
in_area: bool = True

while in_area:
    
    if direction == 'up':
        if in_map(position[0] - 1, position[1]):
            if input[position[0] - 1][position[1]] == '#':
                direction = 'right'
            else:
                position = [position[0] - 1, position[1]]
        else: 
            in_area = False

    if direction == 'down':
        if in_map(position[0] + 1, position[1]):
            if input[position[0] + 1][position[1]] == '#':
                direction = 'left'
            else:
                position = [position[0] + 1, position[1]]
        else: 
            in_area = False
    
    if direction == 'left':
        if in_map(position[0], position[1] - 1):
            if input[position[0]][position[1] - 1] == '#':
                direction = 'up'
            else:
                position = [position[0], position[1] - 1]
        else: 
            in_area = False
    
    if direction == 'right':
        if in_map(position[0] - 1, position[1] + 1):
            if input[position[0]][position[1] + 1] == '#':
                direction = 'down'
            else:
                position = [position[0], position[1] + 1]
        else: 
            in_area = False

    if in_area and position not in indexes_visited:
        indexes_visited.append(position)

answer = len(indexes_visited)
print(answer)