from tkinter import *

def selectedMode(MainWindow):
    selection = MainWindow.subWin.mode_var.get()
    prevCommittedMode = MainWindow.CommitGameMode[:1]
    prevCommittedDounleInMode = MainWindow.CommitGameMode[1:]

    if selection == 1:
        MainWindow.SelectedGameMode = "Standard 301"
        MainWindow.subWin.mode1.configure(fg='black')
        eval("MainWindow.subWin.mode"+str(MainWindow.prevSelMode)+".configure(fg=MainWindow.Button_ft_color)")
        MainWindow.prevSelMode = 1
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != MainWindow.DoubleInMode:
            MainWindow.subWin.button_commitGameMode.config(state='normal')
        else:
            MainWindow.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 2:
        MainWindow.SelectedGameMode = "Standard 501"
        MainWindow.subWin.mode2.configure(fg='black')
        eval("MainWindow.subWin.mode"+str(MainWindow.prevSelMode)+".configure(fg=MainWindow.Button_ft_color)")
        MainWindow.prevSelMode = 2
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != MainWindow.DoubleInMode:
            MainWindow.subWin.button_commitGameMode.config(state='normal')
        else:
            MainWindow.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 3:
        MainWindow.SelectedGameMode = "Around the Clock"
        MainWindow.subWin.mode3.configure(fg='black')
        eval("MainWindow.subWin.mode"+str(MainWindow.prevSelMode)+".configure(fg=MainWindow.Button_ft_color)")
        MainWindow.prevSelMode = 3
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != MainWindow.DoubleInMode:
            MainWindow.subWin.button_commitGameMode.config(state='normal')
        else:
            MainWindow.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 4:
        MainWindow.SelectedGameMode = "180 Around the Clock"
        MainWindow.subWin.mode4.configure(fg='black')
        eval("MainWindow.subWin.mode"+str(MainWindow.prevSelMode)+".configure(fg=MainWindow.Button_ft_color)")
        MainWindow.prevSelMode = 4
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != MainWindow.DoubleInMode:
            MainWindow.subWin.button_commitGameMode.config(state='normal')
        else:
            MainWindow.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 5:
        MainWindow.SelectedGameMode = "Baseball"
        MainWindow.subWin.mode5.configure(fg='black')
        eval("MainWindow.subWin.mode"+str(MainWindow.prevSelMode)+".configure(fg=MainWindow.Button_ft_color)")
        MainWindow.prevSelMode = 5
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != MainWindow.DoubleInMode:
            MainWindow.subWin.button_commitGameMode.config(state='normal')
        else:
            MainWindow.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 6:
        MainWindow.SelectedGameMode = "Chase The Dragon"
        MainWindow.subWin.mode6.configure(fg='black')
        eval("MainWindow.subWin.mode"+str(MainWindow.prevSelMode)+".configure(fg=MainWindow.Button_ft_color)")
        MainWindow.prevSelMode = 6
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != MainWindow.DoubleInMode:
            MainWindow.subWin.button_commitGameMode.config(state='normal')
        else:
            MainWindow.subWin.button_commitGameMode.config(state='disabled')

    elif selection == 7:
        MainWindow.SelectedGameMode = "Cricket"
        MainWindow.subWin.mode7.configure(fg='black')
        eval("MainWindow.subWin.mode"+str(MainWindow.prevSelMode)+".configure(fg=MainWindow.Button_ft_color)")
        MainWindow.prevSelMode = 7
        if selection != prevCommittedMode[0] or prevCommittedDounleInMode[0] != MainWindow.DoubleInMode:
            MainWindow.subWin.button_commitGameMode.config(state='normal')
        else:
            MainWindow.subWin.button_commitGameMode.config(state='disabled')

    concoleMsg = "You selected the option " + str(MainWindow.SelectedGameMode)
    print(concoleMsg)

    return
