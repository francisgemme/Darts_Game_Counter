from tkinter import *
# import all Class methods as aliases, from the MainWindows_functions directory;
from MainWindow_functions import populateGUI as pGUI, initializeGUIvar, keyBindSetup as kBs, updateIndexLog as uIL, \
    writeCommitScore as wCS, endTurn as eT, clickPad as cP, commitScore as cS, commitAddPlayer as cAP, updateStatusLabel as uSL, \
    clearClickPad as cCP, startGame as sG, editScore as eS, addPlayer as aP, refreshImages as rI, editName as eN, \
    destroySubWin as dSW, quitGame as qG


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

    def function_gameMode(MainWindow):

        MainWindow.button_addPlayer.config(state=DISABLED)
        MainWindow.button_gameMode.config(state=DISABLED)

        MainWindow.subWin = Tk()
        MainWindow.subWin.eval('tk::PlaceWindow . center')

        MainWindow.subWin.emptylabel_1 = Label(MainWindow.subWin, padx=10, pady=10, bg=MainWindow.Button_bg_color, borderwidth= 2)
        MainWindow.subWin.emptylabel_2 = Label(MainWindow.subWin, padx=10, pady=2, bg=MainWindow.Button_bg_color)


        MainWindow.subWin.mode1 = Radiobutton(MainWindow.subWin.emptylabel_1,text="Standard 701, 501, 301",
                                              padx=10, pady=5, font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                              fg="yellow", anchor="w")

        MainWindow.subWin.mode2 = Radiobutton(MainWindow.subWin.emptylabel_1,text="Around the Clock",
                                              padx=10, pady=5, font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                              fg="grey", anchor="w")

        MainWindow.subWin.mode3 = Radiobutton(MainWindow.subWin.emptylabel_1,text="180 Around the Clock",
                                              padx=10, pady=5, font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                              fg="grey", anchor="w")

        MainWindow.subWin.mode4 = Radiobutton(MainWindow.subWin.emptylabel_1,text="Baseball",
                                              padx=10, pady=5, font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                              fg="grey", anchor="w")

        MainWindow.subWin.mode5 = Radiobutton(MainWindow.subWin.emptylabel_1,text="Chase The Dragon",
                                              padx=10, pady=5, font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                              fg="grey", anchor="w")

        MainWindow.subWin.mode6 = Radiobutton(MainWindow.subWin.emptylabel_1,text="Cricket",
                                              padx=10, pady=5, font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                              fg="grey", anchor="w")

        MainWindow.subWin.button_commitGameMode = Button(MainWindow.subWin, text="Enregistrer", padx=10, pady=5,
                                                          font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                                          fg="yellow", command=MainWindow.commitAddPlayer,
                                                          activebackground=MainWindow.activeButton_bg_color,
                                                          activeforeground=MainWindow.activeButton_ft_color)

        MainWindow.subWin.button_cancel = Button(MainWindow.subWin, text="Annuler", padx=10, pady=5,
                                                 font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                                 fg=MainWindow.Button_ft_color,
                                                 activebackground=MainWindow.activeButton_bg_color,
                                                 activeforeground=MainWindow.activeButton_ft_color,
                                                 command=lambda: MainWindow.destroySubWin())

        MainWindow.subWin.emptylabel_1.grid(row=0, column=0, columnspan=4)
        MainWindow.subWin.emptylabel_2.grid(row=4, column=0, columnspan=4)
        MainWindow.subWin.mode1.grid(row=0, column=0, sticky='w')
        MainWindow.subWin.mode2.grid(row=1, column=0, sticky='w')
        MainWindow.subWin.mode3.grid(row=2, column=0, sticky='w')
        MainWindow.subWin.mode4.grid(row=3, column=0, sticky='w')
        MainWindow.subWin.mode5.grid(row=4, column=0, sticky='w')
        MainWindow.subWin.mode6.grid(row=5, column=0, sticky='w')


        MainWindow.subWin.button_commitGameMode.grid(row=3, column=1, columnspan=1)
        MainWindow.subWin.button_cancel.grid(row=3, column=0, columnspan=1)

        MainWindow.subWin.wm_title("Sélectionner le Mode de jeu")
        MainWindow.subWin.configure(background=MainWindow.Button_bg_color)
        MainWindow.subWin.resizable(False, False)

        MainWindow.subWin.bind("<Return>", lambda event: MainWindow.commitGameMode())




