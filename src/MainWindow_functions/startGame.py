from tkinter import *


def startGame(MainWindow):
    if ~MainWindow.gameStarted:
        MainWindow.button_gameStart.configure(state=DISABLED, disabledforeground=MainWindow.Button_bg_color)
        MainWindow.button_gameStart.destroy()
        MainWindow.frame9.destroy()

        MainWindow.button_addPlayer.configure(state=DISABLED)
        MainWindow.button_gameMode.config(state=DISABLED)

        if MainWindow.nbPlayer != 0:  # probably a useless check...
            if MainWindow.nbPlayer == 1:
                if MainWindow.DoubleInMode == False:
                    MainWindow.player_1_label_2.config(state=DISABLED, disabledforeground="yellow")

            if MainWindow.nbPlayer == 2:
                if MainWindow.DoubleInMode == False:
                    MainWindow.player_2_label_2.config(state=DISABLED, disabledforeground="yellow")
                    MainWindow.player_1_label_2.config(state=DISABLED, disabledforeground="yellow")

            if MainWindow.nbPlayer == 3:
                if MainWindow.DoubleInMode == False:
                    MainWindow.player_3_label_2.config(state=DISABLED, disabledforeground="yellow")
                    MainWindow.player_2_label_2.config(state=DISABLED, disabledforeground="yellow")
                    MainWindow.player_1_label_2.config(state=DISABLED, disabledforeground="yellow")

            if MainWindow.nbPlayer == 4:
                if MainWindow.DoubleInMode == False:
                    MainWindow.player_4_label_2.config(state=DISABLED, disabledforeground="yellow")
                    MainWindow.player_3_label_2.config(state=DISABLED, disabledforeground="yellow")
                    MainWindow.player_2_label_2.config(state=DISABLED, disabledforeground="yellow")
                    MainWindow.player_1_label_2.config(state=DISABLED, disabledforeground="yellow")

    if MainWindow.DoubleInMode == True:
        MainWindow.player_1_checkbox.config(state=NORMAL) # Activate the Double In box

    MainWindow.playerIndex = [1, MainWindow.nbPlayer]
    MainWindow.updateIndexLog()
    MainWindow.gameStarted = True
    MainWindow.currentGameTurn = 1
    MainWindow.button_editScore.configure(state='normal')
    MainWindow.button_editName.configure(state='normal')
    MainWindow.button_endTurn.configure(state='normal')
    MainWindow.refreshImages()
    MainWindow.updateStatusLabel("La Partie est commencée!")

    return
