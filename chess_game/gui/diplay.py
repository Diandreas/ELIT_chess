from tkinter import Tk, Button
from PIL import Image, ImageTk

root = Tk()
root.title("Échiquier")
root.geometry("700x700")
white = 1
for i in range(8):
    if white==1:
        white=0
    else:
        white=1
    for j in range(8):
        if white == 1:
            button = Button(root, text="", bg="brown" , font=("TkDefaultFont", 8), width=10, height=5)
            button.grid(row=i, column=j)
            white=0
            
        else:
            button = Button(root, text="", bg="yellow" , font=("TkDefaultFont", 8), width=10, height=5)
            button.grid(row=i, column=j)
            white=1
        if i==6 and j==0:
            image=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/gui/pawn.png")
            photo=ImageTk.PhotoImage(image)
            button["image"]=photo
            button["width"]=65
            button["height"]=75
        if i==6 and j==1:
            image1=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/gui/pawn.png")
            photo1=ImageTk.PhotoImage(image1)
            button["image"]=photo1
            button["width"]=65
            button["height"]=75
        if i==6 and j==2:
            image2=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/gui/pawn.png")
            photo2=ImageTk.PhotoImage(image2)
            button["image"]=photo2
            button["width"]=65
            button["height"]=75
        if i==6 and j==2:
            image2=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/gui/pawn.png")
            photo2=ImageTk.PhotoImage(image2)
            button["image"]=photo2
            button["width"]=65
            button["height"]=75
        if i==6 and j==3:
            image3=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/gui/pawn.png")
            photo3=ImageTk.PhotoImage(image3)
            button["image"]=photo3
            button["width"]=65
            button["height"]=75
        if i==6 and j==4:
            image4=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/gui/pawn.png")
            photo4=ImageTk.PhotoImage(image4)
            button["image"]=photo4
            button["width"]=65
            button["height"]=75
        if i==6 and j==5:
            image5=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/gui/pawn.png")
            photo5=ImageTk.PhotoImage(image5)
            button["image"]=photo5
            button["width"]=65
            button["height"]=75
        if i==6 and j==6:
            image6=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/gui/pawn.png")
            photo6=ImageTk.PhotoImage(image6)
            button["image"]=photo6
            button["width"]=65
            button["height"]=75
        if i==6 and j==7:
            image7=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/gui/pawn.png")
            photo7=ImageTk.PhotoImage(image7)
            button["image"]=photo7
            button["width"]=65
            button["height"]=75
        


root.mainloop()
