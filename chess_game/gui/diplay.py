from tkinter import Tk, Button

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
            button = Button(root, text="", bg="white" , font=("TkDefaultFont", 8), width=10, height=5)
            button.grid(row=i, column=j)
            white=1


root.mainloop()
