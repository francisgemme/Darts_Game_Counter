from tkinter import *

def selectedMode(MainWindow):
    selection = MainWindow.subWin.mode_var.get()
    if selection == 1:
        MainWindow.SelectedGameMode = "Standard 301"
    elif selection == 2:
        MainWindow.SelectedGameMode = "Standard 501"
    elif selection == 3:
        MainWindow.SelectedGameMode = "Around the Clock"
    elif selection == 4:
        MainWindow.SelectedGameMode = "180 Around the Clock"
    elif selection == 5:
        MainWindow.SelectedGameMode = "Baseball"
    elif selection == 6:
        MainWindow.SelectedGameMode = "Chase The Dragon"
    elif selection == 7:
        MainWindow.SelectedGameMode = "Cricket"

    concoleMsg = "You selected the option " + str(MainWindow.SelectedGameMode)
    print(concoleMsg)

    return
