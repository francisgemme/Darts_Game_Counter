from tkinter import *

def endTurn(MainWindow):
    if MainWindow.gameStarted == True:

        print(MainWindow.playerIndex)
        MainWindow.button_endTurn.configure(state=DISABLED) #De-activate button for safety

        # get Current Player turn over the total nb of player
        currentPlayer = MainWindow.playerIndex[:1]  # Who is playing
        totalPlayer = MainWindow.playerIndex[1:] # Total number of players

        if currentPlayer < totalPlayer:
            if currentPlayer == [1]: # if player #1 turn
                MainWindow.playerIndex[0] = 2
                if MainWindow.DoubleInMode == True:
                    MainWindow.player_1_checkbox.config(state=DISABLED)
                    if MainWindow.p1_DoubleInVar.get() == True:
                        MainWindow.player_1_checkbox.config(state=DISABLED)
                    if MainWindow.p2_DoubleInVar.get() == False:
                        MainWindow.player_2_checkbox.config(state=NORMAL)
            if currentPlayer == [2]:
                MainWindow.playerIndex[0] = 3
                if MainWindow.DoubleInMode == True:
                    MainWindow.player_2_checkbox.config(state=DISABLED)
                    if MainWindow.p2_DoubleInVar.get() == True:
                        MainWindow.player_2_checkbox.config(state=DISABLED)
                    if MainWindow.p3_DoubleInVar.get()== False:
                        MainWindow.player_3_checkbox.config(state=NORMAL)
            if currentPlayer == [3]:
                MainWindow.playerIndex[0] = 4
                if MainWindow.DoubleInMode == True:
                    MainWindow.player_3_checkbox.config(state=DISABLED)
                    if MainWindow.p3_DoubleInVar.get() == True:
                        MainWindow.player_3_checkbox.config(state=DISABLED)
                    if MainWindow.p4_DoubleInVar.get()== False:
                        MainWindow.player_4_checkbox.config(state=NORMAL)

        if currentPlayer == totalPlayer:
            MainWindow.playerIndex[0] = 1
            if MainWindow.DoubleInMode == True:
                eval("MainWindow.player_"+str(currentPlayer[0])+"_checkbox.config(state=DISABLED)")
                if eval("MainWindow.p"+str(currentPlayer[0])+"_DoubleInVar.get()") == True:
                    eval("MainWindow.player_"+str(currentPlayer[0])+"_checkbox.config(state=DISABLED)")
                if MainWindow.p1_DoubleInVar.get() == False:
                    MainWindow.player_1_checkbox.config(state=NORMAL)
            #if this is the last player to play, the log "game turn" is updated by 1  **To be removed...
            MainWindow.currentGameTurn += 1

        MainWindow.arrowImage.grid_forget()
        MainWindow.button_endTurn.configure(state='normal')
        MainWindow.updateIndexLog()
        MainWindow.refreshImages()

    return
