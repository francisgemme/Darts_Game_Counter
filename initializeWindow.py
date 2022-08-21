from MainWindow_functions import MainWindow
from tkinter import *

def initializeWindow():

    # Call the tkinter tool
    root = Tk()
    # Call Constructor
    e = MainWindow.MainWindow(root)
    # The GUI is acting like a listening... Constantly waiting for something to happen.
    return [root, e]
