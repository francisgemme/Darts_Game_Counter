import initializeWindow as initWin, consoleSetup as cS

if __name__ == "__main__":

    """
    This .py initialize the "tkinter" GUI with all its functionalities.
    This version only has one Class object: the MainWindow Class. This Class contains all parameters (variables) and 
    methods required to handle the GUI. A future version of this code will contains subsequent classes such as Member,
    Game and League to manage data in a suitable matter.    
    """

    quitbuttonPressed = False

    while quitbuttonPressed == False:
            cS.consoleSetup()  # To display Logs into console (in the proper format)
            [root, mainWindow] = initWin.initializeWindow() # Initialize the window creation
            root.mainloop() # Created window is waiting for any action
            quitbuttonPressed = mainWindow.quitbuttonPressed # may be updated if user presses the Quit Button
            root.destroy()





