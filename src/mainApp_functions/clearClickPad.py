from tkinter import *

def clearClickPad(mainApp):
    # A class "Game" with its properties must be sent to this function
    # Transfer created player to the Lobby
    currentPlayer = mainApp.match_inst.playerIndex[:1]  # Who is playing

    if mainApp.match_inst.doubleInMode == True:
        DoubleInStatus = eval("mainApp.p"+str(currentPlayer[0])+"_DoubleInVar.get()")
    else:
        DoubleInStatus = False

    if DoubleInStatus == True or mainApp.match_inst.doubleInMode == False:
        if mainApp.match_inst.editScoreMode == False:
            mainApp.input_Score.config(state=NORMAL)
            mainApp.input_Score.delete(0, END)
            mainApp.input_Score.config(state=DISABLED)
            mainApp.button_commitScore.configure(state=DISABLED)  # Clearing is also disabling the commit score button

        if mainApp.match_inst.editScoreMode == True:
            eval("mainApp.player_" + str(currentPlayer[0]) + "_label_2.config(state=NORMAL)")
            eval("mainApp.player_" + str(currentPlayer[0]) + "_label_2.delete(0, END)")
            eval("mainApp.player_" + str(currentPlayer[0]) + "_label_2.config(state=DISABLED)")

        mainApp.button_commitScore.configure(state=DISABLED)
    return
