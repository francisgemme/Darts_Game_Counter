from tkinter import *
from PIL import ImageTk, Image

def refreshImages(mainApp):
    global logoImage
    global arrowImage

    mainApp.BackgroundFrame.grid(row=0, column=0, sticky=NSEW)
    logoImage = ImageTk.PhotoImage(Image.open("./data/images/dart_Logo2.sgi"))
    mainApp.logoImage = Label(mainApp.emptylabel_3, image=logoImage, bg=mainApp.Button_bg_color, fg="grey")
    mainApp.logoImage.grid(row=1, column=1, columnspan=2)
    if mainApp.match_inst.gameStarted:

        arrowImage = ImageTk.PhotoImage(Image.open("./data/images/arrow.sgi"))
        currentPlayer = mainApp.match_inst.playerIndex[:1]

        if currentPlayer == [1]:
            mainApp.arrowImage = Label(mainApp.arrowLabel_1, image=arrowImage, bg=mainApp.Button_bg_color, fg="grey")
            mainApp.arrowImage.grid(row=1, column=1)
        if currentPlayer == [2]:
            mainApp.arrowImage = Label(mainApp.arrowLabel_2, image=arrowImage, bg=mainApp.Button_bg_color, fg="grey")
            mainApp.arrowImage.grid(row=1, column=1)
        if currentPlayer == [3]:
            mainApp.arrowImage = Label(mainApp.arrowLabel_3, image=arrowImage, bg=mainApp.Button_bg_color, fg="grey")
            mainApp.arrowImage.grid(row=1, column=1)
        if currentPlayer == [4]:
            mainApp.arrowImage = Label(mainApp.arrowLabel_4, image=arrowImage, bg=mainApp.Button_bg_color, fg="grey")
            mainApp.arrowImage.grid(row=1, column=1)
    return
