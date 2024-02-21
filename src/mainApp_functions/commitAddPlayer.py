from tkinter import *

def commitAddPlayer(mainApp):
    playerName = mainApp.subWin.input_Name.get()

    if playerName == "":
        mainApp.subWin.errorStatus.configure(text="Vous devez entrer un nom... ")
        return

    if mainApp.gameStarted == False:  # to do during the game setup, i.e., before starting.

        mainApp.button_gameStart.configure(state="normal", fg="#60ff30")
        updateStatusLabeltext_1 = "Ajouter un deuxième joueur OU Cliquer Démarrer Partie!"
        updateStatusLabeltext_2 = "Ajouter un troisième joueur OU Cliquer Démarrer Partie!"
        updateStatusLabeltext_3 = "Ajouter un quatrième joueur OU Cliquer Démarrer Partie!"
        updateStatusLabeltext_4 = "Cliquer Démarrer Partie!"

        eval("mainApp.player_" + str(mainApp.nbPlayer + 1) + "_label_1.config(state=NORMAL)")
        eval("mainApp.player_" + str(mainApp.nbPlayer + 1) + "_label_1.delete(0, END)")
        eval("mainApp.player_" + str(mainApp.nbPlayer + 1) + "_label_1.insert(0, playerName)")
        eval("mainApp.player_" + str(mainApp.nbPlayer + 1) + "_label_1.config(state=DISABLED, disabledforeground='yellow')")
        eval("mainApp.frame_player_" + str(mainApp.nbPlayer + 1) + ".config(relief='raised')")

        mainApp.nbPlayer += 1
        eval("mainApp.updateStatusLabel(updateStatusLabeltext_" + str(mainApp.nbPlayer) + ')'"")
        mainApp.refreshImages()

    if mainApp.gameStarted == True:  # to do if the editname mode has been pressed.
        currentPlayer = mainApp.playerIndex[:1]
        eval("mainApp.player_" + str(currentPlayer[0]) + "_label_1.config(state=NORMAL)")
        eval("mainApp.player_" + str(currentPlayer[0]) + "_label_1.delete(0, END)")
        eval("mainApp.player_" + str(currentPlayer[0]) + "_label_1.insert(0, playerName)")
        eval("mainApp.player_" + str(currentPlayer[0]) + "_label_1.config(state=DISABLED)")
        mainApp.button_commitScore.configure(state='disabled')
        mainApp.button_editName.config(state='normal')

    mainApp.destroySubWin()

    return
