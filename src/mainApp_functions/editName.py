from tkinter import *

def editName(mainApp):
    if mainApp.gameStarted:
        mainApp.button_editName.config(state='disabled')
        mainApp.editNameMode = True
        mainApp.addPlayer()
    return
