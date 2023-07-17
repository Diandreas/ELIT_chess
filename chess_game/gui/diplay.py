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
            image=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/white/pawn.png")
            photo=ImageTk.PhotoImage(image)
            button["image"]=photo
            button["width"]=65
            button["height"]=75
        if i==6 and j==1:
            image1=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/white/pawn.png")
            photo1=ImageTk.PhotoImage(image1)
            button["image"]=photo1
            button["width"]=65
            button["height"]=75
        if i==6 and j==2:
            image2=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/white/pawn.png")
            photo2=ImageTk.PhotoImage(image2)
            button["image"]=photo2
            button["width"]=65
            button["height"]=75
        if i==6 and j==2:
            image2=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/white/pawn.png")
            photo2=ImageTk.PhotoImage(image2)
            button["image"]=photo2
            button["width"]=65
            button["height"]=75
        if i==6 and j==3:
            image3=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/white/pawn.png")
            photo3=ImageTk.PhotoImage(image3)
            button["image"]=photo3
            button["width"]=65
            button["height"]=75
        if i==6 and j==4:
            image4=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/white/pawn.png")
            photo4=ImageTk.PhotoImage(image4)
            button["image"]=photo4
            button["width"]=65
            button["height"]=75
        if i==6 and j==5:
            image5=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/white/pawn.png")
            photo5=ImageTk.PhotoImage(image5)
            button["image"]=photo5
            button["width"]=65
            button["height"]=75
        if i==6 and j==6:
            image6=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/white/pawn.png")
            photo6=ImageTk.PhotoImage(image6)
            button["image"]=photo6
            button["width"]=65
            button["height"]=75
        if i==6 and j==7:
            image7=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/white/pawn.png")
            photo7=ImageTk.PhotoImage(image7)
            button["image"]=photo7
            button["width"]=65
            button["height"]=75
        if i==1 and j==0:
            image8=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/black/pawn black.png")
            photo8=ImageTk.PhotoImage(image8)
            button["image"]=photo8
            button["width"]=65
            button["height"]=75
        if i==1 and j==1:
            image9=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/black/pawn black.png")
            photo9=ImageTk.PhotoImage(image9)
            button["image"]=photo9
            button["width"]=65
            button["height"]=75
        if i==1 and j==2:
            image10=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/black/pawn black.png")
            photo10=ImageTk.PhotoImage(image10)
            button["image"]=photo10
            button["width"]=65
            button["height"]=75
        if i==1 and j==3:
            image11=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/black/pawn black.png")
            photo11=ImageTk.PhotoImage(image11)
            button["image"]=photo11
            button["width"]=65
            button["height"]=75
        if i==1 and j==4:
            image12=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/black/pawn black.png")
            photo12=ImageTk.PhotoImage(image12)
            button["image"]=photo12
            button["width"]=65
            button["height"]=75
        if i==1 and j==5:
            image13=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/black/pawn black.png")
            photo13=ImageTk.PhotoImage(image13)
            button["image"]=photo13
            button["width"]=65
            button["height"]=75
        if i==1 and j==6:
            image14=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/black/pawn black.png")
            photo14=ImageTk.PhotoImage(image14)
            button["image"]=photo14
            button["width"]=65
            button["height"]=75
        if i==1 and j==7:
            image15=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/black/pawn black.png")
            photo15=ImageTk.PhotoImage(image15)
            button["image"]=photo15
            button["width"]=65
            button["height"]=75
        if i==0 and j==0:
            image16=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/black/root black.png")
            photo16=ImageTk.PhotoImage(image16)
            button["image"]=photo16
            button["width"]=65
            button["height"]=75
        if i==0 and j==7:
            image17=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/black/root black.png")
            photo17=ImageTk.PhotoImage(image17)
            button["image"]=photo17
            button["width"]=65
            button["height"]=75
        if i==0 and j==1:
            image18=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/black/knight black.png")
            photo18=ImageTk.PhotoImage(image18)
            button["image"]=photo18
            button["width"]=65
            button["height"]=75
        if i==0 and j==6:
            image19=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/black/knight black.png")
            photo19=ImageTk.PhotoImage(image19)
            button["image"]=photo19
            button["width"]=65
            button["height"]=75
        if i==0 and j==2:
            image20=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/black/bishop black.png")
            photo20=ImageTk.PhotoImage(image20)
            button["image"]=photo20
            button["width"]=65
            button["height"]=75
        if i==0 and j==5:
            image21=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/black/bishop black.png")
            photo21=ImageTk.PhotoImage(image21)
            button["image"]=photo21
            button["width"]=65
            button["height"]=75
        if i==0 and j==3:
            image22=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/black/black.png")
            photo22=ImageTk.PhotoImage(image22)
            button["image"]=photo22
            button["width"]=65
            button["height"]=75
        if i==0 and j==4:
            image23=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/black/king black.png")
            photo23=ImageTk.PhotoImage(image23)
            button["image"]=photo23
            button["width"]=65
            button["height"]=75
        if i==7 and j==0:
            image24=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/white/root.png")
            photo24=ImageTk.PhotoImage(image24)
            button["image"]=photo24
            button["width"]=65
            button["height"]=75
        if i==7 and j==7:
            image25=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/white/root.png")
            photo25=ImageTk.PhotoImage(image25)
            button["image"]=photo25
            button["width"]=65
            button["height"]=75
        if i==7 and j==1:
            image26=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/white/knight.png")
            photo26=ImageTk.PhotoImage(image26)
            button["image"]=photo26
            button["width"]=65
            button["height"]=75
        if i==7 and j==6:
            image27=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/white/knight.png")
            photo27=ImageTk.PhotoImage(image27)
            button["image"]=photo27
            button["width"]=65
            button["height"]=75
        if i==7 and j==2:
            image28=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/white/bishop.png")
            photo28=ImageTk.PhotoImage(image28)
            button["image"]=photo28
            button["width"]=65
            button["height"]=75
        if i==7 and j==5:
            image29=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/white/bishop.png")
            photo29=ImageTk.PhotoImage(image29)
            button["image"]=photo29
            button["width"]=65
            button["height"]=75
        if i==7 and j==3:
            image30=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/white/queen.png")
            photo30=ImageTk.PhotoImage(image30)
            button["image"]=photo30
            button["width"]=65
            button["height"]=75
        if i==7 and j==4:
            image31=Image.open("C:/Users/isalph2/OneDrive/Documents/GitHub/ELIT_chess/chess_game/assets/model/piece_model_1/white/king.png")
            photo31=ImageTk.PhotoImage(image31)
            button["image"]=photo31
            button["width"]=65
            button["height"]=75
        
        
        

        
        
        


root.mainloop()
