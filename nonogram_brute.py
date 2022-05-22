from nonogram_general import check

from nonograms import small_5x5_002 as ng

grid = [[ False for _ in range(len(ng.rows))] for _ in range(len(ng.cols))]

for i in range(0, 2**(len(ng.cols) * len(ng.rows))):
    if not i % 100000:
        print(f"{int(i / 2**(len(ng.cols) * len(ng.rows)) * 10000.0) / 100.0}%")
    for y in range(len(ng.rows)):
        for x in range(len(ng.cols)):
            grid[x][y] = True if i & (1 << (y * len(ng.cols) + x)) else False

    if check(rows = ng.rows, cols = ng.cols, grid = grid):
        print(grid)

