def commitScore(mainApp):
    if mainApp.editScoreMode == True:
        mainApp.editScore()
        mainApp.updateIndexLog()

    elif mainApp.editScoreMode == False:
        scoreToInput = mainApp.input_Score.get()
        if scoreToInput != '':
            mainApp.writeCommitScore()
            mainApp.updateIndexLog()
    return

