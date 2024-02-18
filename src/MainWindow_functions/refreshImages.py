from tkinter import *
from PIL import ImageTk, Image

def refreshImages(MainWIndow):
    global logoImage
    global arrowImage

    MainWIndow.BackgroundFrame.grid(row=0, column=0, sticky=NSEW)
    logoImage = ImageTk.PhotoImage(Image.open("./data/images/dart_Logo2.sgi"))
    MainWIndow.logoImage = Label(MainWIndow.emptylabel_3, image=logoImage, bg=MainWIndow.Button_bg_color, fg="grey")
    MainWIndow.logoImage.grid(row=1, column=1, columnspan=2)
    if MainWIndow.gameStarted:

        arrowImage = ImageTk.PhotoImage(Image.open("./data/images/arrow.sgi"))
        currentPlayer = MainWIndow.playerIndex[:1]

        if currentPlayer == [1]:
            MainWIndow.arrowImage = Label(MainWIndow.arrowLabel_1, image=arrowImage, bg=MainWIndow.Button_bg_color, fg="grey")
            MainWIndow.arrowImage.grid(row=1, column=1)
        if currentPlayer == [2]:
            MainWIndow.arrowImage = Label(MainWIndow.arrowLabel_2, image=arrowImage, bg=MainWIndow.Button_bg_color, fg="grey")
            MainWIndow.arrowImage.grid(row=1, column=1)
        if currentPlayer == [3]:
            MainWIndow.arrowImage = Label(MainWIndow.arrowLabel_3, image=arrowImage, bg=MainWIndow.Button_bg_color, fg="grey")
            MainWIndow.arrowImage.grid(row=1, column=1)
        if currentPlayer == [4]:
            MainWIndow.arrowImage = Label(MainWIndow.arrowLabel_4, image=arrowImage, bg=MainWIndow.Button_bg_color, fg="grey")
            MainWIndow.arrowImage.grid(row=1, column=1)
    return
