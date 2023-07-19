def is_valid_knight_move(start_row, start_col, end_row, end_col):
    if (abs(end_row - start_row) == 2 and abs(end_col - start_col) == 1) or (abs(end_row - start_row) == 1 and abs(end_col - start_col) == 2):
        return True
    else:
        return True
