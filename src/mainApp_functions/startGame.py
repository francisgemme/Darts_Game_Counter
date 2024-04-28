from tkinter import *


def startGame(mainApp):
    if ~mainApp.match_inst.gameStarted:
        mainApp.button_gameStart.configure(state=DISABLED, disabledforeground=mainApp.Button_bg_color)
        mainApp.button_gameStart.destroy()
        mainApp.frame9.destroy()

        mainApp.button_addPlayer.configure(state=DISABLED)
        mainApp.button_gameMode.config(state=DISABLED)

        if mainApp.match_inst.getNplayer() != 0:  # probably a useless check...
            if mainApp.match_inst.getNplayer() == 1:
                if mainApp.match_inst.doubleInMode == False:
                    mainApp.player_1_label_2.config(state=DISABLED, disabledforeground="yellow")

            if mainApp.match_inst.getNplayer() == 2:
                if mainApp.match_inst.doubleInMode == False:
                    mainApp.player_2_label_2.config(state=DISABLED, disabledforeground="yellow")
                    mainApp.player_1_label_2.config(state=DISABLED, disabledforeground="yellow")

            if mainApp.match_inst.getNplayer() == 3:
                if mainApp.match_inst.doubleInMode == False:
                    mainApp.player_3_label_2.config(state=DISABLED, disabledforeground="yellow")
                    mainApp.player_2_label_2.config(state=DISABLED, disabledforeground="yellow")
                    mainApp.player_1_label_2.config(state=DISABLED, disabledforeground="yellow")

            if mainApp.match_inst.getNplayer() == 4:
                if mainApp.match_inst.doubleInMode == False:
                    mainApp.player_4_label_2.config(state=DISABLED, disabledforeground="yellow")
                    mainApp.player_3_label_2.config(state=DISABLED, disabledforeground="yellow")
                    mainApp.player_2_label_2.config(state=DISABLED, disabledforeground="yellow")
                    mainApp.player_1_label_2.config(state=DISABLED, disabledforeground="yellow")

    if mainApp.match_inst.doubleInMode == True:
        mainApp.player_1_checkbox.config(state=NORMAL) # Activate the Double In box

    mainApp.match_inst.playerIndex = [1, mainApp.match_inst.getNplayer()]
    mainApp.updateIndexLog()

    mainApp.match_inst.gameStarted = True
    mainApp.match_inst.currentGameTurn = 1

    mainApp.button_editScore.configure(state='normal')
    mainApp.button_editName.configure(state='normal')
    mainApp.button_endTurn.configure(state='normal')
    mainApp.refreshImages()
    mainApp.updateStatusLabel("La Partie est commencée!")

    return
