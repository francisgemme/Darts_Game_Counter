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
            if currentPlayer == [2]:
                MainWindow.playerIndex[0] = 3
            if currentPlayer == [3]:
                MainWindow.playerIndex[0] = 4
            if currentPlayer == [4]:
                MainWindow.playerIndex[0] = 1

        if currentPlayer == totalPlayer:
            MainWindow.playerIndex[0] = 1
            #if this is the last player to play, the log "game turn" is updated by 1  **To be removed...

        if currentPlayer == totalPlayer:
            MainWindow.currentGameTurn += 1
            #toAppend = pd.DataFrame([[currentGameTurn]], columns=['gameTurn'])
            #self.turnIndexLog = pd.concat([self.turnIndexLog, toAppend])

        MainWindow.arrowImage.grid_forget()
        MainWindow.button_endTurn.configure(state='normal')
        MainWindow.refreshImages()

    return
