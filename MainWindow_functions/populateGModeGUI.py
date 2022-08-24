from tkinter import *

def populateGModeGUI(MainWindow):
    MainWindow.button_addPlayer.config(state=DISABLED)
    MainWindow.button_gameMode.config(state=DISABLED)

    MainWindow.subWin = Tk()
    MainWindow.subWin.eval('tk::PlaceWindow . center')
    MainWindow.subWin.geometry("258x380")


    MainWindow.subWin.emptylabel_0 = Label(MainWindow.subWin, padx=10, pady=2, bg=MainWindow.Button_bg_color)
    MainWindow.subWin.emptylabel_1 = LabelFrame(MainWindow.subWin, padx=10, pady=10, bg=MainWindow.Button_bg_color,
                                           borderwidth=2)
    MainWindow.subWin.emptylabel_2 = LabelFrame(MainWindow.subWin, padx=10, pady=10, bg=MainWindow.Button_bg_color,
                                           borderwidth=2)
    MainWindow.subWin.emptylabel_3 = LabelFrame(MainWindow.subWin, padx=10, pady=2, bg=MainWindow.Button_bg_color)

    #----------------------------------------------------------------------------------------------------------------
    # Radiobuttons
    #----------------------------------------------------------------------------------------------------------------
    MainWindow.subWin.mode_var = IntVar(MainWindow.subWin)

    MainWindow.subWin.mode1 = Radiobutton(MainWindow.subWin.emptylabel_1, indicatoron=0, text="Standard 301", font=("Helvetica", 12),
                                          padx=5, pady=5, bg=MainWindow.Button_bg_color, activebackground=MainWindow.Button_bg_color, selectcolor = MainWindow.activeButton_bg_color,
                                          fg='black', anchor="w", variable=MainWindow.subWin.mode_var, value=1, command= MainWindow.selectedMode)

    MainWindow.subWin.mode2 = Radiobutton(MainWindow.subWin.emptylabel_1, indicatoron=0, text="Standard 501", font=("Helvetica", 12),
                                          padx=5, pady=5, bg=MainWindow.Button_bg_color, activebackground=MainWindow.activeButton_bg_color, selectcolor = MainWindow.activeButton_bg_color,
                                          fg=MainWindow.Button_ft_color, anchor="w", variable=MainWindow.subWin.mode_var, value=2, command= MainWindow.selectedMode)

    MainWindow.subWin.mode3 = Radiobutton(MainWindow.subWin.emptylabel_2, indicatoron=0, text="Around the Clock", font=("Helvetica", 12),
                                          padx=5, pady=5, bg=MainWindow.Button_bg_color, activebackground=MainWindow.activeButton_bg_color, selectcolor = MainWindow.activeButton_bg_color,
                                          fg=MainWindow.Button_ft_color, anchor="w", variable=MainWindow.subWin.mode_var, value=3, command= MainWindow.selectedMode)

    MainWindow.subWin.mode4 = Radiobutton(MainWindow.subWin.emptylabel_2, indicatoron=0, text="180 Around the Clock", font=("Helvetica", 12),
                                          padx=5, pady=5, bg=MainWindow.Button_bg_color, activebackground=MainWindow.activeButton_bg_color, selectcolor = MainWindow.activeButton_bg_color,
                                          fg=MainWindow.Button_ft_color, anchor="w", variable=MainWindow.subWin.mode_var, value=4, command= MainWindow.selectedMode)

    MainWindow.subWin.mode5 = Radiobutton(MainWindow.subWin.emptylabel_2, indicatoron=0, text="Baseball", font=("Helvetica", 12),
                                          padx=5, pady=5, bg=MainWindow.Button_bg_color, activebackground=MainWindow.activeButton_bg_color, selectcolor = MainWindow.activeButton_bg_color,
                                          fg=MainWindow.Button_ft_color, anchor="w", variable=MainWindow.subWin.mode_var, value=5, command= MainWindow.selectedMode)

    MainWindow.subWin.mode6 = Radiobutton(MainWindow.subWin.emptylabel_2, indicatoron=0, text="Chase The Dragon", font=("Helvetica", 12),
                                          padx=5, pady=5, bg=MainWindow.Button_bg_color, activebackground=MainWindow.activeButton_bg_color, selectcolor = MainWindow.activeButton_bg_color,
                                          fg=MainWindow.Button_ft_color, anchor="w", variable=MainWindow.subWin.mode_var, value=6, command= MainWindow.selectedMode)

    MainWindow.subWin.mode7 = Radiobutton(MainWindow.subWin.emptylabel_2, indicatoron=0, text="Cricket", font=("Helvetica", 12),
                                          padx=5, pady=5, bg=MainWindow.Button_bg_color, activebackground=MainWindow.activeButton_bg_color, selectcolor = MainWindow.activeButton_bg_color,
                                          fg=MainWindow.Button_ft_color, anchor="w", variable=MainWindow.subWin.mode_var, value=7, command= MainWindow.selectedMode)



    #----------------------------------------------------------------------------------------------------------------
    # Buttons
    #----------------------------------------------------------------------------------------------------------------
    MainWindow.subWin.button_commitGameMode = Button(MainWindow.subWin.emptylabel_3, text="Enregistrer", padx=10, pady=5, anchor='e',
                                                     font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                                     fg="yellow", command=MainWindow.commitGameMode,
                                                     activebackground=MainWindow.activeButton_bg_color, state='disabled',
                                                     activeforeground=MainWindow.activeButton_ft_color)

    MainWindow.subWin.button_cancel = Button(MainWindow.subWin.emptylabel_3, text="Annuler", padx=10, pady=5, anchor='e',
                                             font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                             fg=MainWindow.Button_ft_color,
                                             activebackground=MainWindow.activeButton_bg_color,
                                             activeforeground=MainWindow.activeButton_ft_color,
                                             command=lambda: MainWindow.destroySubWin())

    MainWindow.subWin.emptylabel_0.grid(row=1, column=0, columnspan=4, sticky=NSEW)
    MainWindow.subWin.emptylabel_1.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    MainWindow.subWin.emptylabel_2.grid(row=1, column=0, columnspan=4, sticky=NSEW)
    MainWindow.subWin.emptylabel_3.grid(row=4, column=0, columnspan=4, sticky=EW)
    MainWindow.subWin.mode1.grid(row=0, column=0, sticky='ew')
    MainWindow.subWin.mode2.grid(row=1, column=0, sticky='ew')
    MainWindow.subWin.mode3.grid(row=2, column=0, sticky='ew')
    MainWindow.subWin.mode4.grid(row=3, column=0, sticky='ew')
    MainWindow.subWin.mode5.grid(row=4, column=0, sticky='ew')
    MainWindow.subWin.mode6.grid(row=5, column=0, sticky='ew')
    MainWindow.subWin.mode7.grid(row=6, column=0, sticky='ew')

    MainWindow.subWin.button_commitGameMode.grid(row=3, column=3, columnspan=1, sticky=E)
    MainWindow.subWin.button_cancel.grid(row=3, column=2, columnspan=1, sticky=E)

    MainWindow.subWin.wm_title("Sélectionner le Mode de jeu")
    MainWindow.subWin.configure(background=MainWindow.Button_bg_color)
    MainWindow.subWin.resizable(False, False)

    MainWindow.subWin.bind("<Return>", lambda event: MainWindow.commitGameMode())
    MainWindow.subWin.mode1.select()

    return


