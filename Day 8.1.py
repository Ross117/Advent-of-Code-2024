with open('input.txt') as file:
    input = file.read()

map: list[list[str]] = [list(val) for val in input.split('\n')]
frequencies: set[str] = set([char for char in input if char != '.' and char != '\n'])

# the same antenna can be part of more than one pair

# the antinodes occur when one of the antennas is twice as far away as the other
# (some may be off the map)

# can consider each frequency in isolation - they don't impact each other

def find_same_freq_antennas(frequency: str) -> list[list[int]]:
    '''Return the indexes of all the antennas of the same frequency.'''

    indexes: list[list[int]] = []

    # refactor using list comprehension
    for row_ind, row in enumerate(map):
        for col_ind, val in enumerate(row):
            if val == frequency:
                indexes.append([row_ind, col_ind])

    return indexes

def find_antinodes(index_a: list[int], index_b: list[int]) -> list[list[int]]:
    '''Given a pair indexes which represent antennas of the same frequency,
    find the corresponding pair of antinodes. If the antinodes are located
    within the bounds of the map, return their indexes.'''

    antinodes: list[list[int]] = []

    row_diff: int = abs(index_a[0] - index_b[0])
    col_diff: int = abs(index_a[1] - index_b[1])

    antinode_a = [0, 0]
    antinode_b = [0, 0]

    # work out how to apply the offsets - refactor!!
    if index_a[0] < index_b[0]:
        antinode_a[0] = index_a[0] - row_diff
        antinode_b[0] = index_b[0] + row_diff
    elif index_a[0] > index_b[0]:
        antinode_a[0] = index_a[0] + row_diff
        antinode_b[0] = index_b[0] - row_diff
    else:
        antinode_a[0] = index_a[0] - row_diff
        antinode_b[0] = index_b[0] + row_diff

    if index_a[1] < index_b[1]:
        antinode_a[1] = index_a[1] - col_diff
        antinode_b[1] = index_b[1] + col_diff
    elif index_a[1] > index_b[1]:
        antinode_a[1] = index_a[1] + col_diff
        antinode_b[1] = index_b[1] - col_diff
    else:
        antinode_a[1] = index_a[1] - col_diff
        antinode_b[1] = index_b[1] + col_diff

    antinodes.extend([antinode_a, antinode_b])

    in_map_antinodes: list[list[int]] = [antinode for antinode in antinodes if antinode[0] >= 0 
                        and antinode[0] < len(map)
                        and antinode[1] >= 0 
                        and antinode[1] < len(map[0])]

    return in_map_antinodes


locations: list[str] = []

for freq in frequencies:
     
     antennas: list[list[int]] = find_same_freq_antennas(freq)
     
     for antenna in antennas:
        for i in range(len(antennas)):
            # refactor to make more efficient
            if antenna != antennas[i]:
                antinodes = find_antinodes(antenna, antennas[i])
                for antinode in antinodes:
                    locations.append(str(antinode[0]) + str(antinode[1]))

unique_locations: set[str] = set(locations)

answer: int = len(unique_locations)
print(answer)