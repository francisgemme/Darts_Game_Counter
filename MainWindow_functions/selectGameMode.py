from tkinter import *

def selectGameMode(MainWindow):
    MainWindow.button_addPlayer.config(state=DISABLED)
    MainWindow.button_gameMode.config(state=DISABLED)

    MainWindow.subWin = Tk()
    MainWindow.subWin.eval('tk::PlaceWindow . center')

    MainWindow.subWin.emptylabel_1 = Label(MainWindow.subWin, padx=10, pady=10, bg=MainWindow.Button_bg_color,
                                           borderwidth=2)
    MainWindow.subWin.emptylabel_2 = Label(MainWindow.subWin, padx=10, pady=2, bg=MainWindow.Button_bg_color)

    MainWindow.subWin.mode1 = Radiobutton(MainWindow.subWin.emptylabel_1, text="Standard 701, 501, 301",
                                          padx=10, pady=5, font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                          fg="yellow", anchor="w", value= False)

    MainWindow.subWin.mode2 = Radiobutton(MainWindow.subWin.emptylabel_1, text="Around the Clock",
                                          padx=10, pady=5, font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                          fg="grey", anchor="w",value= False)

    MainWindow.subWin.mode3 = Radiobutton(MainWindow.subWin.emptylabel_1, text="180 Around the Clock",
                                          padx=10, pady=5, font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                          fg="grey", anchor="w",value= False)

    MainWindow.subWin.mode4 = Radiobutton(MainWindow.subWin.emptylabel_1, text="Baseball",
                                          padx=10, pady=5, font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                          fg="grey", anchor="w", value= False)

    MainWindow.subWin.mode5 = Radiobutton(MainWindow.subWin.emptylabel_1, text="Chase The Dragon",
                                          padx=10, pady=5, font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                          fg="grey", anchor="w", value= False)

    MainWindow.subWin.mode6 = Radiobutton(MainWindow.subWin.emptylabel_1, text="Cricket",
                                          padx=10, pady=5, font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                          fg="grey", anchor="w", value= False)

    MainWindow.subWin.button_commitGameMode = Button(MainWindow.subWin, text="Enregistrer", padx=10, pady=5,
                                                     font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                                     fg="yellow", command=MainWindow.commitGameMode,
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
