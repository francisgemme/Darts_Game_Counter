from tkinter import *

def editScore(MainWindow):
    if MainWindow.gameStarted:
        currentPlayer = MainWindow.playerIndex[:1]  # Who is playing

        if MainWindow.editScoreMode == False:
            MainWindow.button_editScore.config(fg=MainWindow.activeButton_ft_color, bg=MainWindow.activeButton_bg_color, relief=SUNKEN)
            MainWindow.input_Score.config(state=NORMAL)
            MainWindow.input_Score.delete(0, END)
            MainWindow.input_Score.config(state=DISABLED)
            MainWindow.button_commitScore.configure(state=DISABLED)
            MainWindow.input_Score.config(disabledbackground=MainWindow.Button_bg_color)
            eval("MainWindow.player_" + str(currentPlayer[0]) + "_label_2.config(disabledbackground='black')")
            MainWindow.editScoreMode = True

        elif MainWindow.editScoreMode == True:
            MainWindow.button_editScore.config(fg=MainWindow.Button_ft_color, bg=MainWindow.Button_bg_color, relief=RAISED)
            MainWindow.input_Score.config(disabledbackground='black')
            eval("MainWindow.player_" + str(currentPlayer[0]) + "_label_2.config(disabledbackground=MainWindow.Button_bg_color)")
            MainWindow.editScoreMode = False
    return
