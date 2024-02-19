from MainWindow_functions import MainWindow
from tkinter import *

def initializeWindow(Match_inst):

    # Call the tkinter tool
    tk_layer = Tk()
    # Call Constructor
    MainWindow_inst = MainWindow.MainWindow(tk_layer, Match_inst)

    return [tk_layer, MainWindow_inst]