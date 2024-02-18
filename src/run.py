import initializeWindow as initWin, consoleSetup as cS

if __name__ == "__main__":
    """
    This .py initialize the "tkinter" GUI with all its functionalities.
    This version only has one Class object: the MainWindow Class. This Class contains all parameters (variables) and 
    methods required to handle the GUI. A future version of this code will contains subsequent classes such as Member,
    Game and League to manage data in a suitable matter.    
    """

    quitbuttonPressed = False

    def on_closing():
        root.destroy()
        exit()  # Will stop everything

    while quitbuttonPressed == False:
        cS.consoleSetup()  # To display Logs into console (in the proper format)
        [root, mainWindow] = initWin.initializeWindow()  # Initialize the window creation
        root.protocol("WM_DELETE_WINDOW", on_closing)  # if the user closes the Window. Skip the remaining lines if pressed (due to exit())
        root.mainloop()  # Window is waiting for any action
        quitbuttonPressed = mainWindow.quitbuttonPressed  # may be updated if user presses the Quit Button
        root.destroy() # Destroy everything, then repeat the loop.

