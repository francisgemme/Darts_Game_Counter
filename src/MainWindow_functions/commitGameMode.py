def commitGameMode(MainWindow):

    selection = MainWindow.subWin.mode_var.get()

    MainWindow.CommitGameMode = eval("["+str(selection)+", MainWindow.DoubleInMode]")

    print('Game Mode is now set:')
    print(MainWindow.CommitGameMode)
    print(MainWindow.SelectedGameMode)

    MainWindow.destroySubWin()

    return
