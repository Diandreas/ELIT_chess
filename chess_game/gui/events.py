from game_logic.king import is_valid_king_move
from game_logic.pawn import is_valid_pawn_move
from game_logic.queen import is_valid_queen_move
from game_logic.bishop import is_valid_bishop_move
from game_logic.rook import is_valid_rook_move
from game_logic.knight import is_valid_knight_move

selected_piece = None


def update_board_display(board):
    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece is not None:
                # Mettre à jour l'affichage pour montrer la pièce sur la case (i,j)
                pass
            else:
                # Mettre à jour l'affichage pour ne rien montrer sur la case (i,j)
                pass


def handle_left_click(event, board):
    print("handle_left_click called")
    global selected_piece

    # Récupère les coordonnées de la case cliquée
    row = event.widget.grid_info()["row"]
    col = event.widget.grid_info()["column"]

    # Vérifie si une pièce est sélectionnée
    if selected_piece is not None:
        start_row, start_col = selected_piece
        piece = board[start_row][start_col]
        # Vérifie si le mouvement est valide
        if is_valid_move(piece, start_row, start_col, row, col):
            # Déplace la pièce
            move_piece(start_row, start_col, row, col, board)
            # Désélectionne la pièce
            selected_piece = None
            # Met à jour l'affichage de l'échiquier
            update_board_display(board)
        else:
            # Désélectionne la pièce
            selected_piece = None
    else:
        # Sélectionne la pièce cliquée
        selected_piece = (row, col)
        print(f"selected_piece: {selected_piece}")

def is_valid_move(piece, start_row, start_col, end_row, end_col):
    if piece == "king":
        result = is_valid_king_move(start_row, start_col, end_row, end_col)
    elif piece == "pawn":
        result = is_valid_pawn_move(start_row, start_col, end_row, end_col)
    elif piece == "queen":
        result = is_valid_queen_move(start_row, start_col, end_row, end_col)
    elif piece == "bishop":
        result = is_valid_bishop_move(start_row, start_col, end_row, end_col)
    elif piece == "rook":
        result = is_valid_rook_move(start_row, start_col, end_row, end_col)
    elif piece == "knight":
        result = is_valid_knight_move(start_row, start_col, end_row, end_col)
    else:
        print(f"")
        result = False

    print(f"is_valid_move: {result}")
    return result



def move_piece(start_row, start_col, end_row, end_col, board):
    # Met à jour l'état de l'échiquier
    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = None

    # Met à jour l'affichage
    # ...


def update_valid_moves_display(piece, start_row, start_col):
    for i in range(8):
        for j in range(8):
            if is_valid_move(piece, start_row, start_col, i, j):
                # Mettre à jour l'affichage pour montrer un petit rond sur la case (i,j)
                pass
