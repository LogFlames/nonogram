def check(rows, cols, grid):
    for i, row in enumerate(rows):
        sub_row_index = 0
        length = 0
        for x in range(len(cols)):
            if grid[x][i]:
                length += 1
            elif length > 0:
                if sub_row_index >= len(row) and length == row[sub_row_index]:
                    sub_row_index += 1
                else:
                    return False

                length = 0

        if length > 0 and length != row[sub_row_index]:
            return False

        if sub_row_index != len(row) - 1:
            return False

    for i, col in enumerate(cols):
        sub_col_index = 0
        length = 0
        for y in range(len(rows)):
            if grid[i][y]:
                length += 1
            elif length > 0:
                if sub_col_index >= len(col) and length == col[sub_col_index]:
                    sub_col_index += 1
                else:
                    return False

                length = 0

        if length > 0 and length != col[sub_col_index]:
            return False

        if sub_col_index != len(col) - 1:
            return False

    return True
