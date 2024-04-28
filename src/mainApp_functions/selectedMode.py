from tkinter import *

def selectedMode(mainApp):
    selection = mainApp.subWin.mode_var.get()
    prevCommittedMode = mainApp.CommitGameMode[:1]
    prevCommittedDounleInMode = mainApp.CommitGameMode[1:]

    if selection == 1:
        mainApp.match_inst.SelectedGameMode = "Standard 301"
        mainApp.subWin.mode1.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.match_inst.prevSelMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.match_inst.prevSelMode = 1
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.match_inst.doubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 2:
        mainApp.match_inst.SelectedGameMode = "Standard 501"
        mainApp.subWin.mode2.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.match_inst.prevSelMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.match_inst.prevSelMode = 2
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.match_inst.doubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 3:
        mainApp.match_inst.SelectedGameMode = "Around the Clock"
        mainApp.subWin.mode3.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.match_inst.prevSelMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.match_inst.prevSelMode = 3
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.match_inst.doubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 4:
        mainApp.match_inst.SelectedGameMode = "180 Around the Clock"
        mainApp.subWin.mode4.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.match_inst.prevSelMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.match_inst.prevSelMode = 4
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.match_inst.doubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 5:
        mainApp.match_inst.SelectedGameMode = "Baseball"
        mainApp.subWin.mode5.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.match_inst.prevSelMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.match_inst.prevSelMode = 5
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.match_inst.doubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 6:
        mainApp.match_inst.SelectedGameMode = "Chase The Dragon"
        mainApp.subWin.mode6.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.match_inst.prevSelMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.match_inst.prevSelMode = 6
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.match_inst.doubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 7:
        mainApp.match_inst.SelectedGameMode = "Cricket"
        mainApp.subWin.mode7.configure(fg='black')
        eval("mainApp.subWin.mode"+str(mainApp.match_inst.prevSelMode)+".configure(fg=mainApp.Button_ft_color)")
        mainApp.match_inst.prevSelMode = 7
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != mainApp.match_inst.doubleInMode:
            mainApp.subWin.button_commitGameMode.config(state='normal')
        else:
            mainApp.subWin.button_commitGameMode.config(state='disabled')

    concoleMsg = "You selected the option " + str(mainApp.match_inst.SelectedGameMode)
    print(concoleMsg)

    return
