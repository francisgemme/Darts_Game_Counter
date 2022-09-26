import numpy as np
import pandas as pd
import os

# The LOG function initializes a log and records all actions that occurred during the game.
# Actions such as : EndTurn, Commit Score.

# The recorded information is use for downstream functions such as calculating the player Average, High score, and more.
# This log records also serve as the dataset for the undo/redo functions.

def updateIndexLog(MainWindow):

    #-------------------------------------------------------------------------------------------------------------------
    #                                               INITIALIZING THE LOG
    #-------------------------------------------------------------------------------------------------------------------
    # If the game is not started, create the IndexLog with all added players
        # get Current Player turn over the total nb of player.

    if MainWindow.gameStarted == False:  # if the game is not started
        totalPlayer = MainWindow.playerIndex[1:] #get number of players
        MainWindow.turnIndexLog = pd.DataFrame([[0, 0, 1]], columns=['index', 'gameTurn', 'playerTurn']) # create first default columns

        for i in range(totalPlayer[0]): # add all columns needed for the match

            CommittedScoreToLog = eval("int(MainWindow.player_"+str(i+1)+"_label_2.get())") # Read the initial score in the GUI
            eval("MainWindow.turnIndexLog.insert(len(MainWindow.turnIndexLog.columns), 'P_"+str(i+1)+"_Entry', 0)")
            eval("MainWindow.turnIndexLog.insert(len(MainWindow.turnIndexLog.columns), 'P_"+str(i+1)+"_Score', CommittedScoreToLog)")
            if MainWindow.DoubleInMode == True: # if this mode is on, add column for each player
                eval("MainWindow.turnIndexLog.insert(len(MainWindow.turnIndexLog.columns), 'P_"+str(i+1)+"_DoubleIn', 0)")

    #-------------------------------------------------------------------------------------------------------------------
    #                                                  UPDATE THE LOG
    #-------------------------------------------------------------------------------------------------------------------
    # If the game is started, add the committed score, record the endturn for the current player
    if MainWindow.gameStarted: #if the game is started

        # DO A BUNCH OF CHECKS AND CHANGES ON VARIABLES DEPENDING OF THE SITUATION

        # Extract information that is needed before logging
        MainWindow.logIndex += 1 # The log index event increase. (refer to initializeGUIvar for parameters)
        currentIndex = MainWindow.logIndex # Any event is logged

        # Store who is playing out of the total
        totalPlayer = MainWindow.playerIndex[1:]
        currentPlayer = MainWindow.playerIndex[:1]

        # Get the current and previous game turn. If there are the same, the player entry will be affected.
        currentGameTurn = MainWindow.currentGameTurn # What is the game turn
        lastGameTurn = MainWindow.turnIndexLog['gameTurn'].iloc[-1] # Get previous game turn

        #----------------------------------------------------------------------------------------------------------
        # This loop looks for the last logged score. It looks back until it finds a score. If it finds a PIPE, it continues.
        PIPE = True  #Generate the PIPE variable bolean
        PIPE_count = 1 #Count to go to the next (previous) row in the column.

        while PIPE == True: # Start the search

            # Get the previous score
            lastPlayerScoreTurn = eval("MainWindow.turnIndexLog['P_"+str(currentPlayer[0])+"_Score'].iloc[-"+str(PIPE_count)+"]")# Get previous game turn
            if lastPlayerScoreTurn == "|":
                PIPE_count += 1 # add one and restart
            elif lastPlayerScoreTurn != "|": # if not
                PIPE = False # Set to false, loop is over...

        # Extract the score that just got commited (after commit score button was pressed)
        CommittedScoreToLog = eval("(MainWindow.player_"+str(currentPlayer[0])+"_label_2.get())")


        # If the score is the same as the previous, overwrite the variable with "|". This is to ease the statistical functions.
        # The idea is to only keep score changes. Note that the EndTurn symbol is "|".
        # Which won't be counted during statistical calculations
        if CommittedScoreToLog == lastPlayerScoreTurn:
            CommittedScoreToLog = "|" # Will log this symbol if the score remained as-is.
        #----------------------------------------------------------------------------------------------------------

        # The below code deals with the player entries. This allows the player to add its score for each darts.
        # If this is still is turn, the player_entry gets incremented.

        lastPlayerTurn = MainWindow.turnIndexLog['playerTurn'].iloc[-1]
        if currentPlayer == lastPlayerTurn: # On this player turn, something happened (score or DoubleIn)
            # This allows multiple entries for each turn. The log will display all entries for a specific game turn
            if lastGameTurn == currentGameTurn: # During this turn
                if MainWindow.turnIndexLog["P_" + str(currentPlayer[0]) + "_Entry"].iloc[-1] != "|":
                    player_entry = MainWindow.turnIndexLog["P_" + str(currentPlayer[0]) + "_Entry"].iloc[-1] + 1
                    # increment the player entry number
                else:
                    player_entry = 1
            elif lastGameTurn != currentGameTurn: # Not the same game turn. This is the first entry
                player_entry = 1

        # THe below code records tht the End-Turn button was pressed.
        elif currentPlayer != lastPlayerTurn:  # Below will log the EndTurn event by adding a PIPE .
            player_entry = "|"
            CommittedScoreToLog = "|"
            if MainWindow.DoubleInMode == True:
                DoubleInStatus = "|"
                print(type(DoubleInStatus))

        #---------------------------------------------------------------------------------------------------------------
        #                                 LOG THE DATA AND PRINT IN THE CONSOLE
        #---------------------------------------------------------------------------------------------------------------
        # Log and Deal with the DoubleIn mode
        if MainWindow.DoubleInMode == True:
            if currentPlayer == lastPlayerTurn:
                DoubleInStatus = eval("MainWindow.p"+str(currentPlayer[0])+"_DoubleInVar.get()")
            # Will log the line with the double-in status
            toAppend = eval("pd.DataFrame([[currentIndex, currentGameTurn, currentPlayer[0], player_entry, CommittedScoreToLog, DoubleInStatus]], "
                            "columns=['index', 'gameTurn', 'playerTurn', 'P_"+str(currentPlayer[0])+"_Entry', 'P_"+str(currentPlayer[0])+"_Score','P_"+str(currentPlayer[0])+"_DoubleIn'])")
        else: # If double-in is off
            toAppend = eval("pd.DataFrame([[currentIndex, currentGameTurn, currentPlayer[0], player_entry, CommittedScoreToLog]], "
                            "columns=['index', 'gameTurn', 'playerTurn', 'P_"+str(currentPlayer[0])+"_Entry', 'P_"+str(currentPlayer[0])+"_Score'])")

        MainWindow.turnIndexLog = pd.concat([MainWindow.turnIndexLog, toAppend])
        MainWindow.turnIndexLog = MainWindow.turnIndexLog.replace(np.nan, "|")

        os.system('cls' if os.name == 'nt' else 'clear')
        print(MainWindow.turnIndexLog)

        return
