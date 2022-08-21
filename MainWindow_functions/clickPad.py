from tkinter import *

def clickPad(MainWindow, number):

    if MainWindow.gameStarted == True:

        if MainWindow.editScoreMode == False:
            current = MainWindow.input_Score.get()
            if len(current) < 3:
                MainWindow.input_Score.config(state='normal')
                MainWindow.input_Score.delete(0, END)
                MainWindow.input_Score.insert(0, str(current) + str(number))
                MainWindow.input_Score.config(state=DISABLED)

            # Will change the state of the button depending of what is now inside
            newCurrent = MainWindow.input_Score.get()
            if len(newCurrent) > 0:
                MainWindow.button_commitScore.configure(state='normal')
            if len(newCurrent) < 0:
                MainWindow.button_commitScore.configure(state=DISABLED)

        if MainWindow.editScoreMode == True:
            currentPlayer = MainWindow.playerIndex[:1]  # Who is playing
            currentScore = eval("MainWindow.player_" + str(currentPlayer[0]) + "_label_2.get()", {"MainWindow": MainWindow})
            if len(currentScore) < 3:
                eval("MainWindow.player_" + str(currentPlayer[0]) + "_label_2.config(state='normal')")
                eval("MainWindow.player_" + str(currentPlayer[0]) + "_label_2.delete(0, END)")
                eval("MainWindow.player_" + str(currentPlayer[0]) + "_label_2.insert(0, str(currentScore) + str(number))")
                eval("MainWindow.player_" + str(currentPlayer[0]) + "_label_2.config(state=DISABLED)")
                newCurrentScore = eval("MainWindow.player_" + str(currentPlayer[0]) + "_label_2.get()", {"MainWindow": MainWindow})

                # Will change the state of the button depending of what is now inside
                if len(newCurrentScore) > 0:
                    MainWindow.button_commitScore.configure(state=NORMAL)
                elif len(newCurrentScore) <= 0:
                    MainWindow.button_commitScore.configure(state=DISABLED)
        return
