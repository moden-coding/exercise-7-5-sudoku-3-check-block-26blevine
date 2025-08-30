# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    check = []
    for row in range (row_no, row_no+3):
        for col in range (column_no, column_no+3):
            check.append(sudoku[row][col])
    for val in range(1, 10):
            seen_once = False
            for num in check:
                if num == val:
                    if not seen_once:
                        seen_once = True
                    else:
                        return False
    return True



if __name__ == "__main__":
 
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))