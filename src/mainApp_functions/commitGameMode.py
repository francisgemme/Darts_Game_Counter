def commitGameMode(mainApp):

    selection = mainApp.subWin.mode_var.get()

    mainApp.CommitGameMode = eval("["+str(selection)+", mainApp.DoubleInMode]")

    print('Game Mode is now set:')
    print(mainApp.CommitGameMode)
    print(mainApp.SelectedGameMode)

    mainApp.destroySubWin()

    return
