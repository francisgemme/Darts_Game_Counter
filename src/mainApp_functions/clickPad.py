from tkinter import *

def clickPad(mainApp, number):

    if mainApp.match_inst.gameStarted == True:
        currentPlayer = mainApp.match_inst.playerIndex[:1]  # Who is playing

        if mainApp.match_inst.doubleInMode == True:
            DoubleInStatus = eval("mainApp.p"+str(currentPlayer[0])+"_DoubleInVar.get()")
        else:
            DoubleInStatus = False

        if DoubleInStatus == True or mainApp.match_inst.doubleInMode == False:
            current = mainApp.input_Score.get()
            if number == -1:
                mainApp.input_Score.config(state='normal')
                mainApp.input_Score.delete(len(current)-1, len(current))
                mainApp.input_Score.config(state=DISABLED)
                return

            if mainApp.match_inst.editScoreMode == False:
                if len(current) < 3:
                    mainApp.input_Score.config(state='normal')
                    mainApp.input_Score.delete(0, END)
                    mainApp.input_Score.insert(0, str(current) + str(number))
                    mainApp.input_Score.config(state=DISABLED)

                # Will change the state of the button depending of what is now inside
                newCurrent = mainApp.input_Score.get()
                if len(newCurrent) > 0:
                    mainApp.button_commitScore.configure(state='normal')
                if len(newCurrent) < 0:
                    mainApp.button_commitScore.configure(state=DISABLED)


            if mainApp.match_inst.editScoreMode == True:
                currentPlayer = mainApp.match_inst.playerIndex[:1]  # Who is playing
                currentScore = eval("mainApp.player_" + str(currentPlayer[0]) + "_label_2.get()", {"mainApp": mainApp})
                if len(currentScore) < 3:
                    eval("mainApp.player_" + str(currentPlayer[0]) + "_label_2.config(state='normal')")
                    eval("mainApp.player_" + str(currentPlayer[0]) + "_label_2.delete(0, END)")
                    eval("mainApp.player_" + str(currentPlayer[0]) + "_label_2.insert(0, str(currentScore) + str(number))")
                    eval("mainApp.player_" + str(currentPlayer[0]) + "_label_2.config(state=DISABLED)")
                    newCurrentScore = eval("mainApp.player_" + str(currentPlayer[0]) + "_label_2.get()", {"mainApp": mainApp})

                    # Will change the state of the button depending of what is now inside
                    if len(newCurrentScore) > 0:
                        mainApp.button_commitScore.configure(state=NORMAL)
                    elif len(newCurrentScore) <= 0:
                        mainApp.button_commitScore.configure(state=DISABLED)
        return
