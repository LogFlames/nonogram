def partial_check_rows(rows, cols, grid, to_x, to_y):
    for i, row in enumerate(rows):
        sub_row_index = 0
        length = 0
        full_check = True
        for x in range(len(cols)):
            if x >= (to_x if i < to_y else to_x - 1):
                full_check = False
                break

            if grid[x][i]:
                length += 1
            elif length > 0:
                if sub_row_index < len(row) and length == row[sub_row_index]:
                    sub_row_index += 1
                else:
                    return False

                length = 0

        if length > 0:
            if sub_row_index >= len(row) or \
                (length != row[sub_row_index] and full_check or \
                        length > row[sub_row_index] and not full_check):
                return False
            else:
                sub_row_index += 1

        if full_check and sub_row_index != len(row):
            return False

    return True

def partial_check_cols(rows, cols, grid, to_x, to_y):
    for i, col in enumerate(cols):
        if i > to_x:
            break

        sub_col_index = 0
        length = 0
        full_check = True
        for y in range(len(rows)):
            if i == to_x and y >= to_y:
                full_check = False
                break

            if grid[i][y]:
                length += 1
            elif length > 0:
                if sub_col_index < len(col) and length == col[sub_col_index]:
                    sub_col_index += 1
                else:
                    return False

                length = 0

        if length > 0:
            if sub_col_index >= len(col) or \
                (length != col[sub_col_index] and full_check or \
                length > col[sub_col_index] and not full_check):
                return False
            else:
                sub_col_index += 1

        if full_check and sub_col_index != len(col):
            return False

    return True

def partial_check(rows, cols, grid, to_x, to_y):
    return partial_check_rows(rows = rows, cols = cols, grid = grid, to_x = to_x, to_y = to_y) and \
           partial_check_cols(rows = rows, cols = cols, grid = grid, to_x = to_x, to_y = to_y)

def check(rows, cols, grid):
    return partial_check(rows = rows, cols = cols, grid = grid, to_x = len(cols), to_y = len(rows))

def print_rows_cols(rows, cols, scale = 2, keep_scale_even = True):
    if len(rows) == 0 or len(cols) == 0:
        print("Empty rows or cols")
        return

    longest_num = 0
    for col in cols:
        for c in col:
            if len(str(c)) > longest_num:
                longest_num = len(str(c))
    for row in rows:
        for r in row:
            if len(str(r)) > longest_num:
                longest_num = len(str(r))

    scale = max(scale, longest_num + 1)
    if keep_scale_even:
        scale += scale % 2

    col_lines = [[" " for _ in range(len(cols))] for _ in range(max(map(len, cols)))]
    row_lines = ["" for _ in range(len(rows))]

    for i, col in enumerate(cols):
        for j in range(len(col)):
            col_lines[j][i] = str(col[j]) + " " * (scale - len(str(col[j])))
        for j in range(len(col), len(col_lines)):
            col_lines[j][i] = " " * scale

    for i, row in enumerate(rows):
        for j in range(len(row)):
            row_lines[i] += str(row[j]) + " " * (scale - len(str(row[j])))

    max_row_len = max(map(len, row_lines))
    max_col_len = 0
    
    for line in col_lines:
        row_print = " " * (max_row_len) + "|" + "".join(line)
        print(row_print)
        max_col_len = max(max_col_len, len(row_print))

    print("-" * max_row_len + "|" + "-" * (max_col_len - max_row_len - 1))

    for line in row_lines:
        print(" " * (max_row_len - len(line)) + line + "|")
        for _ in range(max(scale // 2, 1) - 1):
            print(" " * max_row_len + "|")

def print_grid(grid, scale = 2):
    if grid is None or len(grid) == 0:
        print("Empty grid")
        return

    lines = ["" for _ in range(len(grid[0]))]
    for col in grid:
        for j in range(len(col)):
            lines[j] += ("\u2588" if col[j] else " ") * scale

    for line in lines:
        for _ in range(max(scale // 2, 1)):
            print(line)

def print_rows_cols_grid(rows, cols, grid, scale = 2, keep_scale_even = True):
    if grid is None or len(grid) == 0:
        print("Empty grid")
        return

    if len(rows) == 0 or len(cols) == 0:
        print("Empty rows or cols")
        return

    longest_num = 0
    for col in cols:
        for c in col:
            if len(str(c)) > longest_num:
                longest_num = len(str(c))
    for row in rows:
        for r in row:
            if len(str(r)) > longest_num:
                longest_num = len(str(r))

    scale = max(scale, longest_num + 1)
    if keep_scale_even:
        scale += scale % 2

    col_lines = [[" " for _ in range(len(cols))] for _ in range(max(map(len, cols)))]
    row_lines = ["" for _ in range(len(rows))]

    for i, col in enumerate(cols):
        for j in range(len(col)):
            col_lines[j][i] = str(col[j]) + " " * (scale - len(str(col[j])))
        for j in range(len(col), len(col_lines)):
            col_lines[j][i] = " " * scale

    for i, row in enumerate(rows):
        for j in range(len(row)):
            row_lines[i] += str(row[j]) + " " * (scale - len(str(row[j])))

    max_row_len = max(map(len, row_lines))
    max_col_len = 0
    
    for line in col_lines:
        row_print = " " * (max_row_len) + "|" + "".join(line)
        print(row_print)
        max_col_len = max(max_col_len, len(row_print))

    print("-" * max_row_len + "|" + "-" * (max_col_len - max_row_len - 1))

    grid_lines = ["" for _ in range(len(grid[0]))]
    for col in grid:
        for j in range(len(col)):
            grid_lines[j] += ("\u2588" if col[j] else " ") * scale

    for i in range(len(row_lines)):
        print(" " * (max_row_len - len(row_lines[i])) + row_lines[i] + "|" + grid_lines[i])
        for _ in range(max(scale // 2, 1) - 1):
            print(" " * max_row_len + "|" + grid_lines[i])
