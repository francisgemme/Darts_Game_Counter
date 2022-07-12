from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Score Board")
root.geometry("1050x880")
#root.resizable(False, False)

root.iconbitmap("dart_icon.ico")
root.configure(background="#38404B")

# Create things!
# Create the label widget
#str_clickJoueurAjoute = Label(root, text='Entrer Nom du Joueur à Ajouter')
# myLabel2 = Label(root, text='My Name is Frank')
# myLabel3 = Label(root, text='My Name is John')
# myLabel4 = Label(root, text='My Name is Joce')


#def clickJoueurAjoute():
    # A class "Game" with its properties must be sent to this function
    # Transfer created player to the Lobby
 #   newPlayerName = Label(root, text=input_JoueurAjoute.get())
  #  newPlayerName.grid(row=4, column=6)

#--------------------------------------------------------------------------------------------------------------------
# Defining Global variable (temporary, pending classes creations)
#--------------------------------------------------------------------------------------------------------------------
global nbPlayer
nbPlayer = 0
global playerTurnIndex
playerTurnIndex = 0
global playerScores
playerScores = [0]

#--------------------------------------------------------------------------------------------------------------------
# Defining Functions
#--------------------------------------------------------------------------------------------------------------------
def button_click(number):
    # A class "Game" with its properties must be sent to this function
    # Transfer created player to the Lobby
    if nbPlayer != 0:
        current = input_Score.get()
        input_Score.delete(0,END)
        input_Score.insert(0, str(current) + str(number))
    return

def button_clear():
    # A class "Game" with its properties must be sent to this function
    # Transfer created player to the Lobby
    if nbPlayer != 0:
        input_Score.delete(0,END)
    return

def button_equal():
    # A class "Game" with its properties must be sent to this function
    # Must create a memory (by using a global variable)
    if nbPlayer != 0:
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

def button_addPlayer():
    # Transfer created player to the Lobby
    first_number = input_Score.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    input_Score.delete(0, END)

    return

def button_adjustWinSize():
    return

def updateStatus():
    if nbPlayer == 0:
        updateStatusLabel.insert(0,"hello")
    return


#--------------------------------------------------------------------------------------------------------------------
# CREATING FRAMES
#--------------------------------------------------------------------------------------------------------------------
# Add player button frame
frame0 = LabelFrame(root, padx=5, pady=5)
frame0.grid(row=0,column=0,columnspan=2,sticky="W")
frame0.configure(background="#38404B")

# To create horizontal space between frames (this area provide instructions & Game Status)
emptylabel0= Label(root, padx=25, pady=30)
emptylabel0.grid(row=1,column=1,columnspan=1)
emptylabel0.configure(background="#38404B")

# To create a vertical space between first column of frames
emptylabel_1= Label(root, padx=20, pady=5)
emptylabel_1.grid(row=2,column=0,rowspan=10)
emptylabel_1.configure(background="#38404B")

# To create a vertical space after first column of frames
emptylabel_2= Label(root, padx=20, pady=10)
emptylabel_2.grid(row=1,column=2,rowspan=10)
emptylabel_2.configure(background="#38404B")

# Calculator and submit button frame
frame1 = LabelFrame(root, padx=10, pady=10)
frame1.grid(row=4,column=1,columnspan=1,rowspan=3)
frame1.configure(background="#38404B")

# To create vertical space between frames
emptylabel_3= Label(root, padx=25, pady=2)
emptylabel_3.grid(row=3,column=1,columnspan=1)
emptylabel_3.configure(background="#38404B")

# Entry Score frame
frame2 = LabelFrame(root, padx=10, pady=10)
frame2.grid(row=2,column=1,columnspan=1)
frame2.configure(background="#38404B")

# first player frame
frame3 = LabelFrame(root, padx=10, pady=10)
frame3.grid(row=3,column=4,columnspan=1,rowspan=3)
frame3.configure(background="#38404B")

# Second player frame
frame4 = LabelFrame(root, padx=10, pady=10)
frame4.grid(row=3,column=5,columnspan=1,rowspan=3)
frame4.configure(background="#38404B")

# third player frame
frame5 = LabelFrame(root, padx=10, pady=10)
frame5.grid(row=5,column=4,columnspan=1,rowspan=3)
frame5.configure(background="#38404B")

# fourth player frame
frame6 = LabelFrame(root, padx=10, pady=10)
frame6.grid(row=5,column=5,columnspan=1,rowspan=3)
frame6.configure(background="#38404B")

# End turn button frame
frame7 = LabelFrame(root, padx=10, pady=5)
frame7.grid(row=7,column=1,columnspan=1)
frame7.configure(background="#38404B")


#--------------------------------------------------------------------------------------------------------------------
# CREATING BUTTONS
#--------------------------------------------------------------------------------------------------------------------

Button_bg_color = "#38404B"
Button_ft_color = "#D3DBE5"

# Define buttons
button_1 = Button(frame1, text="1", padx=40, pady =20, font=("Helvetica", 25), bg=Button_bg_color, fg=Button_ft_color,
                  command=lambda: button_click(1))
button_2 = Button(frame1, text="2", padx=40, pady =20, font=("Helvetica", 25), bg=Button_bg_color, fg=Button_ft_color,
                  command=lambda: button_click(2))
button_3 = Button(frame1, text="3", padx=40, pady =20, font=("Helvetica", 25), bg=Button_bg_color, fg=Button_ft_color,
                  command=lambda: button_click(3))
button_4 = Button(frame1, text="4", padx=40, pady =20, font=("Helvetica", 25), bg=Button_bg_color, fg=Button_ft_color,
                  command=lambda: button_click(4))
