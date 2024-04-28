def commitScore(mainApp):
    if mainApp.match_inst.editScoreMode == True:
        mainApp.editScore()
        mainApp.updateIndexLog()

    elif mainApp.match_inst.editScoreMode == False:
        scoreToInput = mainApp.input_Score.get()
        if scoreToInput != '':
            mainApp.writeCommitScore()
            mainApp.updateIndexLog()
    return

