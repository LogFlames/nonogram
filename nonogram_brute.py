from nonogram_general import check

def solve(rows, cols):
    grid = [[ False for _ in range(len(rows))] for _ in range(len(cols))]

    for i in range(0, 2**(len(cols) * len(rows))):
        if not i % 100000:
            print(f"{int(i / 2**(len(cols) * len(rows)) * 10000.0) / 100.0}%")
        for y in range(len(rows)):
            for x in range(len(cols)):
                grid[x][y] = True if i & (1 << (y * len(cols) + x)) else False

        if check(rows = rows, cols = cols, grid = grid):
            return grid

    return None

