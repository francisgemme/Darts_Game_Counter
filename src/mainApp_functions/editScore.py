from tkinter import *

def editScore(mainApp):
    if mainApp.gameStarted:
        currentPlayer = mainApp.playerIndex[:1]  # Who is playing

        if mainApp.editScoreMode == False:
            mainApp.button_editScore.config(fg=mainApp.activeButton_ft_color, bg=mainApp.activeButton_bg_color, relief=SUNKEN)
            mainApp.input_Score.config(state=NORMAL)
            mainApp.input_Score.delete(0, END)
            mainApp.input_Score.config(state=DISABLED)
            mainApp.button_commitScore.configure(state=DISABLED)
            mainApp.input_Score.config(disabledbackground=mainApp.Button_bg_color)
            eval("mainApp.player_" + str(currentPlayer[0]) + "_label_2.config(disabledbackground='black')")
            mainApp.button_endTurn.configure(state='disabled')

            if mainApp.match_inst.doubleInMode == True:
                eval("mainApp.player_"+str(currentPlayer[0])+"_checkbox.configure(state='disabled')")


            mainApp.editScoreMode = True

        elif mainApp.editScoreMode == True:
            mainApp.button_editScore.config(fg=mainApp.Button_ft_color, bg=mainApp.Button_bg_color, relief=RAISED)
            mainApp.input_Score.config(disabledbackground='black')
            eval("mainApp.player_" + str(currentPlayer[0]) + "_label_2.config(disabledbackground=mainApp.Button_bg_color)")
            mainApp.button_endTurn.configure(state='normal')

            if mainApp.match_inst.doubleInMode == True:
                DoubleInStatus = eval("mainApp.p"+str(currentPlayer[0])+"_DoubleInVar.get()")
                if DoubleInStatus == False:
                    eval("mainApp.player_"+str(currentPlayer[0])+"_checkbox.configure(state='normal')")

            mainApp.editScoreMode = False
    return
