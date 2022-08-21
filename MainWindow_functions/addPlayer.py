from tkinter import *

def addPlayer(MainWindow):

    # Disable MainWindow button
    MainWindow.button_addPlayer.config(state=DISABLED)
    MainWindow.button_gameMode.config(state=DISABLED)

    # Create another window (sub-window attached to Mainwindow)
    MainWindow.subWin = Tk()
    MainWindow.subWin.eval('tk::PlaceWindow . center')

    # Distinguishing if editing the name or adding a new player...
    if MainWindow.editNameMode == True:
        tmp = MainWindow.playerIndex[:1]  # Who is playing
        currentPlayer = tmp[0]
    elif MainWindow.editNameMode == False:
        currentPlayer = MainWindow.nbPlayer + 1

    # Populate all sub-GUI widgets
    MainWindow.subWin.emptylabel_1 = Label(MainWindow.subWin, padx=10, pady=10, bg=MainWindow.Button_bg_color)
    MainWindow.subWin.emptylabel_2 = Label(MainWindow.subWin, padx=10, pady=2, bg=MainWindow.Button_bg_color)
    MainWindow.subWin.emptylabel_3 = Label(MainWindow.subWin, text="Entrer le Nom du Joueur #%s" % (currentPlayer),
                                           font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                           fg=MainWindow.Button_ft_color)

    MainWindow.subWin.errorStatus = Label(MainWindow.subWin, text="", bg=MainWindow.Button_bg_color, fg="cyan")
    MainWindow.subWin.input_Name = Entry(MainWindow.subWin, width=20, bg='black', fg='yellow', borderwidth=3,
                                         font=("Helvetica", 16), justify='center')

    MainWindow.subWin.button_commitAddPlayer = Button(MainWindow.subWin, text="Enregistrer", padx=10, pady=5,
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
    MainWindow.subWin.emptylabel_3.grid(row=1, column=0, columnspan=1, padx=50, pady=10)
    MainWindow.subWin.errorStatus.grid(row=2, column=1, columnspan=1, padx=1, pady=10, sticky="n")
    MainWindow.subWin.input_Name.grid(row=1, column=1, columnspan=1)
    MainWindow.subWin.button_commitAddPlayer.grid(row=3, column=1, columnspan=1)
    MainWindow.subWin.button_cancel.grid(row=3, column=0, columnspan=1)

    MainWindow.subWin.wm_title("Ajouter Joueur #%s" % (currentPlayer))
    MainWindow.subWin.configure(background=MainWindow.Button_bg_color)
    MainWindow.subWin.resizable(False, False)

    MainWindow.subWin.bind("<Return>", lambda event: MainWindow.commitAddPlayer())
    MainWindow.subWin.after(1, lambda: MainWindow.subWin.input_Name.focus_force())

    return
