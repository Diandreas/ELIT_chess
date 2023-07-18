from tkinter import Tk, Button, Frame, PhotoImage
from PIL import Image, ImageTk

root = Tk()
root.title("Échiquier")
root.geometry("700x700")

# Créer des cadres
chessboard_frame = Frame(root)
chessboard_frame.pack(side="left", fill="both", expand=True)

button_frame = Frame(root)
button_frame.pack(side="right", fill="y")

# Créer un échiquier
colors = ["brown", "gray"]
buttons = []
photos = []
for i in range(8):
    row = []
    photo_row = []
    for j in range(8):
        button = Button(chessboard_frame, text="", bg=colors[(i+j)%2], font=("TkDefaultFont", 8), width=10, height=5)
        button.grid(row=i, column=j)
        row.append(button)
        photo_row.append(None)
    buttons.append(row)
    photos.append(photo_row)

# Créer des boutons
new_game_button = Button(button_frame, text="Nouvelle partie")
new_game_button.pack()

# Ajouter des images
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

root.mainloop()
