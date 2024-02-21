from tkinter import *

def checkChanged(mainApp):
    tmp = mainApp.playerIndex[:1]  # Who is playing
    playerTurn = tmp[0]
    if playerTurn == 1:
        mainApp.player_1_checkbox.config(state=DISABLED)
        mainApp.player_1_label_2.config(state=DISABLED, disabledforeground="yellow")
        mainApp.updateIndexLog()

    elif playerTurn == 2:
        mainApp.player_2_checkbox.config(state=DISABLED)
        mainApp.player_2_label_2.config(state=DISABLED, disabledforeground="yellow")
        mainApp.updateIndexLog()

    elif playerTurn == 3:
        mainApp.player_3_checkbox.config(state=DISABLED)
        mainApp.player_3_label_2.config(state=DISABLED, disabledforeground="yellow")
        mainApp.updateIndexLog()

    elif playerTurn == 4:
        mainApp.player_4_checkbox.config(state=DISABLED)
        mainApp.player_4_label_2.config(state=DISABLED, disabledforeground="yellow")
        mainApp.updateIndexLog()

    return
