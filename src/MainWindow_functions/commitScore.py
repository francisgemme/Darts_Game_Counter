def commitScore(MainWindow):
    if MainWindow.editScoreMode == True:
        MainWindow.editScore()
        MainWindow.updateIndexLog()

    elif MainWindow.editScoreMode == False:
        scoreToInput = MainWindow.input_Score.get()
        if scoreToInput != '':
            MainWindow.writeCommitScore()
            MainWindow.updateIndexLog()
    return

