from tkinter import *
# import all Class methods as aliases, from the MainWindows_functions directory;
from MainWindow_functions import populateGUI as pGUI, initializeGUIvar, keyBindSetup as kBs, updateIndexLog as uIL, \
    writeCommitScore as wCS, endTurn as eT, clickPad as cP, commitScore as cS, commitAddPlayer as cAP, updateStatusLabel as uSL, \
    clearClickPad as cCP, startGame as sG, editScore as eS, addPlayer as aP, refreshImages as rI, editName as eN, \
    destroySubWin as dSW, quitGame as qG, populateGModeGUI as popGMGUI, commitGameMode as cGM, selectedMode as sM, \
    checkChanged as cC, checkChangedDoubleIn as cCDI


class MainWindow:

    def __init__(self, master):

        """The init initializes variables and populate the GUI. The variables will be remove from
        this object in the next version.
        """

        self.initializeGUIvar() # Create variables (temporary method)
        self.populateGUI(master)  # Create all tkinter GUI widgets
        self.keyBindSetup(master)  # keybinds the keyboard caLculator to the GUI

    # -------------------------------------------------------------------------------------------------------------------
    # DEFINING FUNCTIONS (CLASS METHODS)
    # -------------------------------------------------------------------------------------------------------------------
    # All below methods are stored in the MainWindows_functions directory in separate .py files.
    # The name of the .py file and function must be the same in order to work properly

    def initializeGUIvar(self): # Method that initialize all variables stored in the MainWindow Object (Temporary)
        initializeGUIvar.initializeGUIvar(self)
        return

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

