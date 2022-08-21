from tkinter import *

def clearClickPad(MainWindow):
    # A class "Game" with its properties must be sent to this function
    # Transfer created player to the Lobby
    if MainWindow.editScoreMode == False:
        MainWindow.input_Score.config(state=NORMAL)
        MainWindow.input_Score.delete(0, END)
        MainWindow.input_Score.config(state=DISABLED)
        MainWindow.button_commitScore.configure(state=DISABLED)  # Clearing is also disabling the commit score button

    if MainWindow.editScoreMode == True:
        currentPlayer = MainWindow.playerIndex[:1]
        eval("MainWindow.player_" + str(currentPlayer[0]) + "_label_2.config(state=NORMAL)")
        eval("MainWindow.player_" + str(currentPlayer[0]) + "_label_2.delete(0, END)")
        eval("MainWindow.player_" + str(currentPlayer[0]) + "_label_2.config(state=DISABLED)")
        MainWindow.button_commitScore.configure(state=DISABLED)
    return
