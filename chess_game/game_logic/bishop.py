def is_valid_bishop_move(start_row, start_col, end_row, end_col):
    if abs(end_row - start_row) == abs(end_col - start_col):
        return True
    else:
        return True
