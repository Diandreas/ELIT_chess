from tkinter import Tk, Button, Frame
from PIL import Image, ImageTk
from events import handle_left_click

root = Tk()
root.title("Échiquier")
root.geometry("700x700")

chessboard_frame = Frame(root)
chessboard_frame.pack(side="left", fill="both", expand=True)

button_frame = Frame(root)
button_frame.pack(side="right", fill="y")

colors = ["brown", "#F9E3E5"]
global buttons
buttons = []
global photos
photos = []
for i in range(8):
    row = []
    photo_row = []
    for j in range(8):
        button = Button(chessboard_frame, text="", bg=colors[(i+j)%2], font=("TkDefaultFont", 8), width=10, height=5)
        button.grid(row=i, column=j)
        button.bind("<Button-1>", lambda event: handle_left_click(event, board, buttons))
        row.append(button)
        photo_row.append(None)
    buttons.append(row)
    photos.append(photo_row)

new_game_button = Button(button_frame, text="Nouvelle parties")
new_game_button.pack()

pieces = ["pawn", "rook", "knight", "bishop", "queen", "king"]
for i in range(8):
    for j in range(8):
        if i == 0 or i == 7:
            if j == 0 or j == 7:
                piece = "rook"
            elif j == 1 or j == 6:
                piece = "knight"
            elif j == 2 or j == 5:
                piece = "bishop"
            elif j == 3:
                piece = "king"
            else:
                piece = "queen"
        elif i == 1:
            piece = "pawn"
        elif i == 6:
            piece = "pawn"
        else:
            piece = None

        if piece is not None:
            if i < 2:
                color = "black"
            else:
                color = "white"

            image_path = f"../assets/model/piece_model_1/{color}/{piece}.png"
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
            photos[i][j] = photo
            buttons[i][j]["image"] = photos[i][j]
            buttons[i][j]["width"] = 65
            buttons[i][j]["height"] = 75

# Initialisation de l'échiquier
board = [[None for j in range(8)] for i in range(8)]
# Ajouter les pièces initiales sur l'échiquier
for i in range(8):
    for j in range(8):
        if i == 0 or i == 7:
            if j == 0 or j == 7:
                piece = "rook"
            elif j == 1 or j == 6:
                piece = "knight"
            elif j == 2 or j == 5:
                piece = "bishop"
            elif j == 3:
                piece = "king"
            else:
                piece = "queen"
        elif i == 1:
            piece = "pawn"
        elif i == 6:
            piece = "pawn"
        else:
            piece = None

        board[i][j] = piece


root.mainloop()
