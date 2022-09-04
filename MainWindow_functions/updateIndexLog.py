import numpy as np
import pandas as pd
import os


def updateIndexLog(MainWindow):
    if MainWindow.gameStarted == False:  # If the game is not started, create the IndexLog with all added players
        # get Current Player turn over the total nb of player
        totalPlayer = MainWindow.playerIndex[1:]
        MainWindow.turnIndexLog = pd.DataFrame([[0, 0, 1]], columns=['index', 'gameTurn', 'playerTurn']) # first default columns

        for i in range(totalPlayer[0]): # add all columns needed for the match
            CommittedScoreToLog = eval("int(MainWindow.player_"+str(i+1)+"_label_2.get())")
            eval("MainWindow.turnIndexLog.insert(len(MainWindow.turnIndexLog.columns), 'P_"+str(i+1)+"_Entry', 0)")
            eval("MainWindow.turnIndexLog.insert(len(MainWindow.turnIndexLog.columns), 'P_"+str(i+1)+"_Score', CommittedScoreToLog)")
            if MainWindow.DoubleInMode == True:
                eval("MainWindow.turnIndexLog.insert(len(MainWindow.turnIndexLog.columns), 'P_"+str(i+1)+"_DoubleIn', 0)")

    # If the game is started, add the committed score (and more) to the current player
    if MainWindow.gameStarted:
        MainWindow.logIndex += 1 # Any index event increase
        currentIndex = MainWindow.logIndex # Any event is logged
        currentGameTurn = MainWindow.currentGameTurn # What is the game turn
        lastGameTurn = MainWindow.turnIndexLog['gameTurn'].iloc[-1] # Get previous game turn

        totalPlayer = MainWindow.playerIndex[1:]
        currentPlayer = MainWindow.playerIndex[:1]

        CommittedScoreToLog = eval("int(MainWindow.player_"+str(currentPlayer[0])+"_label_2.get())")

        lastPlayerTurn = MainWindow.turnIndexLog['playerTurn'].iloc[-1]
        if currentPlayer == lastPlayerTurn: # On this player turn, something happened (score or DoubleIn)
            # This allow multiple entries for each turns. The log will diplay all entries for a specific game turn
            if lastGameTurn == currentGameTurn:
                if MainWindow.turnIndexLog["P_" + str(currentPlayer[0]) + "_Entry"].iloc[-1] != "|":
                    player_entry = MainWindow.turnIndexLog["P_" + str(currentPlayer[0]) + "_Entry"].iloc[-1] + 1

                else:
                    player_entry = 1
            elif lastGameTurn != currentGameTurn:
                player_entry = 1

        elif currentPlayer != lastPlayerTurn:  # This block will log the EndTurn event by adding a line.
            player_entry = "|"
            CommittedScoreToLog = "|"
            DoubleInStatus = "|"

        if MainWindow.DoubleInMode == True:
            if currentPlayer == lastPlayerTurn:
                DoubleInStatus = eval("MainWindow.p"+str(currentPlayer[0])+"_DoubleInVar.get()")
            toAppend = eval("pd.DataFrame([[currentIndex, currentGameTurn, currentPlayer[0], player_entry, CommittedScoreToLog, DoubleInStatus]], "
                            "columns=['index', 'gameTurn', 'playerTurn', 'P_"+str(currentPlayer[0])+"_Entry', 'P_"+str(currentPlayer[0])+"_Score','P_"+str(currentPlayer[0])+"_DoubleIn'])")
        else:
            toAppend = eval("pd.DataFrame([[currentIndex, currentGameTurn, currentPlayer[0], player_entry, CommittedScoreToLog]], "
                            "columns=['index', 'gameTurn', 'playerTurn', 'P_"+str(currentPlayer[0])+"_Entry', 'P_"+str(currentPlayer[0])+"_Score'])")

        MainWindow.turnIndexLog = pd.concat([MainWindow.turnIndexLog, toAppend])
        MainWindow.turnIndexLog = MainWindow.turnIndexLog.replace(np.nan, "|")

        os.system('cls' if os.name == 'nt' else 'clear')
        print(MainWindow.turnIndexLog)


        return
