from tkinter import *

def destroySubWin(mainApp):
    if mainApp.gameStarted == False:
        if mainApp.nbPlayer < 4:
            mainApp.button_addPlayer.configure(state='normal')

        mainApp.button_gameMode.config(state=NORMAL)
    elif mainApp.gameStarted == True:
        mainApp.editNameMode = False
        mainApp.button_editName.config(state='normal')

    mainApp.subWin.destroy()
    return