button_5 = Button(frame1, text="5", padx=40, pady =20, font=("Helvetica", 25), bg=Button_bg_color, fg=Button_ft_color,
                  command=lambda: button_click(5))
button_6 = Button(frame1, text="6", padx=40, pady =20, font=("Helvetica", 25), bg=Button_bg_color, fg=Button_ft_color,
                  command=lambda: button_click(6))
button_7 = Button(frame1, text="7", padx=40, pady =20, font=("Helvetica", 25), bg=Button_bg_color, fg=Button_ft_color,
                  command=lambda: button_click(7))
button_8 = Button(frame1, text="8", padx=40, pady =20, font=("Helvetica", 25), bg=Button_bg_color, fg=Button_ft_color,
                  command=lambda: button_click(8))
button_9 = Button(frame1, text="9", padx=40, pady =20, font=("Helvetica", 25), bg=Button_bg_color, fg=Button_ft_color,
                  command=lambda: button_click(9))
button_0 = Button(frame1, text="0", padx=40, pady =20, font=("Helvetica", 25), bg=Button_bg_color, fg=Button_ft_color,
                  command=lambda: button_click(0))

button_commitScore = Button(frame1, text="Soumettre", padx=100, pady =20, font=("Helvetica", 25), bg=Button_bg_color,
                            fg="yellow", command=button_equal)
button_clear = Button(frame1, text="C", padx=100, pady =20, font=("Helvetica", 25), bg=Button_bg_color,
                      fg=Button_ft_color, command=button_clear)

button_addPlayer = Button(frame0, text="Ajouter Joueur", padx=40, pady =5, font=("Helvetica", 12), bg=Button_bg_color,
                          fg=Button_ft_color, command=button_addPlayer)

button_endTurn = Button(frame7, text="Tour terminé", padx=40, pady =5, font=("Helvetica", 12), bg=Button_bg_color,
                        fg=Button_ft_color, command=button_addPlayer)

button_quit = Button(root, text="Exit Program", padx=40, pady =5, font=("Helvetica", 12), bg=Button_bg_color,
                     fg=Button_ft_color, command=root.quit)

# Put the buttons on the screen
button_1.grid(row=3 ,column=0)
button_2.grid(row=3 ,column=1)
button_3.grid(row=3 ,column=2)
button_4.grid(row=2 ,column=0)
button_5.grid(row=2 ,column=1)
button_6.grid(row=2 ,column=2)
button_7.grid(row=1 ,column=0)
button_8.grid(row=1 ,column=1)
button_9.grid(row=1 ,column=2)
button_0.grid(row=4 ,column=0)
button_commitScore.grid(row=5 ,column=0, columnspan=3)
button_clear.grid(row=4 ,column=1, columnspan=2)
button_addPlayer.grid(row=0 ,column=0,columnspan=1)
button_endTurn.grid(row=0 ,column=0,columnspan=1)
button_quit.grid(row=7 ,column=5,columnspan=1)

#--------------------------------------------------------------------------------------------------------------------
# CREATING ENTRY BOXES
#--------------------------------------------------------------------------------------------------------------------
# Create Entry box
input_Score = Entry(frame2, width=5, bg='black',fg='yellow', borderwidth=3, font=("Helvetica", 50),justify='center')
#Columnspan can hold other slots
input_Score.grid(row=0,column=2, columnspan=1)
#input_Score.insert(0, "Enter Name")

#--------------------------------------------------------------------------------------------------------------------
# CREATING STATUS
#--------------------------------------------------------------------------------------------------------------------
updateStatusLabel = Label(emptylabel0,padx=1, pady =20, text="Ajoutez le premier Joueur!",font=("Helvetica", 12),bg=Button_bg_color, fg="cyan")
updateStatusLabel.grid(row=0,column=0)

#--------------------------------------------------------------------------------------------------------------------
# PLAYER SCORES AND STATUS
#--------------------------------------------------------------------------------------------------------------------
player_1_label_1 = Label(frame3,padx=40, pady =20, text="Ajoutez le Joueur #1",font=("Helvetica", 12),bg=Button_bg_color, fg="grey")
player_1_label_1.grid(row=0,column=0)
player_1_label_2 = Label(frame3,padx=40, pady =20, text="501",font=("Helvetica", 30),bg=Button_bg_color, fg="grey")
player_1_label_2.grid(row=1,column=0)

player_2_label = Label(frame4,padx=40, pady =20, text="Ajoutez le Joueur #2",font=("Helvetica", 12),bg=Button_bg_color, fg="grey")
player_2_label.grid(row=0,column=0)
player_2_label_2 = Label(frame4,padx=40, pady =20, text="501",font=("Helvetica", 30),bg=Button_bg_color, fg="grey")
player_2_label_2.grid(row=1,column=0)

player_3_label = Label(frame5,padx=40, pady =20, text="Ajoutez le Joueur #3",font=("Helvetica", 12),bg=Button_bg_color, fg="grey")
player_3_label.grid(row=0,column=0)
player_3_label_2 = Label(frame5,padx=40, pady =20, text="501",font=("Helvetica", 30),bg=Button_bg_color, fg="grey")
player_3_label_2.grid(row=1,column=0)

player_4_label = Label(frame6,padx=40, pady =20, text="Ajoutez le Joueur #4",font=("Helvetica", 12),bg=Button_bg_color, fg="grey")
player_4_label.grid(row=0,column=0)
player_3_label_2 = Label(frame6,padx=40, pady =20, text="501",font=("Helvetica", 30),bg=Button_bg_color, fg="grey")
player_3_label_2.grid(row=1,column=0)

# The GUI is acting like a listening... Constantly waiting for something to happen.
root.mainloop()
