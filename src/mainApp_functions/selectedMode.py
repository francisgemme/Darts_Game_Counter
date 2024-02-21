from tkinter import *

def selectedMode(mainApp):
    selection = mainApp.subWin.mode_var.get()
    prevCommittedMode = mainApp.CommitGameMode[:1]
    prevCommittedDounleInMode = mainApp.CommitGameMode[1:]

    if selection == 1:
        mainApp.SelectedGameMode = "Standard 301"
        mainApp.subWin.mode1.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.prevSelMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.prevSelMode = 1
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.DoubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 2:
        mainApp.SelectedGameMode = "Standard 501"
        mainApp.subWin.mode2.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.prevSelMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.prevSelMode = 2
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.DoubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 3:
        mainApp.SelectedGameMode = "Around the Clock"
        mainApp.subWin.mode3.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.prevSelMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.prevSelMode = 3
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.DoubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 4:
        mainApp.SelectedGameMode = "180 Around the Clock"
        mainApp.subWin.mode4.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.prevSelMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.prevSelMode = 4
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.DoubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 5:
        mainApp.SelectedGameMode = "Baseball"
        mainApp.subWin.mode5.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.prevSelMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.prevSelMode = 5
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.DoubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 6:
        mainApp.SelectedGameMode = "Chase The Dragon"
        mainApp.subWin.mode6.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.prevSelMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.prevSelMode = 6
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.DoubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 7:
        mainApp.SelectedGameMode = "Cricket"
        mainApp.subWin.mode7.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.prevSelMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.prevSelMode = 7
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.DoubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

    concoleMsg = "You selected the option " + str(mainApp.SelectedGameMode)
    print(concoleMsg)

    return
