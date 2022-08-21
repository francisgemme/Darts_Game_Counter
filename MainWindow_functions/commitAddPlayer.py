from tkinter import *

def commitAddPlayer(MainWindow):
    playerName = MainWindow.subWin.input_Name.get()

    if playerName == "":
        MainWindow.subWin.errorStatus.configure(text="Vous devez entrer un nom... ")
        return

    if MainWindow.gameStarted == False:  # to do during the game setup, i.e., before starting.

        MainWindow.button_gameStart.configure(state="normal", fg="#60ff30")
        updateStatusLabeltext_1 = "Ajouter un deuxième joueur OU Cliquer Démarrer Partie!"
        updateStatusLabeltext_2 = "Ajouter un troisième joueur OU Cliquer Démarrer Partie!"
        updateStatusLabeltext_3 = "Ajouter un quatrième joueur OU Cliquer Démarrer Partie!"
        updateStatusLabeltext_4 = "Cliquer Démarrer Partie!"

        eval("MainWindow.player_" + str(MainWindow.nbPlayer + 1) + "_label_1.config(state=NORMAL)")
        eval("MainWindow.player_" + str(MainWindow.nbPlayer + 1) + "_label_1.delete(0, END)")
        eval("MainWindow.player_" + str(MainWindow.nbPlayer + 1) + "_label_1.insert(0, playerName)")
        eval("MainWindow.player_" + str(
            MainWindow.nbPlayer + 1) + "_label_1.config(state=DISABLED, disabledforeground='yellow')")
        eval("MainWindow.frame_player_" + str(MainWindow.nbPlayer + 1) + ".config(relief='raised')")

        MainWindow.nbPlayer += 1
        eval("MainWindow.updateStatusLabel(updateStatusLabeltext_" + str(MainWindow.nbPlayer) + ')'"")
        MainWindow.refreshImages()

    if MainWindow.gameStarted == True:  # to do if the editname mode has been pressed.
        currentPlayer = MainWindow.playerIndex[:1]
        eval("MainWindow.player_" + str(currentPlayer[0]) + "_label_1.config(state=NORMAL)")
        eval("MainWindow.player_" + str(currentPlayer[0]) + "_label_1.delete(0, END)")
        eval("MainWindow.player_" + str(currentPlayer[0]) + "_label_1.insert(0, playerName)")
        eval("MainWindow.player_" + str(currentPlayer[0]) + "_label_1.config(state=DISABLED)")
        MainWindow.button_commitScore.configure(state='disabled')
        MainWindow.button_editName.config(state='normal')

    MainWindow.destroySubWin()

    return
