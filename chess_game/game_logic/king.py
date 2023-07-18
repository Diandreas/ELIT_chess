def is_valid_king_move(start_row, start_col, end_row, end_col):
    if abs(end_row - start_row) <= 1 and abs(end_col - start_col) <= 1:
        return True
    else:
        return False
