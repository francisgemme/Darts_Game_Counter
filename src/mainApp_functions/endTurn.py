from tkinter import *

def endTurn(mainApp):
    if mainApp.gameStarted == True:

        print(mainApp.playerIndex)
        mainApp.button_endTurn.configure(state=DISABLED) #De-activate button for safety

        # get Current Player turn over the total nb of player
        currentPlayer = mainApp.playerIndex[:1]  # Who is playing
        totalPlayer = mainApp.playerIndex[1:] # Total number of players

        if currentPlayer < totalPlayer:
            if currentPlayer == [1]: # if player #1 turn
                mainApp.playerIndex[0] = 2
                if mainApp.match_inst.doubleInMode == True:
                    mainApp.player_1_checkbox.config(state=DISABLED)
                    if mainApp.p1_DoubleInVar.get() == True:
                        mainApp.player_1_checkbox.config(state=DISABLED)
                    if mainApp.p2_DoubleInVar.get() == False:
                        mainApp.player_2_checkbox.config(state=NORMAL)

            if currentPlayer == [2]:
                mainApp.playerIndex[0] = 3
                if mainApp.match_inst.doubleInMode == True:
                    mainApp.player_2_checkbox.config(state=DISABLED)
                    if mainApp.p2_DoubleInVar.get() == True:
                        mainApp.player_2_checkbox.config(state=DISABLED)
                    if mainApp.p3_DoubleInVar.get()== False:
                        mainApp.player_3_checkbox.config(state=NORMAL)

            if currentPlayer == [3]:
                mainApp.playerIndex[0] = 4
                if mainApp.match_inst.doubleInMode == True:
                    mainApp.player_3_checkbox.config(state=DISABLED)
                    if mainApp.p3_DoubleInVar.get() == True:
                        mainApp.player_3_checkbox.config(state=DISABLED)
                    if mainApp.p4_DoubleInVar.get()== False:
                        mainApp.player_4_checkbox.config(state=NORMAL)

        if currentPlayer == totalPlayer:
            mainApp.playerIndex[0] = 1
            if mainApp.match_inst.doubleInMode == True:
                eval("mainApp.player_"+str(currentPlayer[0])+"_checkbox.config(state=DISABLED)")
                if eval("mainApp.p"+str(currentPlayer[0])+"_DoubleInVar.get()") == True:
                    eval("mainApp.player_"+str(currentPlayer[0])+"_checkbox.config(state=DISABLED)")
                if mainApp.p1_DoubleInVar.get() == False:
                    mainApp.player_1_checkbox.config(state=NORMAL)
            
            #if this is the last player to play, the log "game turn" is updated by 1  **To be removed...
            mainApp.currentGameTurn += 1

        mainApp.arrowImage.grid_forget()
        mainApp.button_endTurn.configure(state='normal')
        mainApp.updateIndexLog()
        mainApp.refreshImages()

    return