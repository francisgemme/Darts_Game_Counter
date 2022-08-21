from tkinter import *


def updateStatusLabel(MainWindow, text):
    MainWindow.StatusLabel.destroy()
    MainWindow.StatusLabel = Label(MainWindow.emptylabel0, padx=1, pady=20, text=text, font=("Helvetica", 12),
                                   bg=MainWindow.Button_bg_color, fg="cyan")
    MainWindow.StatusLabel.grid(row=0, column=0, columnspan=1)
    return
