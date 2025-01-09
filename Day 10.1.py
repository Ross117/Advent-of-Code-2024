with open('input.txt') as file:
    input = file.read().split('\n')

map: list[list[int]] = [[int(val) for val in list(val)] for val in input]

trailheads: list[int] = []

def in_map(row_ind, col_ind) -> bool:
    '''Check that we're still in bounds of the map'''

    if row_ind < 0 \
        or row_ind >= len(map) \
        or col_ind < 0 \
        or col_ind >= len(map[0]):
        return False

    return True

def find_summit_trails(row_ind: int, col_ind: int, trailhead_ind: int, summits_found: list[str]) -> None:
    '''Check if the trailhead leads to a summit.
    If it does, add it to the trailhead's score'''

    height: int = map[row_ind][col_ind]
    
    neighbours: list[list[int]] = [
        [row_ind - 1, col_ind], 
        [row_ind + 1, col_ind],
        [row_ind, col_ind - 1],
        [row_ind, col_ind + 1]
    ]

    for neightbour in neighbours:
        if in_map(neightbour[0], neightbour[1]):
            if map[neightbour[0]][neightbour[1]] - height == 1 and map[neightbour[0]][neightbour[1]] == 9 and str(neightbour[0]) + str(neightbour[1]) not in summits_found:
                trailheads[trailhead_ind] += 1
                summits_found.extend([str(neightbour[0]) + str(neightbour[1])])
            elif map[neightbour[0]][neightbour[1]] - height == 1:
                find_summit_trails(neightbour[0], neightbour[1], trailhead_ind, summits_found)

    return

            
for row_ind, row in enumerate(map):
    for col_ind, val in enumerate(row):
        if val == 0:
            trailheads.append(0)
            trailhead_ind: int = len(trailheads) - 1
            find_summit_trails(row_ind, col_ind, trailhead_ind, summits_found=[])

answer = sum(trailheads)

print(answer)