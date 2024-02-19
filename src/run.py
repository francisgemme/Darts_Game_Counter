from tkinter import *
from classes import Match
import initializeWindow as initWin, consoleSetup as cS

if __name__ == "__main__":
    """
    This .py initialize the "tkinter" GUI with all its functionalities.
    This version only has one Class object: the MainWindow Class. This Class contains all parameters (variables) and 
    methods required to handle the GUI. A future version of this code will contains subsequent classes such as Member,
    Game and League to manage data in a suitable matter.    
    """

    # Initiates the match object
    Match_inst = Match.initMatch()

    quitbuttonPressed = False

    def on_closing():
        tk_layer.destroy()
        exit()  # Will stop everything

    while quitbuttonPressed == False:
        cS.consoleSetup()  # To display Logs into console (in the proper format)
        [tk_layer, MainWindow_inst] = initWin.initializeWindow(Match_inst)  # Initialize the window creation
        tk_layer.protocol("WM_DELETE_WINDOW", on_closing)  # if the user closes the Window. Skip the remaining lines if pressed (due to exit())
        tk_layer.mainloop()  # Window is waiting for any action
        quitbuttonPressed = MainWindow_inst.quitbuttonPressed  # may be updated if user presses the Quit Button
        tk_layer.destroy() # Destroy everything, then repeat the loop.