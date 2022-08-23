import numpy as np
import pandas as pd


def updateIndexLog(MainWindow):
    if MainWindow.gameStarted == False:  # If the game is not started, create the IndexLog with all added players
        # get Current Player turn over the total nb of player
        totalPlayer = MainWindow.playerIndex[1:]
        MainWindow.turnIndexLog = pd.DataFrame([[0, 0]], columns=['index', 'gameTurn']) # first default columns

        for i in range(totalPlayer[0]): # add all columns needed for the match
            eval("MainWindow.turnIndexLog.insert(len(MainWindow.turnIndexLog.columns), 'P_"+str(i+1)+"_Entry', 0)")
            eval("MainWindow.turnIndexLog.insert(len(MainWindow.turnIndexLog.columns), 'P_"+str(i+1)+"_Score', 501)")
            if MainWindow.doubleInMode:
                eval("MainWindow.turnIndexLog.insert(len(MainWindow.turnIndexLog.columns), 'P_"+str(i+1)+"_DoubleIn', 0)")

    # If the game is started, add the committed score (and more) to the current player
    if MainWindow.gameStarted:
        MainWindow.logIndex += 1
        currentIndex = MainWindow.logIndex
        currentGameTurn = MainWindow.currentGameTurn
        lastGameTurn = MainWindow.turnIndexLog['gameTurn'].iloc[-1]

        totalPlayer = MainWindow.playerIndex[1:]
        currentPlayer = MainWindow.playerIndex[:1]

        # This allow multiple entries for each turns. The log will diplay all entries for a specific game turn
        if lastGameTurn == currentGameTurn:
            if MainWindow.turnIndexLog["P_" + str(currentPlayer[0]) + "_Entry"].iloc[-1] != "|":
                player_entry = MainWindow.turnIndexLog["P_" + str(currentPlayer[0]) + "_Entry"].iloc[-1] + 1
            else:
                player_entry = 1
        elif lastGameTurn != currentGameTurn:
            player_entry = 1

        CommitedScoreToLog = eval("int(MainWindow.player_"+str(currentPlayer[0])+"_label_2.get())")
        toAppend = eval("pd.DataFrame([[currentIndex, currentGameTurn, player_entry, CommitedScoreToLog]], "
                        "columns=['index', 'gameTurn', 'P_"+str(currentPlayer[0])+"_Entry', 'P_"+str(currentPlayer[0])+"_Score'])")
        MainWindow.turnIndexLog = pd.concat([MainWindow.turnIndexLog, toAppend])

        MainWindow.turnIndexLog = MainWindow.turnIndexLog.replace(np.nan, "|")

        print(MainWindow.turnIndexLog)


        return
