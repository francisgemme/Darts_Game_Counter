from tkinter import *

def checkChangedDoubleIn(mainApp,buttonPressed):

    selectedMode = mainApp.subWin.mode_var.get()
    prevCommittedMode = mainApp.CommitGameMode[:1]
    prevCommittedDounleInMode = mainApp.CommitGameMode[1:]

    print(prevCommittedMode[0])
    print(prevCommittedDounleInMode[0])

    if buttonPressed == "ON":
        mainApp.DoubleInMode = True
        mainApp.subWin.DoubleIn_ON.configure(fg='black')
        mainApp.subWin.DoubleIn_OFF.configure(fg=mainApp.Button_ft_color)
        mainApp.subWin.DoubleInModeONVar.set(1)
        mainApp.subWin.DoubleInModeOFFVar.set(0)

    elif buttonPressed == "OFF":
        mainApp.DoubleInMode = False
        mainApp.subWin.DoubleIn_OFF.configure(fg='black')
        mainApp.subWin.DoubleIn_ON.configure(fg=mainApp.Button_ft_color)
        mainApp.subWin.DoubleInModeONVar.set(0)
        mainApp.subWin.DoubleInModeOFFVar.set(1)

    if prevCommittedDounleInMode[0] != mainApp.DoubleInMode and selectedMode != prevCommittedMode[0]:
        mainApp.subWin.button_commitGameMode.config(state='normal')
    elif prevCommittedDounleInMode[0] != mainApp.DoubleInMode and selectedMode == prevCommittedMode[0]:
        mainApp.subWin.button_commitGameMode.config(state='normal')
    elif prevCommittedDounleInMode[0] == mainApp.DoubleInMode and selectedMode == prevCommittedMode[0]:
        mainApp.subWin.button_commitGameMode.config(state='disabled')

    return
