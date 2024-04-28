# import all Class methods as aliases, from the mainApps_functions directory;

class __init__:
    """
    Class representing the main window attributes.

    Attributes:
        nbPlayer (int): Number of players.
        p1_DoubleInVar (bool): Player 1 Double In variable.
        p2_DoubleInVar (bool): Player 2 Double In variable.
        p3_DoubleInVar (bool): Player 3 Double In variable.
        p4_DoubleInVar (bool): Player 4 Double In variable.
        SelectedGameMode (list): Selected Game Mode.
        prevSelMode (int): Previous Selected Mode.
        doubleInMode (bool): Double In Mode.
        doubleOutMode (bool): Double Out Mode.
        CommitGameMode (list): Game Mode to commit.
        gameStarted (bool): Indicates if the game has started.
        playerIndex (list): Player turn index and total number of players.
        turnIndexLog (list): Turn index log.
        editScoreMode (bool): Edit Score Mode.
        editNameMode (bool): Edit Name Mode.
        currentGameTurn (int): Current game turn.
        logIndex (int): Log index.
        doubleInMode (bool): Double In Mode.
        quitbuttonPressed (bool): Indicates if the quit button has been pressed.
    """

    # Declare variables & types
    nbPlayer = int(0)
    players = []

    #Used to be stored in the GUI, must be located in the player object
    p1_DoubleInVar = bool(False)
    p2_DoubleInVar = bool(False)
    p3_DoubleInVar = bool(False)
    p4_DoubleInVar = bool(False)

    SelectedGameMode = []
    prevSelGameMode = 1 # to initiate the GUI with the current mode
    prevSelDoubleInMode = bool(True) # to initiate the GUI with the current mode
    prevSelDoubleOutMode = bool(True) # to initiate the GUI with the current mode
    doubleInMode = bool(True)
    doubleOutMode = bool(False)
    CommitGameMode = [1, doubleInMode]

    gameStarted = bool(False)
    playerIndex = [0, 0]
    turnIndexLog = []
    editScoreMode = bool(False)
    editNameMode = bool(False)
    currentGameTurn = int(0)
    logIndex = int(0)
    
    quitbuttonPressed = bool(False)    
    
    # -------------------------------------------------------------------------------------------------------------------
    # DEFINING FUNCTIONS (CLASS METHODS)
    # -------------------------------------------------------------------------------------------------------------------
    # All below methods are stored in the mainApps_functions directory in separate .py files.
    # The name of the .py file and function must be the same in order to work properly

    def getNplayer(self):
        """
        A regular method that can access instance attributes.
        """
        return self.nbPlayer
    
    def addNplayer(self):
        """
        A regular method that can access instance attributes.
        """
        self.nbPlayer += 1
        return
    
    def addPlayer(self, player):
        """
        A regular method that can access instance attributes.
        """
        self.players += player
        return
    
    def getPlayer(self, index):
        """
        A regular method that can access instance attributes.
        """
        player = self.players(index)
        return player