from tkinter import *


def startGame(mainApp):
    if ~mainApp.gameStarted:
        mainApp.button_gameStart.configure(state=DISABLED, disabledforeground=mainApp.Button_bg_color)
        mainApp.button_gameStart.destroy()
        mainApp.frame9.destroy()

        mainApp.button_addPlayer.configure(state=DISABLED)
        mainApp.button_gameMode.config(state=DISABLED)

        if mainApp.nbPlayer != 0:  # probably a useless check...
            if mainApp.nbPlayer == 1:
                if mainApp.DoubleInMode == False:
                    mainApp.player_1_label_2.config(state=DISABLED, disabledforeground="yellow")

            if mainApp.nbPlayer == 2:
                if mainApp.DoubleInMode == False:
                    mainApp.player_2_label_2.config(state=DISABLED, disabledforeground="yellow")
                    mainApp.player_1_label_2.config(state=DISABLED, disabledforeground="yellow")

            if mainApp.nbPlayer == 3:
                if mainApp.DoubleInMode == False:
                    mainApp.player_3_label_2.config(state=DISABLED, disabledforeground="yellow")
                    mainApp.player_2_label_2.config(state=DISABLED, disabledforeground="yellow")
                    mainApp.player_1_label_2.config(state=DISABLED, disabledforeground="yellow")

            if mainApp.nbPlayer == 4:
                if mainApp.DoubleInMode == False:
                    mainApp.player_4_label_2.config(state=DISABLED, disabledforeground="yellow")
                    mainApp.player_3_label_2.config(state=DISABLED, disabledforeground="yellow")
                    mainApp.player_2_label_2.config(state=DISABLED, disabledforeground="yellow")
                    mainApp.player_1_label_2.config(state=DISABLED, disabledforeground="yellow")

    if mainApp.DoubleInMode == True:
        mainApp.player_1_checkbox.config(state=NORMAL) # Activate the Double In box

    mainApp.playerIndex = [1, mainApp.nbPlayer]
    mainApp.updateIndexLog()
    mainApp.gameStarted = True
    mainApp.currentGameTurn = 1
    mainApp.button_editScore.configure(state='normal')
    mainApp.button_editName.configure(state='normal')
    mainApp.button_endTurn.configure(state='normal')
    mainApp.refreshImages()
    mainApp.updateStatusLabel("La Partie est commencée!")

    return
