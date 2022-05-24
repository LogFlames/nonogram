from nonogram_general import check, partial_check, partial_check_rows

def solve_rec(rows, cols, grid, x, y, sub_col_index):
    if grid is None:
        grid = [[False for _ in range(len(rows))] for _ in range(len(cols))]

    for i in range(len(rows) - y - sum(cols[x][sub_col_index:]) - (len(cols[x]) - sub_col_index - 1) + 1):
        for j in range(cols[x][sub_col_index]):
            grid[x][y + i + j] = True

        if not partial_check_rows(rows = rows, cols = cols, grid = grid, to_x = x, to_y = y + i + cols[x][sub_col_index]):
            for j in range(cols[x][sub_col_index]):
                grid[x][y + i + j] = False
            continue
        
        if sub_col_index + 1 >= len(cols[x]):
            if x + 1 >= len(cols):
                if check(rows, cols, grid):
                    return grid
            else:
                ret = solve_rec(rows = rows, cols = cols, grid = grid[:], x = x + 1, y = 0, sub_col_index = 0)

                if ret is not None:
                    return ret
        else:
            ret = solve_rec(rows = rows, cols = cols, grid = grid[:], x = x, y = y + i + cols[x][sub_col_index] + 1, sub_col_index = sub_col_index + 1)

            if ret is not None:
                return ret

        for j in range(cols[x][sub_col_index]):
            grid[x][y + i + j] = False

    return None

def solve(rows, cols):
    return solve_rec(rows = rows, cols = cols, grid = None, x = 0, y = 0, sub_col_index = 0)
