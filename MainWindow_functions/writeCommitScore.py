from tkinter import *

def writeCommitScore(MainWindow):
    # get Current Player turn over the total nb of player
    scoreToInput = MainWindow.input_Score.get()
    if scoreToInput != '':
        scoreToInput = int(MainWindow.input_Score.get())
        currentPlayer = MainWindow.playerIndex[:1]
        MainWindow.input_Score.config(state=NORMAL)
        MainWindow.input_Score.delete(0, END)
        MainWindow.input_Score.config(state=DISABLED)

        currentPlayerScore = eval("MainWindow.player_" + str(currentPlayer[0]) +"_label_2.get()", {"MainWindow": MainWindow})

        if int(currentPlayerScore) >= int(scoreToInput):
            eval("MainWindow.player_"+str(currentPlayer[0])+"_label_2.config(state=NORMAL)")
            eval("MainWindow.player_"+str(currentPlayer[0])+"_label_2.delete(0, END)")
            eval("MainWindow.player_"+str(currentPlayer[0])+"_label_2.insert(0, str(int(currentPlayerScore) - scoreToInput))")
            eval("MainWindow.player_"+str(currentPlayer[0])+"_label_2.config(state=DISABLED)")

        MainWindow.button_commitScore.configure(state=DISABLED)
    return
