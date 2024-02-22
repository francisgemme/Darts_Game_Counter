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
        DoubleInMode (bool): Double In Mode.
        DoubleOutMode (bool): Double Out Mode.
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

    nbPlayer = int(0)
    p1_DoubleInVar = bool(False)
    p2_DoubleInVar = bool(False)
    p3_DoubleInVar = bool(False)
    p4_DoubleInVar = bool(False)
    SelectedGameMode = []
    prevSelMode = 1
    DoubleInMode = bool(True)
    DoubleOutMode = bool(False)
    CommitGameMode = [1, DoubleInMode]
    gameStarted = bool(False)
    playerIndex = [int(0), int(0)]
    turnIndexLog = []
    editScoreMode = bool(False)
    editNameMode = bool(False)
    currentGameTurn = int(0)
    logIndex = int(0)
    doubleInMode = bool(True)
    quitbuttonPressed = bool(False)  
    
    # -------------------------------------------------------------------------------------------------------------------
    # DEFINING FUNCTIONS (CLASS METHODS)
    # -------------------------------------------------------------------------------------------------------------------
    # All below methods are stored in the mainApps_functions directory in separate .py files.
    # The name of the .py file and function must be the same in order to work properly

    @staticmethod
    def static_method():
        """
        A static method that does not require access to instance attributes.
        """
        print("This is a static method")

    def regular_method(self):
        """
        A regular method that can access instance attributes.
        """
        print("This is a regular method")
        print("Number of players:", self.nbPlayer)

    def getNplayer(self):
        return self.nbPlayer
    
    def addNplayer(self):
        self.nbPlayer += 1
        return