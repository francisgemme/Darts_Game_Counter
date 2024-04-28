def commitGameMode(mainApp):

    selection = mainApp.subWin.mode_var.get()

    mainApp.CommitGameMode = eval("["+str(selection)+", mainApp.match_inst.doubleInMode]")

    print('Game Mode is now set:')
    print(mainApp.CommitGameMode)
    print(mainApp.match_inst.SelectedGameMode)

    mainApp.destroySubWin()

    return
