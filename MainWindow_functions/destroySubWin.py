from tkinter import *

def destroySubWin(MainWindow):
    if MainWindow.gameStarted == False:
        if MainWindow.nbPlayer < 4:
            MainWindow.button_addPlayer.configure(state='normal')

        MainWindow.button_gameMode.config(state=NORMAL)
    elif MainWindow.gameStarted == True:
        MainWindow.editNameMode = False
        MainWindow.button_editName.config(state='normal')

    MainWindow.subWin.destroy()
    return
