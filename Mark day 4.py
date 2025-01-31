fn = "input.txt"
word = "XMAS"

data = []
with open(fn) as f:
    for row in f:
        data.append(row.strip("\n"))

DIM = len(data)
# Iterators yield sequences seperated by "_"

def iterate_vertically(arr):
    for j in range(DIM):
        for i in range(DIM):
            yield arr[i][j]
        yield "_"


def iterate_horizontal(arr):
    for i in range(DIM):
        for j in range(DIM):
            yield arr[i][j]
        yield "_"


def iterate_diagonal(arr):
    # top-left to bottom-right
    for k in range(-DIM, DIM + 1):
        for j in range(DIM):
            i = k + j
            if 0 <= i < DIM:
                yield arr[j][i]
        yield "_"
    # top-right to bottom-left
    for k in range(2 * DIM + 1, 0, -1):
        for j in range(DIM):
            i = k - j
            if 0 <= i < DIM:
                yield arr[j][i]
        yield "_"


def seq(iterator, N):
    """
    yields strings of length :N:
    from iterator
    """
    def reset():
        return [next(iterator, None) for _ in range(N)]

    r = reset()
    while None not in r:
        R = "".join(r)

        yield R
        yield R[::-1]  # check reversed as well!
        r.pop(0)
        r.append(next(iterator, None))


count = 0
iterators = (iterate_horizontal(data),
             iterate_vertically(data), 
             iterate_diagonal(data))

total = 0
for iter_ in iterators:
    count = 0
    for p in seq(iter_, len(word)):
        if p == word:
            count += 1
    print(iter_.__name__, count)
    total += count

print(f"'{word}' has been found {total} times")

