from tkinter import *

def checkChanged(MainWindow):
    tmp = MainWindow.playerIndex[:1]  # Who is playing
    playerTurn = tmp[0]
    if playerTurn == 1:
        MainWindow.player_1_checkbox.config(state=DISABLED)
        MainWindow.player_1_label_2.config(state=DISABLED, disabledforeground="yellow")
        MainWindow.updateIndexLog()

    elif playerTurn == 2:
        MainWindow.player_2_checkbox.config(state=DISABLED)
        MainWindow.player_2_label_2.config(state=DISABLED, disabledforeground="yellow")
        MainWindow.updateIndexLog()

    elif playerTurn == 3:
        MainWindow.player_3_checkbox.config(state=DISABLED)
        MainWindow.player_3_label_2.config(state=DISABLED, disabledforeground="yellow")
        MainWindow.updateIndexLog()

    elif playerTurn == 4:
        MainWindow.player_4_checkbox.config(state=DISABLED)
        MainWindow.player_4_label_2.config(state=DISABLED, disabledforeground="yellow")
        MainWindow.updateIndexLog()

    return
