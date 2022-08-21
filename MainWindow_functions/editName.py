from tkinter import *

def editName(MainWindow):
    if MainWindow.gameStarted:
        MainWindow.button_editName.config(state='disabled')
        MainWindow.editNameMode = True
        MainWindow.addPlayer()
    return
