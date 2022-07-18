from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Score Board")
root.geometry("1050x880")
#root.resizable(False, False)
root.iconbitmap("dart_icon.ico")
root.configure(background="#38404B")

class MainWindow:

    def __init__(self, master):

        self.nbPlayer = 1
        self.Button_bg_color = "#38404B"
        self.Button_ft_color = "#D3DBE5"

        # Add player button frame
        self.frame0 = LabelFrame(master, padx=5, pady=5)
        self.frame0.grid(row=0,column=0,columnspan=2,sticky="W")
        self.frame0.configure(background="#38404B")

        # To create horizontal space between frames (this area provide instructions & Game Status)
        self.emptylabel0= Label(master, padx=25, pady=30)
        self.emptylabel0.grid(row=1,column=1,columnspan=1)
        self.emptylabel0.configure(background="#38404B")

        # To create a vertical space between first column of frames
        self.emptylabel_1= Label(master, padx=20, pady=5)
        self.emptylabel_1.grid(row=2,column=0,rowspan=10)
        self.emptylabel_1.configure(background="#38404B")

        # To create a vertical space after first column of frames
        self.emptylabel_2= Label(master, padx=20, pady=10)
        self.emptylabel_2.grid(row=1,column=2,rowspan=10)
        self.emptylabel_2.configure(background="#38404B")

        # Calculator and submit button frame
        self.frame1 = LabelFrame(master, padx=10, pady=10)
        self.frame1.grid(row=4,column=1,columnspan=1,rowspan=3)
        self.frame1.configure(background="#38404B")

        # To create vertical space between frames
        self.emptylabel_3= Label(master, padx=25, pady=2)
        self.emptylabel_3.grid(row=3,column=1,columnspan=1)
        self.emptylabel_3.configure(background="#38404B")

        # Entry Score frame
        self.frame2 = LabelFrame(master, padx=10, pady=10)
        self.frame2.grid(row=2,column=1,columnspan=1)
        self.frame2.configure(background="#38404B")

        # first player frame
        self.frame3 = LabelFrame(master, padx=10, pady=10)
        self.frame3.grid(row=3,column=4,columnspan=1,rowspan=3)
        self.frame3.configure(background="#38404B")

        # Second player frame
        self.frame4 = LabelFrame(master, padx=10, pady=10)
        self.frame4.grid(row=3,column=5,columnspan=1,rowspan=3)
        self.frame4.configure(background="#38404B")

        # third player frame
        self.frame5 = LabelFrame(master, padx=10, pady=10)
        self.frame5.grid(row=5,column=4,columnspan=1,rowspan=3)
        self.frame5.configure(background="#38404B")

        # fourth player frame
        self.frame6 = LabelFrame(master, padx=10, pady=10)
        self.frame6.grid(row=5,column=5,columnspan=1,rowspan=3)
        self.frame6.configure(background="#38404B")

        # End turn button frame
        self.frame7 = LabelFrame(master, padx=10, pady=5)
        self.frame7.grid(row=7,column=1,columnspan=1)
        self.frame7.configure(background="#38404B")

        #---------------------------------------------------------------------------------------------------------------
        # CREATING BUTTONS
        #---------------------------------------------------------------------------------------------------------------

        # Define buttons
        self.button_1 = Button(self.frame1,
                               text="1",
                               padx=40, pady =20,
                               font=("Helvetica", 25),
                               bg=self.Button_bg_color,
                               fg=self.Button_ft_color,
                               command=lambda: self.button_click(1))
        self.button_2 = Button(self.frame1,
                               text="2",
                               padx=40, pady =20,
                               font=("Helvetica", 25),
                               bg=self.Button_bg_color,
                               fg=self.Button_ft_color,
                               command=lambda: self.button_click(2))

        self.button_3 = Button(self.frame1, text="3", padx=40, pady =20, font=("Helvetica", 25), bg=self.Button_bg_color, fg=self.Button_ft_color,
                  command=lambda: self.button_click(3))
        self.button_4 = Button(self.frame1, text="4", padx=40, pady =20, font=("Helvetica", 25), bg=self.Button_bg_color, fg=self.Button_ft_color,
                  command=lambda: self.button_click(4))
        self.button_5 = Button(self.frame1, text="5", padx=40, pady =20, font=("Helvetica", 25), bg=self.Button_bg_color, fg=self.Button_ft_color,
                  command=lambda: self.button_click(5))
        self.button_6 = Button(self.frame1, text="6", padx=40, pady =20, font=("Helvetica", 25), bg=self.Button_bg_color, fg=self.Button_ft_color,
                  command=lambda: self.button_click(6))
        self.button_7 = Button(self.frame1, text="7", padx=40, pady =20, font=("Helvetica", 25), bg=self.Button_bg_color, fg=self.Button_ft_color,
                  command=lambda: self.button_click(7))
        self.button_8 = Button(self.frame1, text="8", padx=40, pady =20, font=("Helvetica", 25), bg=self.Button_bg_color, fg=self.Button_ft_color,
                  command=lambda: self.button_click(8))
        self.button_9 = Button(self.frame1, text="9", padx=40, pady =20, font=("Helvetica", 25), bg=self.Button_bg_color, fg=self.Button_ft_color,
                  command=lambda: self.button_click(9))
        self.button_0 = Button(self.frame1, text="0", padx=40, pady =20, font=("Helvetica", 25), bg=self.Button_bg_color, fg=self.Button_ft_color,
                  command=lambda: self.button_click(0))

        self.button_commitScore = Button(self.frame1, text="Soumettre", padx=100, pady =20, font=("Helvetica", 25), bg=self.Button_bg_color,
                            fg="yellow", command=self.button_commitScore)
        self.button_clear = Button(self.frame1, text="C", padx=100, pady =20, font=("Helvetica", 25), bg=self.Button_bg_color,
                      fg=self.Button_ft_color, command=self.button_clear)

        self.button_addPlayer = Button(self.frame0, text="Ajouter Joueur", padx=40, pady =5, font=("Helvetica", 12), bg=self.Button_bg_color,
                          fg=self.Button_ft_color, command=self.button_addPlayer)

        self.button_endTurn = Button(self.frame7, text="Tour terminé", padx=40, pady =5, font=("Helvetica", 12), bg=self.Button_bg_color,
                        fg=self.Button_ft_color, command=self.button_addPlayer)

        self.button_quit = Button(master, text="Exit Program", padx=40, pady =5, font=("Helvetica", 12), bg=self.Button_bg_color,
                     fg=self.Button_ft_color, command=master.quit)

        # Put the buttons on the screen
        self.button_1.grid(row=3 ,column=0)
        self.button_2.grid(row=3 ,column=1)
        self.button_3.grid(row=3 ,column=2)
        self.button_4.grid(row=2 ,column=0)
        self.button_5.grid(row=2 ,column=1)
        self.button_6.grid(row=2 ,column=2)
        self.button_7.grid(row=1 ,column=0)
        self.button_8.grid(row=1 ,column=1)
        self.button_9.grid(row=1 ,column=2)
        self.button_0.grid(row=4 ,column=0)
        self.button_commitScore.grid(row=5 ,column=0, columnspan=3)
        self.button_clear.grid(row=4 ,column=1, columnspan=2)
        self.button_addPlayer.grid(row=0 ,column=0,columnspan=1)
        self.button_endTurn.grid(row=0 ,column=0,columnspan=1)
        self.button_quit.grid(row=7 ,column=5,columnspan=1)

        #---------------------------------------------------------------------------------------------------------------
        # CREATING ENTRY BOXES
        #---------------------------------------------------------------------------------------------------------------
        # Create Entry box
        self.input_Score = Entry(self.frame2,
                                 width=5,
                                 bg='black',
                                 fg='yellow',
                                 borderwidth=3,
                                 font=("Helvetica", 50),
                                 justify='center',
                                 disabledbackground='black',
                                 disabledforeground="yellow")

        #Columnspan can hold other slots
        self.input_Score.grid(row=0,column=2, columnspan=1)
        self.input_Score.config(state=DISABLED)
        #input_Score.insert(0, "Enter Name")

        #---------------------------------------------------------------------------------------------------------------
        # CREATING STATUS
        #---------------------------------------------------------------------------------------------------------------
        self.updateStatusLabel = Label(self.emptylabel0,padx=1, pady =20, text="Ajoutez au moins un Joueur!",font=("Helvetica", 12),bg=self.Button_bg_color, fg="cyan")
        self.updateStatusLabel.grid(row=0,column=0)

        self.player_1_label_1 = Label(self.frame3,padx=40, pady =20, text="Ajoutez le Joueur #1",font=("Helvetica", 12),bg=self.Button_bg_color, fg="grey")
        self.player_1_label_1.grid(row=0,column=0)
        self.player_1_label_2 = Label(self.frame3,padx=40, pady =20, text="501",font=("Helvetica", 30),bg=self.Button_bg_color, fg="grey")
        self.player_1_label_2.grid(row=1,column=0)

        self.player_2_label_1 = Label(self.frame4,padx=40, pady =20, text="Ajoutez le Joueur #2",font=("Helvetica", 12),bg=self.Button_bg_color, fg="grey")
        self.player_2_label_1.grid(row=0,column=0)
        self.player_2_label_2 = Label(self.frame4,padx=40, pady =20, text="501",font=("Helvetica", 30),bg=self.Button_bg_color, fg="grey")
        self.player_2_label_2.grid(row=1,column=0)

        self.player_3_label_1 = Label(self.frame5,padx=40, pady =20, text="Ajoutez le Joueur #3",font=("Helvetica", 12),bg=self.Button_bg_color, fg="grey")
        self.player_3_label_1.grid(row=0,column=0)
        self.player_3_label_2 = Label(self.frame5,padx=40, pady =20, text="501",font=("Helvetica", 30),bg=self.Button_bg_color, fg="grey")
        self.player_3_label_2.grid(row=1,column=0)

        self.player_4_label_1 = Label(self.frame6,padx=40, pady =20, text="Ajoutez le Joueur #4",font=("Helvetica", 12),bg=self.Button_bg_color, fg="grey")
        self.player_4_label_1.grid(row=0,column=0)
        self.player_4_label_2 = Label(self.frame6,padx=40, pady =20, text="501",font=("Helvetica", 30),bg=self.Button_bg_color, fg="grey")
        self.player_4_label_2.grid(row=1,column=0)


    def button_click(self,number):
        # A class "Game" with its properties must be sent to this function
        # Transfer created player to the Lobby
        if self.nbPlayer != 0:

            current = self.input_Score.get()

            if len(current) < 3:
                self.input_Score.config(state=NORMAL)
                self.input_Score.delete(0,END)
                self.input_Score.insert(0, str(current) + str(number))
                self.input_Score.config(state=DISABLED)
        return

    def button_clear(self):
          # A class "Game" with its properties must be sent to this function
        # Transfer created player to the Lobby
        if self.nbPlayer != 0:
          self.input_Score.delete(0,END)
        return

    def button_commitScore(self):
        # A class "Game" with its properties must be sent to this function
        # Must create a memory (by using a global variable)
            if self.nbPlayer != 0:
                next_number = self.input_Score.get()
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

    def button_addPlayer(self):
        # Transfer created player to the Lobby

        self.subWin = Tk()
        self.subWin.wm_title("Ajouter Joueur #%s" % self.nbPlayer)
        self.subWin.configure(background=self.Button_bg_color)
        self.subWin.resizable(False, False)
        l = Label(self.subWin, text="Entrer le Nom du Joueur #%s" % self.nbPlayer,bg=self.Button_bg_color,fg=self.Button_ft_color)
        l.grid(row=0,column=0, columnspan=1, padx=50, pady=50)
        self.subWin.input_Name = Entry(self.subWin, width=20, bg='black',fg='yellow', borderwidth=3, font=("Helvetica", 12),justify='center')
        #Columnspan can hold other slots
        self.subWin.input_Name.grid(row=0,column=1, columnspan=1)
         #input_Score.insert(0, "Enter Name")

        self.subWin.button_commitAddPlayer= Button(self.subWin, text="Enregistrer", padx=10, pady =10, font=("Helvetica", 12), bg=self.Button_bg_color,
                            fg="yellow", command=self.commitAddPlayer)
        self.subWin.button_cancel = Button(self.subWin, text="Annuler", padx=10, pady =10, font=("Helvetica", 12), bg=self.Button_bg_color,
                      fg=self.Button_ft_color, command=self.subWin.destroy)

        self.subWin.button_commitAddPlayer.grid(row=1 ,column=1, columnspan=1)
        self.subWin.button_cancel.grid(row=1 ,column=0, columnspan=1)

        return(self)

    def commitAddPlayer(self):
        # A class "Game" with its properties must be sent to this function
        # Transfer created player to the Lobby
        print('yo gros big')
        playerName= self.subWin.input_Name.get()
        print(self.nbPlayer)

        if self.nbPlayer != 0:
            if self.nbPlayer == 1:
                self.player_1_label_1.configure(text=playerName,fg='yellow')
                self.player_1_label_2.configure(padx=40, pady =20, text="501",font=("Helvetica", 30), fg="yellow")
                self.frame3.configure(relief='raised', borderwidth=5, padx=40, pady=10)
                self.updateStatusLabel.configure(text="Ajouter un autre joueur OU Cliquer Démarrer!")

            if self.nbPlayer == 2:
                self.player_2_label_1.configure(text=playerName,fg='yellow')
                self.player_2_label_2.configure(padx=40, pady =20, text="501",font=("Helvetica", 30), fg="yellow")
                self.frame4.configure(relief='raised', borderwidth=5, padx=40, pady=10)

            if self.nbPlayer == 3:
                self.player_3_label_1.configure(text=playerName,fg='yellow')
                self.player_3_label_2.configure(padx=40, pady =20, text="501",font=("Helvetica", 30), fg="yellow")
                self.frame5.configure(relief='raised', borderwidth=5, padx=40, pady=10)

            if self.nbPlayer == 4:
                self.player_4_label_1.configure(text=playerName,fg='yellow')
                self.player_4_label_2.configure(padx=40, pady =20, text="501",font=("Helvetica", 30), fg="yellow")
                self.frame6.configure(relief='raised', borderwidth=5, padx=40, pady=10)
                self.updateStatusLabel.configure(text="Cliquer Démarrer la Partie!")

        self.nbPlayer += 1
        self.subWin.destroy()

        return(self)




e = MainWindow(root)
# The GUI is acting like a listening... Constantly waiting for something to happen.
root.mainloop()
