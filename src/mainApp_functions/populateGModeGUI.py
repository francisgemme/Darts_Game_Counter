from tkinter import *


def populateGModeGUI(mainApp):
    mainApp.button_addPlayer.config(state=DISABLED)
    mainApp.button_gameMode.config(state=DISABLED)

    mainApp.subWin = Tk()
    mainApp.subWin.eval('tk::PlaceWindow . center')
    mainApp.subWin.geometry("355x450")

    mainApp.subWin.emptylabel_0 = Label(mainApp.subWin, padx=20, pady=2, bg=mainApp.Button_bg_color)
    mainApp.subWin.emptylabel_1 = LabelFrame(mainApp.subWin, padx=20, pady=10, bg=mainApp.Button_bg_color,
                                           borderwidth=2)
    mainApp.subWin.emptylabel_2 = LabelFrame(mainApp.subWin, padx=20, pady=10, bg=mainApp.Button_bg_color,
                                           borderwidth=2)
    mainApp.subWin.emptylabel_3 = LabelFrame(mainApp.subWin, padx=20, pady=2, bg=mainApp.Button_bg_color)

    #----------------------------------------------------------------------------------------------------------------
    # Radiobuttons
    #----------------------------------------------------------------------------------------------------------------
    mainApp.subWin.mode_var = IntVar(mainApp.subWin)
    mainApp.subWin.mode1 = Radiobutton(mainApp.subWin.emptylabel_1, indicatoron=0, text="Standard: 301", font=("Helvetica", 14), anchor='center',
                                          width=27, pady=5, bg=mainApp.Button_bg_color, activebackground=mainApp.Button_bg_color, selectcolor = mainApp.activeButton_bg_color,
                                          fg='black', variable=mainApp.subWin.mode_var, value=1, command= mainApp.selectedMode)

    mainApp.subWin.mode2 = Radiobutton(mainApp.subWin.emptylabel_1, indicatoron=0, text="Standard: 501", font=("Helvetica", 14), anchor='center',
                                          width=27, pady=5, bg=mainApp.Button_bg_color, activebackground=mainApp.activeButton_bg_color, selectcolor = mainApp.activeButton_bg_color,
                                          fg=mainApp.Button_ft_color, variable=mainApp.subWin.mode_var, value=2, command= mainApp.selectedMode)


    mainApp.subWin.DoubleInModeONVar = IntVar(mainApp.subWin)
    mainApp.subWin.DoubleInModeOFFVar = IntVar(mainApp.subWin)
    mainApp.subWin.DoubleIn_ON = Checkbutton(mainApp.subWin.emptylabel_1, indicatoron=0, onvalue=1, offvalue=0,
                                                variable=mainApp.subWin.DoubleInModeONVar,
                                                command=lambda: mainApp.checkChangedDoubleIn('ON'),
                                                width = 7, selectcolor = mainApp.activeButton_bg_color,
                                                bg=mainApp.Button_bg_color,
                                                text = "ON",
                                                fg=mainApp.Button_ft_color,
                                                activebackground=mainApp.activeButton_bg_color)
    mainApp.subWin.DoubleIn_OFF = Checkbutton(mainApp.subWin.emptylabel_1, indicatoron=0, onvalue=1, offvalue=0,
                                                 variable=mainApp.subWin.DoubleInModeOFFVar,
                                                 command=lambda: mainApp.checkChangedDoubleIn('OFF'),
                                                 width = 7, selectcolor = mainApp.activeButton_bg_color,
                                                 bg=mainApp.Button_bg_color,
                                                 text = "OFF",
                                                 fg=mainApp.Button_ft_color,
                                                 activebackground=mainApp.activeButton_bg_color)
    if mainApp.match_inst.doubleInMode == True:
        mainApp.subWin.DoubleIn_ON.select()
        mainApp.subWin.DoubleIn_ON.configure(fg='black')


    mainApp.subWin.DoubleInLabel = Entry(mainApp.subWin.emptylabel_1, bg=mainApp.Button_bg_color, fg="grey", width=15,
                                            font=("Helvetica", 12), justify='right', disabledbackground=mainApp.Button_bg_color,
                                            disabledforeground= mainApp.disabledButton_ft_color, border=0)
    mainApp.subWin.DoubleInLabel.insert(0, "Double-In Mode: ")
    mainApp.subWin.DoubleInLabel.config(state=DISABLED)

    mainApp.subWin.mode3 = Radiobutton(mainApp.subWin.emptylabel_2, indicatoron=0, text="Around the Clock", font=("Helvetica", 14),
                                          width=27, pady=5, bg=mainApp.Button_bg_color, activebackground=mainApp.activeButton_bg_color, selectcolor = mainApp.activeButton_bg_color,
                                          fg=mainApp.Button_ft_color, anchor="center", variable=mainApp.subWin.mode_var, value=3, command= mainApp.selectedMode)

    mainApp.subWin.mode4 = Radiobutton(mainApp.subWin.emptylabel_2, indicatoron=0, text="180 Around the Clock", font=("Helvetica", 14),
                                          width=27, pady=5, bg=mainApp.Button_bg_color, activebackground=mainApp.activeButton_bg_color, selectcolor = mainApp.activeButton_bg_color,
                                          fg=mainApp.Button_ft_color, anchor="center", variable=mainApp.subWin.mode_var, value=4, command= mainApp.selectedMode)

    mainApp.subWin.mode5 = Radiobutton(mainApp.subWin.emptylabel_2, indicatoron=0, text="Baseball", font=("Helvetica", 14),
                                          width=27, pady=5, bg=mainApp.Button_bg_color, activebackground=mainApp.activeButton_bg_color, selectcolor = mainApp.activeButton_bg_color,
                                          fg=mainApp.Button_ft_color, anchor="center", variable=mainApp.subWin.mode_var, value=5, command= mainApp.selectedMode)

    mainApp.subWin.mode6 = Radiobutton(mainApp.subWin.emptylabel_2, indicatoron=0, text="Chase The Dragon", font=("Helvetica", 14),
                                          width=27, pady=5, bg=mainApp.Button_bg_color, activebackground=mainApp.activeButton_bg_color, selectcolor = mainApp.activeButton_bg_color,
                                          fg=mainApp.Button_ft_color, anchor="center", variable=mainApp.subWin.mode_var, value=6, command= mainApp.selectedMode)

    mainApp.subWin.mode7 = Radiobutton(mainApp.subWin.emptylabel_2, indicatoron=0, text="Cricket", font=("Helvetica", 14),
                                          padx=5, pady=5, bg=mainApp.Button_bg_color, activebackground=mainApp.activeButton_bg_color, selectcolor = mainApp.activeButton_bg_color,
                                          fg=mainApp.Button_ft_color, anchor="center", variable=mainApp.subWin.mode_var, value=7, command= mainApp.selectedMode)



    #----------------------------------------------------------------------------------------------------------------
    # Buttons
    #----------------------------------------------------------------------------------------------------------------
    mainApp.subWin.button_commitGameMode = Button(mainApp.subWin.emptylabel_3, text="Appliquer", padx=12, pady=5, anchor='center',
                                                     font=("Helvetica", 14), bg=mainApp.Button_bg_color,
                                                     fg="yellow", command=lambda: mainApp.commitGameMode(), width=11,
                                                     activebackground=mainApp.activeButton_bg_color, state='disabled',
                                                     activeforeground=mainApp.activeButton_ft_color)

    mainApp.subWin.button_cancel = Button(mainApp.subWin.emptylabel_3, text="Annuler", padx=12, pady=5, anchor='center',
                                             font=("Helvetica", 14), bg=mainApp.Button_bg_color,
                                             fg=mainApp.Button_ft_color, width=11,
                                             activebackground=mainApp.activeButton_bg_color,
                                             activeforeground=mainApp.activeButton_ft_color,
                                             command=lambda: mainApp.destroySubWin())

    mainApp.subWin.emptylabel_0.grid(row=1, column=1, sticky=NSEW)
    mainApp.subWin.emptylabel_1.grid(row=0, column=1, sticky=NSEW)
    mainApp.subWin.emptylabel_2.grid(row=1, column=1, sticky=NSEW)
    mainApp.subWin.emptylabel_3.grid(row=4, column=1, sticky=NSEW)

    mainApp.subWin.mode1.grid(row=0, column=0, sticky='ew', columnspan=3)
    mainApp.subWin.mode2.grid(row=1, column=0, sticky='ew',columnspan=3)
    mainApp.subWin.DoubleInLabel.grid(row=3, column=0, ipady=15)
    mainApp.subWin.DoubleIn_ON.grid(row=3, column=1, sticky=E)
    mainApp.subWin.DoubleIn_OFF.grid(row=3, column=2, sticky=W)
    mainApp.subWin.mode3.grid(row=2, column=0, sticky='ew')
    mainApp.subWin.mode4.grid(row=3, column=0, sticky='ew')
    mainApp.subWin.mode5.grid(row=4, column=0, sticky='ew')
    mainApp.subWin.mode6.grid(row=5, column=0, sticky='ew')
    mainApp.subWin.mode7.grid(row=6, column=0, sticky='ew')

    mainApp.subWin.button_commitGameMode.grid(row=3, column=3, sticky=E)
    mainApp.subWin.button_cancel.grid(row=3, column=2, sticky=E)

    mainApp.subWin.wm_title("Sélectionner le Mode de Jeu")
    mainApp.subWin.configure(background=mainApp.Button_bg_color)
    mainApp.subWin.resizable(False, False)

    mainApp.subWin.bind("<Return>", lambda event: mainApp.commitGameMode())
    mainApp.subWin.mode1.select()

    return


