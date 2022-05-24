from nonogram_general import *
import nonogram_brute
import nonogram_smarter_brute

#from nonograms import ng_1x3_001 as ng
#from nonograms import ng_2x2_001 as ng
#from nonograms import ng_1x4_001 as ng
#from nonograms import ng_5x5_001 as ng
#from nonograms import ng_5x5_002 as ng
#from nonograms import ng_5x6_001 as ng
#from nonograms import ng_9x9_001 as ng
from nonograms import ng_16x14_001 as ng
#from nonograms import ng_18x30_001 as ng
#from nonograms import ng_25x25_001 as ng

def main():
    grid = nonogram_smarter_brute.solve(rows = ng.rows, cols = ng.cols)
    if grid is None:
        print("No solution")
        print_rows_cols(rows = ng.rows, cols = ng.cols)
    else:
        print_rows_cols_grid(rows = ng.rows, cols = ng.cols, grid = grid)

if __name__ == "__main__":
    main()

