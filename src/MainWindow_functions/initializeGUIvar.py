"""Temporary method to store data; The variables are stored in "self" (i.e. Mainwindow).
Since all methods use the MainWindow Object as an input/output, it is a lazy effective way to implement functionalities"""

def initializeGUIvar(MainWindow):
    MainWindow.softVersion = "ver 1.3"
    MainWindow.colorTheme = "default"
    # Visual Stuff. These are used in the Populate GUI methods:
    if MainWindow.colorTheme == "default":
        MainWindow.Button_bg_color = "#245042"
        MainWindow.Button_ft_color = "#D3DBE5"
        MainWindow.activeButton_bg_color = "#9aa794"
        MainWindow.activeButton_ft_color = "#D3DBE5"
        MainWindow.disabledButton_ft_color = "#D3DBE5"
        MainWindow.disabledButton_bg_color = "#245042"


    if MainWindow.colorTheme == "Dark":
        MainWindow.Button_bg_color = "#0a290a"
        MainWindow.Button_ft_color = "#D3DBE5"
        MainWindow.activeButton_bg_color = "#9aa794"
        MainWindow.activeButton_ft_color = "#D3DBE5"

    # Variables
    MainWindow.nbPlayer = 0

    MainWindow.p1_DoubleInVar = False # Selected Game Mode
    MainWindow.p2_DoubleInVar = False # Selected Game Mode
    MainWindow.p3_DoubleInVar = False # Selected Game Mode
    MainWindow.p4_DoubleInVar = False # Selected Game Mode


    MainWindow.SelectedGameMode = [] # Selected Game Mode
    MainWindow.prevSelMode = 1 # temporary
    MainWindow.DoubleInMode = True
    MainWindow.DoubleOutMode = False
    MainWindow.CommitGameMode = [1, MainWindow.DoubleInMode]  # Commit Game Mode
    MainWindow.gameStarted = False  # some methods (such as the log) act differently if the game is started.
    MainWindow.playerIndex = [0, 0]  # Variable tracking player turn and total number of players.
                                # A quick variable to know who is playing
    MainWindow.turnIndexLog = []  #
    MainWindow.editScoreMode = False
    MainWindow.editNameMode = False
    MainWindow.currentGameTurn = 0
    MainWindow.logIndex = 0
    MainWindow.doubleInMode = True

    MainWindow.quitbuttonPressed = False

    return
