from MainWindow_functions import MainWindow
from tkinter import *

def initializeWindow():

    # Call the tkinter tool
    root = Tk()
    # Call Constructor
    e = MainWindow.MainWindow(root)

    return [root, e]

