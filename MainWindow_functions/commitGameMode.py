
def commitGameMode(MainWindow):

    #MainWindow.populateGMode(MainWindow.SelectedGameMode)
    MainWindow.commitedGameMode = MainWindow.SelectedGameMode
    print('Game Mode is now set')
    MainWindow.destroySubWin()

    return
