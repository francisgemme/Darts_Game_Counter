from tkinter import *


def checkChangedDoubleIn(MainWindow,buttonPressed):

    selectedMode = MainWindow.subWin.mode_var.get()
    prevCommittedMode = MainWindow.CommitGameMode[:1]
    prevCommittedDounleInMode = MainWindow.CommitGameMode[1:]

    print(prevCommittedMode[0])
    print(prevCommittedDounleInMode[0])

    if buttonPressed == "ON":
        MainWindow.DoubleInMode = True
        MainWindow.subWin.DoubleIn_ON.configure(fg='black')
        MainWindow.subWin.DoubleIn_OFF.configure(fg=MainWindow.Button_ft_color)
        MainWindow.subWin.DoubleInModeONVar.set(1)
        MainWindow.subWin.DoubleInModeOFFVar.set(0)

    elif buttonPressed == "OFF":
        MainWindow.DoubleInMode = False
        MainWindow.subWin.DoubleIn_OFF.configure(fg='black')
        MainWindow.subWin.DoubleIn_ON.configure(fg=MainWindow.Button_ft_color)
        MainWindow.subWin.DoubleInModeONVar.set(0)
        MainWindow.subWin.DoubleInModeOFFVar.set(1)

    if prevCommittedDounleInMode[0] != MainWindow.DoubleInMode and selectedMode != prevCommittedMode[0]:
        MainWindow.subWin.button_commitGameMode.config(state='normal')
    elif prevCommittedDounleInMode[0] != MainWindow.DoubleInMode and selectedMode == prevCommittedMode[0]:
        MainWindow.subWin.button_commitGameMode.config(state='normal')
    elif prevCommittedDounleInMode[0] == MainWindow.DoubleInMode and selectedMode == prevCommittedMode[0]:
        MainWindow.subWin.button_commitGameMode.config(state='disabled')

    return
