from tkinter import *

def writeCommitScore(mainApp):
    # get Current Player turn over the total nb of player
    scoreToInput = mainApp.input_Score.get()
    if scoreToInput != '':
        scoreToInput = int(mainApp.input_Score.get())
        currentPlayer = mainApp.playerIndex[:1]
        mainApp.input_Score.config(state=NORMAL)
        mainApp.input_Score.delete(0, END)
        mainApp.input_Score.config(state=DISABLED)

        currentPlayerScore = eval("mainApp.player_" + str(currentPlayer[0]) +"_label_2.get()", {"mainApp": mainApp})

        if int(currentPlayerScore) >= int(scoreToInput):
            eval("mainApp.player_"+str(currentPlayer[0])+"_label_2.config(state=NORMAL)")
            eval("mainApp.player_"+str(currentPlayer[0])+"_label_2.delete(0, END)")
            eval("mainApp.player_"+str(currentPlayer[0])+"_label_2.insert(0, str(int(currentPlayerScore) - scoreToInput))")
            eval("mainApp.player_"+str(currentPlayer[0])+"_label_2.config(state=DISABLED)")

        mainApp.button_commitScore.configure(state=DISABLED)
    return
