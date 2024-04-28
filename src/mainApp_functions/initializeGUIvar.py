"""Temporary method to store data; The variables are stored in "self" (i.e. mainApp).
Since all methods use the mainApp Object as an input/output, it is a lazy effective way to implement functionalities"""

def initializeGUIvar(mainApp):
    mainApp.softVersion = "ver 1.3"
    mainApp.colorTheme = "default"
    # Visual Stuff. These are used in the Populate GUI methods:
    if mainApp.colorTheme == "default":
        mainApp.Button_bg_color = "#245042"
        mainApp.Button_ft_color = "#D3DBE5"
        mainApp.activeButton_bg_color = "#9aa794"
        mainApp.activeButton_ft_color = "#D3DBE5"
        mainApp.disabledButton_ft_color = "#D3DBE5"
        mainApp.disabledButton_bg_color = "#245042"

    if mainApp.colorTheme == "Dark":
        mainApp.Button_bg_color = "#0a290a"
        mainApp.Button_ft_color = "#D3DBE5"
        mainApp.activeButton_bg_color = "#9aa794"
        mainApp.activeButton_ft_color = "#D3DBE5"

    # Variables  
    mainApp.p1_DoubleInVar = False
    mainApp.p2_DoubleInVar = False
    mainApp.p3_DoubleInVar = False
    mainApp.p4_DoubleInVar = False

    mainApp.gameStarted = False  # some methods (such as the log) act differently if the game is started.
    mainApp.playerIndex = [0, 0]  # Variable tracking player turn and total number of players.
                                # A quick variable to know who is playing
    mainApp.turnIndexLog = []  #
    mainApp.editScoreMode = False
    mainApp.editNameMode = False
    mainApp.currentGameTurn = 0
    mainApp.logIndex = 0

    mainApp.quitbuttonPressed = False

    return
