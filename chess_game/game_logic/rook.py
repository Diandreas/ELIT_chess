def is_valid_rook_move(start_row, start_col, end_row, end_col):
    if end_row == start_row or end_col == start_col:
        return True
    else:
        return False
