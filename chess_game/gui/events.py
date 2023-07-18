from game_logic.king import is_valid_king_move
from game_logic.pawn import is_valid_pawn_move
from game_logic.queen import is_valid_queen_move
from game_logic.bishop import is_valid_bishop_move
from game_logic.rook import is_valid_rook_move
from game_logic.knight import is_valid_knight_move

selected_piece = None

def handle_left_click(event, board=None):
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
            move_piece(start_row, start_col, row, col)
            # Désélectionne la pièce
            selected_piece = None
        else:
            # Affiche un message d'erreur
            print("Mouvement invalide")
    else:
        # Sélectionne la pièce cliquée
        selected_piece = (row, col)

def is_valid_move(piece, start_row, start_col, end_row, end_col):
    if piece == "king":
        return is_valid_king_move(start_row, start_col, end_row, end_col)
    elif piece == "pawn":
        return is_valid_pawn_move(start_row, start_col, end_row, end_col)
    elif piece == "queen":
        return is_valid_queen_move(start_row, start_col, end_row, end_col)
    elif piece == "bishop":
        return is_valid_bishop_move(start_row, start_col, end_row, end_col)
    elif piece == "rook":
        return is_valid_rook_move(start_row, start_col, end_row, end_col)
    elif piece == "knight":
        return is_valid_knight_move(start_row, start_col, end_row, end_col)
    else:
        # Type de pièce inconnu
        return False

def move_piece(start_row, start_col, end_row, end_col, board=None):
    # Met à jour l'état de l'échiquier
    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = None

    # Met à jour l'affichage
    # ...
