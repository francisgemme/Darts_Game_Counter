from tkinter import *

root = Tk()

# Personal notes for development;
# A class "League" (Parent) must be created to host Matches with Player. The League will be able to manage Player stats
# after many games.
# A class "Match" (child of ) must be created to use this GUI properly.
# A class "Lobby" is a temporary isolated entity that will be created. (to be confirm)
# classes "Players" (child of Match) will also be created to use this GUI properly.


# Create things!
# Create the label widget
str_clickJoueurAjoute = Label(root, text='Entrer Nom du Joueur à Ajouter')
# myLabel2 = Label(root, text='My Name is Frank')
# myLabel3 = Label(root, text='My Name is John')
# myLabel4 = Label(root, text='My Name is Joce')

# Second step, following the creation of the widget, we pack the label onto root. Shoving it onto the screen.
# .grid:  to position the label. The row number is a relative value.
str_clickJoueurAjoute.grid(row=2, column=0)
# myLabel2.grid(row=1, column=1)
# myLabel3.grid(row=2, column=0)
# myLabel4.grid(row=3, column=0)

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.grid(row=4, column=0)


def clickJoueurAjoute():
    # A class "Game" with its properties must be sent to this function
    # Transfer created player to the Lobby
    newPlayerName = Label(root, text=input_JoueurAjoute.get())
    newPlayerName.grid(row=4, column=6)


# Create a button
# padx and pady size the button.
myButton = Button(root, text='Ajouter Joueur', command=clickJoueurAjoute, fg="#288BA8", bg='#ffffff')
myButton.grid(row=3,column=1)

# padx and pady size the button.
myButton = Button(root, text='Commencer La Partie', command=myClick, fg="#288BA8", bg='#ffffff')
myButton.grid(row=4,column=1)


# Create Entry box
input_JoueurAjoute = Entry(root, width=50, bg='blue',fg='white', borderwidth=3)
input_JoueurAjoute.grid(row=2,column=1)
#input_JoueurAjoute.insert(0, "Enter Name")

# The GUI is acting like a listening... Constantly waiting for something to happen.
root.mainloop()
