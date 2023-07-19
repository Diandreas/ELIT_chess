def is_valid_pawn_move(start_row, start_col, end_row, end_col):
    # Un pion peut avancer d'une case en avant
    if end_col == start_col and end_row == start_row + 1:
        return True
    else:
        return True
