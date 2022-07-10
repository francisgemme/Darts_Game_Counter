from tkinter import *
from PIL import ImageTK, Image

root = Tk()
root.title("Score Board")
root.geometry("500x700")

root.iconbitmap("P:\Python_Projects\Darts\dart_icon.ico")

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.grid(row=7 ,column=2)

# Create things!
# Create the label widget
#str_clickJoueurAjoute = Label(root, text='Entrer Nom du Joueur à Ajouter')
# myLabel2 = Label(root, text='My Name is Frank')
# myLabel3 = Label(root, text='My Name is John')
# myLabel4 = Label(root, text='My Name is Joce')

# Second step, following the creation of the widget, we pack the label onto root. Shoving it onto the screen.
# .grid:  to position the label. The row number is a relative value.
#str_clickJoueurAjoute.grid(row=2, column=0)
# myLabel2.grid(row=1, column=1)
# myLabel3.grid(row=2, column=0)
# myLabel4.grid(row=3, column=0)

#def myClick():
 #   myLabel = Label(root, text="Look! I clicked a Button!!")
 #   myLabel.grid(row=4, column=0)


#def clickJoueurAjoute():
    # A class "Game" with its properties must be sent to this function
    # Transfer created player to the Lobby
 #   newPlayerName = Label(root, text=input_JoueurAjoute.get())
  #  newPlayerName.grid(row=4, column=6)

def button_click(number):
    # A class "Game" with its properties must be sent to this function
    # Transfer created player to the Lobby
    current = input_Score.get()
    input_Score.delete(0,END)
    input_Score.insert(0, str(current) + str(number))
    return

def button_clear():
    # A class "Game" with its properties must be sent to this function
    # Transfer created player to the Lobby
    input_Score.delete(0,END)
    return

def button_add():
    # A class "Game" with its properties must be sent to this function
    # Must create a memory (by using a global variable)
    first_number = input_Score.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    input_Score.delete(0, END)
    return

def button_equal():
    # A class "Game" with its properties must be sent to this function
    # Must create a memory (by using a global variable)
    next_number = input_Score.get()
    input_Score.delete(0, END)

    if math == "addition":
        input_Score.insert(0, f_num + int(next_number))
    if math == "substraction":
        input_Score.insert(0, f_num - int(next_number))
    if math == "multiplication":
        input_Score.insert(0, f_num * int(next_number))
    if math == "division":
        input_Score.insert(0, f_num / int(next_number))

    return

def button_substract():
    # A class "Game" with its properties must be sent to this function
    # Transfer created player to the Lobby
    first_number = input_Score.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(first_number)
    input_Score.delete(0, END)
    return

def button_multiply():
    # A class "Game" with its properties must be sent to this function
    # Transfer created player to the Lobby
    first_number = input_Score.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    input_Score.delete(0, END)
    return

def button_divide():
    # A class "Game" with its properties must be sent to this function
    # Transfer created player to the Lobby
    first_number = input_Score.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    input_Score.delete(0, END)
    return


# Create buttons
# padx and pady size the button.
#myButton = Button(root, text='Ajouter Joueur', command=clickJoueurAjoute, fg="#288BA8", bg='#ffffff')
#myButton.grid(row=3,column=1)

# padx and pady size the button.
#myButton = Button(root, text='Commencer La Partie', command=myClick, fg="#288BA8", bg='#ffffff')
#myButton.grid(row=4,column=1)

# Define buttons
button_1 = Button(root, text="1", padx=40, pady =20, font=("Helvetica", 25), command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady =20, font=("Helvetica", 25), command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady =20, font=("Helvetica", 25), command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady =20, font=("Helvetica", 25), command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady =20, font=("Helvetica", 25), command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady =20, font=("Helvetica", 25), command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady =20, font=("Helvetica", 25), command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady =20, font=("Helvetica", 25), command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady =20, font=("Helvetica", 25), command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady =20, font=("Helvetica", 25), command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady =20, font=("Helvetica", 25), command=button_add)
button_equal = Button(root, text="=", padx=110, pady =20, font=("Helvetica", 25), command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady =20, font=("Helvetica", 25), command=button_clear)

button_substract = Button(root, text="-", padx=40, pady =20, font=("Helvetica", 25), command=button_substract)
button_multiply = Button(root, text="*", padx=40, pady =20, font=("Helvetica", 25), command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady =20, font=("Helvetica", 25), command=button_divide)

# Put the buttons on the screen

button_1.grid(row=3 ,column=0 )
button_2.grid(row=3 ,column=1 )
button_3.grid(row=3 ,column=2 )

button_4.grid(row=2 ,column=0 )
button_5.grid(row=2 ,column=1 )
button_6.grid(row=2 ,column=2 )

button_7.grid(row=1 ,column=0)
button_8.grid(row=1 ,column=1)
button_9.grid(row=1 ,column=2)

button_0.grid(row=4 ,column=0 )

button_add.grid(row=5 ,column=0)
button_equal.grid(row=5 ,column=1, columnspan=2)
button_clear.grid(row=4 ,column=1,columnspan=2)

button_substract.grid(row=6 ,column=0)
button_multiply.grid(row=6 ,column=1, columnspan=1)
button_divide.grid(row=6 ,column=2,columnspan=1)



# Create Entry box
input_Score = Entry(root, width=50, bg='blue',fg='white', borderwidth=5, font=("Helvetica", 25))
#Columnspan can hold other slots
input_Score.grid(row=0,column=0, columnspan=20)
#input_Score.insert(0, "Enter Name")

# The GUI is acting like a listening... Constantly waiting for something to happen.
root.mainloop()
