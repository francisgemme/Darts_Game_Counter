from tkinter import *


def populateGModeGUI(MainWindow):
    MainWindow.button_addPlayer.config(state=DISABLED)
    MainWindow.button_gameMode.config(state=DISABLED)

    MainWindow.subWin = Tk()
    MainWindow.subWin.eval('tk::PlaceWindow . center')
    MainWindow.subWin.geometry("355x450")

    MainWindow.subWin.emptylabel_0 = Label(MainWindow.subWin, padx=20, pady=2, bg=MainWindow.Button_bg_color)
    MainWindow.subWin.emptylabel_1 = LabelFrame(MainWindow.subWin, padx=20, pady=10, bg=MainWindow.Button_bg_color,
                                           borderwidth=2)
    MainWindow.subWin.emptylabel_2 = LabelFrame(MainWindow.subWin, padx=20, pady=10, bg=MainWindow.Button_bg_color,
                                           borderwidth=2)
    MainWindow.subWin.emptylabel_3 = LabelFrame(MainWindow.subWin, padx=20, pady=2, bg=MainWindow.Button_bg_color)

    #----------------------------------------------------------------------------------------------------------------
    # Radiobuttons
    #----------------------------------------------------------------------------------------------------------------
    MainWindow.subWin.mode_var = IntVar(MainWindow.subWin)
    MainWindow.subWin.mode1 = Radiobutton(MainWindow.subWin.emptylabel_1, indicatoron=0, text="Standard: 301", font=("Helvetica", 14), anchor='center',
                                          width=27, pady=5, bg=MainWindow.Button_bg_color, activebackground=MainWindow.Button_bg_color, selectcolor = MainWindow.activeButton_bg_color,
                                          fg='black', variable=MainWindow.subWin.mode_var, value=1, command= MainWindow.selectedMode)

    MainWindow.subWin.mode2 = Radiobutton(MainWindow.subWin.emptylabel_1, indicatoron=0, text="Standard: 501", font=("Helvetica", 14), anchor='center',
                                          width=27, pady=5, bg=MainWindow.Button_bg_color, activebackground=MainWindow.activeButton_bg_color, selectcolor = MainWindow.activeButton_bg_color,
                                          fg=MainWindow.Button_ft_color, variable=MainWindow.subWin.mode_var, value=2, command= MainWindow.selectedMode)


    MainWindow.subWin.DoubleInModeONVar = IntVar(MainWindow.subWin)
    MainWindow.subWin.DoubleInModeOFFVar = IntVar(MainWindow.subWin)
    MainWindow.subWin.DoubleIn_ON = Checkbutton(MainWindow.subWin.emptylabel_1, indicatoron=0, onvalue=1, offvalue=0,
                                                variable=MainWindow.subWin.DoubleInModeONVar,
                                                command=lambda: MainWindow.checkChangedDoubleIn('ON'),
                                                width = 7, selectcolor = MainWindow.activeButton_bg_color,
                                                bg=MainWindow.Button_bg_color,
                                                text = "ON",
                                                fg=MainWindow.Button_ft_color,
                                                activebackground=MainWindow.activeButton_bg_color)
    MainWindow.subWin.DoubleIn_OFF = Checkbutton(MainWindow.subWin.emptylabel_1, indicatoron=0, onvalue=1, offvalue=0,
                                                 variable=MainWindow.subWin.DoubleInModeOFFVar,
                                                 command=lambda: MainWindow.checkChangedDoubleIn('OFF'),
                                                 width = 7, selectcolor = MainWindow.activeButton_bg_color,
                                                 bg=MainWindow.Button_bg_color,
                                                 text = "OFF",
                                                 fg=MainWindow.Button_ft_color,
                                                 activebackground=MainWindow.activeButton_bg_color)
    if MainWindow.DoubleInMode == True:
        MainWindow.subWin.DoubleIn_ON.select()
        MainWindow.subWin.DoubleIn_ON.configure(fg='black')


    MainWindow.subWin.DoubleInLabel = Entry(MainWindow.subWin.emptylabel_1, bg=MainWindow.Button_bg_color, fg="grey", width=15,
                                            font=("Helvetica", 12), justify='right', disabledbackground=MainWindow.Button_bg_color,
                                            disabledforeground= MainWindow.disabledButton_ft_color, border=0)
    MainWindow.subWin.DoubleInLabel.insert(0, "Double-In Mode: ")
    MainWindow.subWin.DoubleInLabel.config(state=DISABLED)

    MainWindow.subWin.mode3 = Radiobutton(MainWindow.subWin.emptylabel_2, indicatoron=0, text="Around the Clock", font=("Helvetica", 14),
                                          width=27, pady=5, bg=MainWindow.Button_bg_color, activebackground=MainWindow.activeButton_bg_color, selectcolor = MainWindow.activeButton_bg_color,
                                          fg=MainWindow.Button_ft_color, anchor="center", variable=MainWindow.subWin.mode_var, value=3, command= MainWindow.selectedMode)

    MainWindow.subWin.mode4 = Radiobutton(MainWindow.subWin.emptylabel_2, indicatoron=0, text="180 Around the Clock", font=("Helvetica", 14),
                                          width=27, pady=5, bg=MainWindow.Button_bg_color, activebackground=MainWindow.activeButton_bg_color, selectcolor = MainWindow.activeButton_bg_color,
                                          fg=MainWindow.Button_ft_color, anchor="center", variable=MainWindow.subWin.mode_var, value=4, command= MainWindow.selectedMode)

    MainWindow.subWin.mode5 = Radiobutton(MainWindow.subWin.emptylabel_2, indicatoron=0, text="Baseball", font=("Helvetica", 14),
                                          width=27, pady=5, bg=MainWindow.Button_bg_color, activebackground=MainWindow.activeButton_bg_color, selectcolor = MainWindow.activeButton_bg_color,
                                          fg=MainWindow.Button_ft_color, anchor="center", variable=MainWindow.subWin.mode_var, value=5, command= MainWindow.selectedMode)

    MainWindow.subWin.mode6 = Radiobutton(MainWindow.subWin.emptylabel_2, indicatoron=0, text="Chase The Dragon", font=("Helvetica", 14),
                                          width=27, pady=5, bg=MainWindow.Button_bg_color, activebackground=MainWindow.activeButton_bg_color, selectcolor = MainWindow.activeButton_bg_color,
                                          fg=MainWindow.Button_ft_color, anchor="center", variable=MainWindow.subWin.mode_var, value=6, command= MainWindow.selectedMode)

    MainWindow.subWin.mode7 = Radiobutton(MainWindow.subWin.emptylabel_2, indicatoron=0, text="Cricket", font=("Helvetica", 14),
                                          padx=5, pady=5, bg=MainWindow.Button_bg_color, activebackground=MainWindow.activeButton_bg_color, selectcolor = MainWindow.activeButton_bg_color,
                                          fg=MainWindow.Button_ft_color, anchor="center", variable=MainWindow.subWin.mode_var, value=7, command= MainWindow.selectedMode)



    #----------------------------------------------------------------------------------------------------------------
    # Buttons
    #----------------------------------------------------------------------------------------------------------------
    MainWindow.subWin.button_commitGameMode = Button(MainWindow.subWin.emptylabel_3, text="Appliquer", padx=12, pady=5, anchor='center',
                                                     font=("Helvetica", 14), bg=MainWindow.Button_bg_color,
                                                     fg="yellow", command=lambda: MainWindow.commitGameMode(), width=11,
                                                     activebackground=MainWindow.activeButton_bg_color, state='disabled',
                                                     activeforeground=MainWindow.activeButton_ft_color)

    MainWindow.subWin.button_cancel = Button(MainWindow.subWin.emptylabel_3, text="Annuler", padx=12, pady=5, anchor='center',
                                             font=("Helvetica", 14), bg=MainWindow.Button_bg_color,
                                             fg=MainWindow.Button_ft_color, width=11,
                                             activebackground=MainWindow.activeButton_bg_color,
                                             activeforeground=MainWindow.activeButton_ft_color,
                                             command=lambda: MainWindow.destroySubWin())

    MainWindow.subWin.emptylabel_0.grid(row=1, column=1, sticky=NSEW)
    MainWindow.subWin.emptylabel_1.grid(row=0, column=1, sticky=NSEW)
    MainWindow.subWin.emptylabel_2.grid(row=1, column=1, sticky=NSEW)
    MainWindow.subWin.emptylabel_3.grid(row=4, column=1, sticky=NSEW)

    MainWindow.subWin.mode1.grid(row=0, column=0, sticky='ew', columnspan=3)
    MainWindow.subWin.mode2.grid(row=1, column=0, sticky='ew',columnspan=3)
    MainWindow.subWin.DoubleInLabel.grid(row=3, column=0, ipady=15)
    MainWindow.subWin.DoubleIn_ON.grid(row=3, column=1, sticky=E)
    MainWindow.subWin.DoubleIn_OFF.grid(row=3, column=2, sticky=W)
    MainWindow.subWin.mode3.grid(row=2, column=0, sticky='ew')
    MainWindow.subWin.mode4.grid(row=3, column=0, sticky='ew')
    MainWindow.subWin.mode5.grid(row=4, column=0, sticky='ew')
    MainWindow.subWin.mode6.grid(row=5, column=0, sticky='ew')
    MainWindow.subWin.mode7.grid(row=6, column=0, sticky='ew')

    MainWindow.subWin.button_commitGameMode.grid(row=3, column=3, sticky=E)
    MainWindow.subWin.button_cancel.grid(row=3, column=2, sticky=E)

    MainWindow.subWin.wm_title("Sélectionner Mode de Jeu")
    MainWindow.subWin.configure(background=MainWindow.Button_bg_color)
    MainWindow.subWin.resizable(False, False)

    MainWindow.subWin.bind("<Return>", lambda event: MainWindow.commitGameMode())
    MainWindow.subWin.mode1.select()

    return


