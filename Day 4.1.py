with open('input.txt') as file:
    input = file.read().split('\n')

offsets: list[list[tuple[int]]] = [
    [(1, 0), (2, 0), (3, 0)], # verticle up
    [(-1, 0), (-2, 0), (-3, 0)], # verticle down
    [(0, 1), (0, 2), (0, 3)], # horizontal left
    [(0, -1), (0, -2), (0, -3)], # horizontal right
    [(1, 1), (2, 2), (3, 3)], # diagonal up left
    [(1, -1), (2, -2), (3, -3)], # diagonal up right
    [(-1, 1), (-2, 2), (-3, 3)], # diagonal down left
    [(-1, -1), (-2, -2), (-3, -3)] # diagonal down right
]

def xmas_matches(line_ind: int, char_ind: int) -> int:
    '''
    Test if the X character at the given position
    in the input is part of an 'XMAS' string. Return a
    count of how many different instances of 'XMAS' it's
    a part of
    '''
    xmas: int = 0

    for offset in offsets:
        try:
            if input[line_ind - offset[0][0]][char_ind - offset[0][1]] \
                + input[line_ind - offset[1][0]][char_ind - offset[1][1]] \
                + input[line_ind - offset[2][0]][char_ind - offset[2][1]]  == 'MAS':

                if not list(filter(lambda x: x < 0, [
                    line_ind,
                    char_ind,
                    line_ind - offset[0][0],
                    char_ind - offset[0][1],
                    line_ind - offset[1][0],
                    char_ind - offset[1][1],
                    line_ind - offset[2][0],
                    char_ind - offset[2][1]
                ])):
                    xmas += 1
        except IndexError:
            continue

    return xmas

matches: int = 0

for line_ind, line in enumerate(input):
    for char_ind, char in enumerate(line):
        if char == 'X':
            matches += xmas_matches(line_ind, char_ind)

answer: int = matches
print(answer)