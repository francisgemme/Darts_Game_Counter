# import all Class methods as aliases, from the MainWindows_functions directory;
from MainWindow_functions import populateGUI as pGUI, keyBindSetup as kBs, updateIndexLog as uIL, \
    writeCommitScore as wCS, endTurn as eT, clickPad as cP, commitScore as cS, commitAddPlayer as cAP, updateStatusLabel as uSL, \
    clearClickPad as cCP, startGame as sG, editScore as eS, addPlayer as aP, refreshImages as rI, editName as eN, \
    destroySubWin as dSW, quitGame as qG, populateGModeGUI as popGMGUI, commitGameMode as cGM, selectedMode as sM, \
    checkChanged as cC, checkChangedDoubleIn as cCDI

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

    nbPlayer = 0
    p1_DoubleInVar = False
    p2_DoubleInVar = False
    p3_DoubleInVar = False
    p4_DoubleInVar = False
    SelectedGameMode = []
    prevSelMode = 1
    DoubleInMode = True
    DoubleOutMode = False
    CommitGameMode = [1, DoubleInMode]
    gameStarted = False
    playerIndex = [0, 0]
    turnIndexLog = []
    editScoreMode = False
    editNameMode = False
    currentGameTurn = 0
    logIndex = 0
    doubleInMode = True
    quitbuttonPressed = False   


    # -------------------------------------------------------------------------------------------------------------------
    # DEFINING FUNCTIONS (CLASS METHODS)
    # -------------------------------------------------------------------------------------------------------------------
    # All below methods are stored in the MainWindows_functions directory in separate .py files.
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

    def populateGUI(self, master): # Creates and locates all tkinter widgets
        pGUI.populateGUI(self, master)
        return

    def keyBindSetup(self, master): # Keybinding methods
        kBs.keyBindSetup(self, master)
        return

    def clickPad(self, number):
        cP.clickPad(self, number)
        return

    def commitScore(self):
        cS.commitScore(self)
        return

    def writeCommitScore(self):
        wCS.writeCommitScore(self)
        return

    def endTurn(self):
        eT.endTurn(self)
        return

    def updateStatusLabel(self, text):
        uSL.updateStatusLabel(self, text)
        return

    def commitAddPlayer(self):
        cAP.commitAddPlayer(self)
        return

    def startGame(self):
        sG.startGame(self)
        return

    def refreshImages(self):
        rI.refreshImages(self)
        return

    def clearClickPad(self):
        cCP.clearClickPad(self)
        return

    def updateIndexLog(self):
        uIL.updateIndexLog(self)
        return

    def editScore(self):
        eS.editScore(self)
        return

    def editName(self):
        eN.editName(self)
        return

    def addPlayer(self):
        aP.addPlayer(self)
        return

    def destroySubWin(self):
        dSW.destroySubWin(self)
        return

    def quitGame(self, master):
        qG.quitGame(self, master)
        return

    def populateGModeGUI(self):
        popGMGUI.populateGModeGUI(self)
        return

    def commitGameMode(self):
        cGM.commitGameMode(self)
        return

    def selectedMode(self):
        sM.selectedMode(self)
        return

    def checkChanged(self):
        cC.checkChanged(self)
        return

    def checkChangedDoubleIn(self, buttonPressed):
        cCDI.checkChangedDoubleIn(self,buttonPressed)


# Example usage:
# Call the static method directly from the class
#MainWindow.static_method()

# Create an instance of MainWindow and call the regular method
#main_window_instance = MainWindow()
#main_window_instance.nbPlayer = 4
#main_window_instance.regular_method()

