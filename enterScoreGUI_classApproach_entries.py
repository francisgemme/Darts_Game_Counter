from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Score Board")
root.geometry("1125x850")
root.resizable(False, False)
root.iconbitmap("dart_icon.ico")
root.configure(background="#245042")
##38404B"

class MainWindow:

    def __init__(self, master):

        self.softVersion= "ver 0.x"
        self.nbPlayer = 0
        self.Button_bg_color = "#245042"
        self.Button_ft_color = "#D3DBE5"
        self.gameStarted = False
        self.playerIndex = []  #

        # Add player button frame
        self.frame0 = LabelFrame(master, padx=5, pady=5, bg=self.Button_bg_color)
        self.frame0.grid(row=0,column=0,columnspan=7,sticky="W")

        # To create horizontal space between frames (this area provide instructions & Game Status)
        self.emptylabel0= Label(master, padx=25, pady=30, bg= self.Button_bg_color)
        self.emptylabel0.grid(row=2,column=1,columnspan=3)

        # To create a vertical space between first column of frames
        self.emptylabel_1= Label(master, padx=20, pady=5, bg= self.Button_bg_color)
        self.emptylabel_1.grid(row=2,column=0,rowspan=14)

        # Calculator and submit button frame
        self.frame1 = LabelFrame(master, padx=10, pady=10, bg= self.Button_bg_color)
        self.frame1.grid(row=5,column=1,columnspan=3,rowspan=5)

        # To create a vertical space after first column of frames
        self.emptylabel_2= Label(master, padx=20, pady=10, bg= self.Button_bg_color)
        self.emptylabel_2.grid(row=5,column=4,rowspan=2)

        # To create vertical space between frames
        self.emptylabel_3= Label(master, padx=25, pady=2,bg= self.Button_bg_color)
        self.emptylabel_3.grid(row=0,column=10,columnspan=5,rowspan=5)

        # Entry Score frame
        self.frame2 = LabelFrame(master, padx=10, pady=10, bg= self.Button_bg_color)
        self.frame2.grid(row=3,column=1,columnspan=3)

        # Start Game button frame
        self.frame9 = LabelFrame(master, padx=10, pady=10, bg= self.Button_bg_color)
        self.frame9.grid(row=3,column=5,columnspan=2,rowspan=1)

       # Turn arrow panel
        self.emptylabel_4= Label(master, padx=10, pady=0,bg= self.Button_bg_color)
        self.emptylabel_4.grid(row=4,column=5,rowspan=2, columnspan=3)

        self.emptylabel_5= Label(master, padx=10, pady=0, bg= self.Button_bg_color)
        self.emptylabel_5.grid(row=4,column=9,rowspan=2, columnspan=4)

        self.emptylabel_6= Label(master, padx=10, pady=0, bg=self.Button_bg_color)
        self.emptylabel_6.grid(row=7,column=5,rowspan=2, columnspan=3)

        self.emptylabel_7= Label(master, padx=10, pady=0, bg=self.Button_bg_color)
        self.emptylabel_7.grid(row=7,column=9,rowspan=2, columnspan=4)

        # Empty Row between players 1-2 and player 3-4
        self.frame8 = LabelFrame(master, padx=10, pady=1, bg=self.Button_bg_color)
        self.frame8.grid(row=5,column=8,columnspan=3,rowspan=3)

        # End turn button frame
        self.frame7 = LabelFrame(master, padx=10, pady=5, bg=self.Button_bg_color)
        self.frame7.grid(row=13,column=2,columnspan=1)

        # first player frame
        self.frame3 = LabelFrame(master, padx=30, pady=30, bg=self.Button_bg_color)
        self.frame3.grid(row=5,column=5,columnspan=4,rowspan=3)

        # Second player frame
        self.frame4 = LabelFrame(master, padx=30, pady=30,bg=self.Button_bg_color)
        self.frame4.grid(row=5,column=9,columnspan=4,rowspan=3)

        # third player frame
        self.frame5 = LabelFrame(master, padx=30, pady=30, background=self.Button_bg_color)
        self.frame5.grid(row=8,column=5,columnspan=4,rowspan=3)

        # fourth player frame
        self.frame6 = LabelFrame(master, padx=30, pady=30, bg=self.Button_bg_color)
        self.frame6.grid(row=8,column=9,columnspan=4,rowspan=3)

        #---------------------------------------------------------------------------------------------------------------
        #                                               CREATING BUTTONS
        #---------------------------------------------------------------------------------------------------------------

        # Define buttons
        self.button_1 = Button(self.frame1, text="1", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                               fg=self.Button_ft_color, command=lambda: self.function_click(1))
        self.button_2 = Button(self.frame1, text="2", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                               fg=self.Button_ft_color, command=lambda: self.function_click(2))
        self.button_3 = Button(self.frame1, text="3", padx=40, pady =20, font=("Helvetica", 25),
                               bg=self.Button_bg_color, fg=self.Button_ft_color, command=lambda: self.function_click(3))
        self.button_4 = Button(self.frame1, text="4", padx=40, pady =20, font=("Helvetica", 25),
                               bg=self.Button_bg_color, fg=self.Button_ft_color, command=lambda: self.function_click(4))
        self.button_5 = Button(self.frame1, text="5", padx=40, pady =20, font=("Helvetica", 25),
                               bg=self.Button_bg_color, fg=self.Button_ft_color, command=lambda: self.function_click(5))
        self.button_6 = Button(self.frame1, text="6", padx=40, pady =20, font=("Helvetica", 25),
                               bg=self.Button_bg_color, fg=self.Button_ft_color, command=lambda: self.function_click(6))
        self.button_7 = Button(self.frame1, text="7", padx=40, pady =20, font=("Helvetica", 25),
                               bg=self.Button_bg_color, fg=self.Button_ft_color, command=lambda: self.function_click(7))
        self.button_8 = Button(self.frame1, text="8", padx=40, pady =20, font=("Helvetica", 25),
                               bg=self.Button_bg_color, fg=self.Button_ft_color, command=lambda: self.function_click(8))
        self.button_9 = Button(self.frame1, text="9", padx=40, pady =20, font=("Helvetica", 25),
                               bg=self.Button_bg_color, fg=self.Button_ft_color, command=lambda: self.function_click(9))
        self.button_0 = Button(self.frame1, text="0", padx=40, pady =20, font=("Helvetica", 25),
                               bg=self.Button_bg_color, fg=self.Button_ft_color, command=lambda: self.function_click(0))

        self.button_commitScore = Button(self.frame1, text="Soumettre", padx=100, pady =20, font=("Helvetica", 25),
                                         bg=self.Button_bg_color, fg="yellow", command=self.button_commitScore)
        self.button_clear = Button(self.frame1, text="C", padx=99.49999, pady =20, font=("Helvetica", 25),
                                   bg=self.Button_bg_color, fg=self.Button_ft_color, command=self.function_clear)

        self.button_addPlayer = Button(self.frame0, text="Ajouter Joueur", padx=35, pady =3, font=("Helvetica", 12),
                                       bg=self.Button_bg_color, fg=self.Button_ft_color, command=self.function_addPlayer)

        self.button_gameMode = Button(self.frame0, text="Mode de Jeu", padx=35, pady =3, font=("Helvetica", 12),
                                       bg=self.Button_bg_color, fg=self.Button_ft_color, state=DISABLED)

        self.button_editScore = Button(self.frame0, text="Modifier Pointage", padx=20, pady=3, font=("Helvetica", 12),
                                       bg=self.Button_bg_color, fg=self.Button_ft_color, state=DISABLED)

        self.button_editName = Button(self.frame0, text="Renommer Joueur", padx=20, pady=3, font=("Helvetica", 12),
                                       bg=self.Button_bg_color, fg=self.Button_ft_color, state=DISABLED)

        self.button_gameStart = Button(self.frame9, text="Démarrer Partie!", padx=40, pady =5, font=("Helvetica", 12),
                                       bg=self.Button_bg_color, fg=self.Button_ft_color,
                                       command=self.function_gameStart,state="disabled")

        self.button_endTurn = Button(self.frame7, text="Tour terminé", padx=40, pady =5, font=("Helvetica", 12),
                                     bg=self.Button_bg_color, fg=self.Button_ft_color,
                                     command=self.function_endTurn,state="disabled")

        self.button_quit = Button(master, text="Quitter", padx=40, pady =5, font=("Helvetica", 12),
                                  bg=self.Button_bg_color, fg=self.Button_ft_color, command=master.quit)

        self.restartBoard = Button(master, text="Réinitialiser Jeu", padx=40, pady =5, font=("Helvetica", 12),
                                  bg=self.Button_bg_color, fg=self.Button_ft_color, state=DISABLED)

        # Put the buttons on the screen
        self.button_1.grid(row=3, column=0)
        self.button_2.grid(row=3, column=1)
        self.button_3.grid(row=3, column=2)
        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)
        self.button_7.grid(row=1, column=0)
        self.button_8.grid(row=1, column=1)
        self.button_9.grid(row=1, column=2)
        self.button_0.grid(row=4, column=0)
        self.button_commitScore.grid(row=5, column=0, columnspan=3)
        self.button_clear.grid(row=4, column=1, columnspan=2)
        self.button_addPlayer.grid(row=0, column=0,columnspan=1)
        self.button_gameMode.grid(row=0, column=2,columnspan=1)
        self.button_editScore.grid(row=0, column=3,columnspan=1)
        self.button_editName.grid(row=0, column=4,columnspan=1)
        self.button_endTurn.grid(row=0, column=0,columnspan=1)
        self.button_gameStart.grid(row=0, column=3,columnspan=1)
        self.restartBoard.grid(row=13, column=10,columnspan=1, sticky="SE")
        self.button_quit.grid(row=13, column=11, columnspan=1, sticky="SE")

        #---------------------------------------------------------------------------------------------------------------
        # CREATING ENTRY BOXES
        #---------------------------------------------------------------------------------------------------------------
        # Create Entry box
        self.input_Score = Entry(self.frame2, width=5, bg='black',fg='yellow', borderwidth=3, font=("Helvetica", 50),
                                       justify='center',disabledbackground='black',disabledforeground="yellow", state=DISABLED)
        #Columnspan can hold other slots
        self.input_Score.grid(row=0,column=0, columnspan=3)
        #input_Score.insert(0, "Enter Name")

        #---------------------------------------------------------------------------------------------------------------
        # CREATING STATUS
        #---------------------------------------------------------------------------------------------------------------
        self.updateStatusLabel = Label(self.emptylabel0, padx=1, pady =20, text="Ajoutez au moins un Joueur!",
                                       font=("Helvetica", 12), bg=self.Button_bg_color,
                                       fg="cyan")
        self.updateStatusLabel.grid(row=0,column=0)

        #---------------------------------------------------------------------------------------------------------------
        # CREATING PLAYERS ENTRY BOXES
        #---------------------------------------------------------------------------------------------------------------
        #First Player Name
        self.player_1_label_1= Entry(self.frame3, width=16, bg=self.Button_bg_color,fg="grey", borderwidth=0, font=("Helvetica", 14),
                                       justify='center',disabledbackground=self.Button_bg_color,disabledforeground="grey",state=DISABLED)
        self.player_1_label_1.grid(row=0,column=0)
        self.player_1_label_1.insert(0, "Ajoutez le Joueur #1")
        self.player_1_label_1.config(state=DISABLED)

        #First Player Score
        self.player_1_label_2= Entry(self.frame3, width=5, bg=self.Button_bg_color,fg="grey", borderwidth=1, font=("Helvetica", 30),
                                       justify='center',disabledbackground=self.Button_bg_color,disabledforeground="grey")
        self.player_1_label_2.grid(row=2,column=0,pady=10)
        self.player_1_label_2.insert(0, "501")
        self.player_1_label_2.config(state=DISABLED)

        # Second Player Name
        self.player_2_label_1= Entry(self.frame4, width=16, bg=self.Button_bg_color,fg="grey", borderwidth=0, font=("Helvetica", 14),
                                       justify='center',disabledbackground=self.Button_bg_color,disabledforeground="grey")
        self.player_2_label_1.grid(row=0,column=0)
        self.player_2_label_1.insert(0, "Ajoutez le Joueur #2")
        self.player_2_label_1.config(state=DISABLED)

        # Second Player Score
        self.player_2_label_2= Entry(self.frame4, width=5, bg=self.Button_bg_color,fg="grey", borderwidth=1, font=("Helvetica", 30),
                                       justify='center',disabledbackground=self.Button_bg_color,disabledforeground="grey")
        self.player_2_label_2.grid(row=2,column=0,pady=10)
        self.player_2_label_2.insert(0, "501")
        self.player_2_label_2.config(state=DISABLED)

        #Third Player Name
        self.player_3_label_1= Entry(self.frame5, width=16, bg=self.Button_bg_color,fg="grey", borderwidth=0, font=("Helvetica", 14),
                                       justify='center',disabledbackground=self.Button_bg_color,disabledforeground="grey")
        self.player_3_label_1.grid(row=0,column=0)
        self.player_3_label_1.insert(0, "Ajoutez le Joueur #3")
        self.player_3_label_1.config(state=DISABLED)

        #Third Player Score
        self.player_3_label_2= Entry(self.frame5, width=5, bg=self.Button_bg_color,fg="grey", borderwidth=1, font=("Helvetica", 30),
                                       justify='center',disabledbackground=self.Button_bg_color,disabledforeground="grey")
        self.player_3_label_2.grid(row=2,column=0,pady=10)
        self.player_3_label_2.insert(0, "501")
        self.player_3_label_2.config(state=DISABLED)

        #Fourth Player Name
        self.player_4_label_1= Entry(self.frame6, width=16, bg=self.Button_bg_color,fg="grey", borderwidth=0, font=("Helvetica", 14),
                                       justify='center',disabledbackground=self.Button_bg_color,disabledforeground="grey")
        self.player_4_label_1.grid(row=0,column=0)
        self.player_4_label_1.insert(0, "Ajoutez le Joueur #4")
        self.player_4_label_1.config(state=DISABLED)

        #Fourth Player Score
        self.player_4_label_2= Entry(self.frame6, width=5, bg=self.Button_bg_color,fg="grey", borderwidth=1, font=("Helvetica", 30),
                                       justify='center',disabledbackground=self.Button_bg_color,disabledforeground="grey")
        self.player_4_label_2.grid(row=2,column=0,pady=10)
        self.player_4_label_2.insert(0, "501")
        self.player_4_label_2.config(state=DISABLED)

        #---------------------------------------------------------------------------------------------------------------
        # CREATING IMAGES (from .SGI files)
        #---------------------------------------------------------------------------------------------------------------
        #Images global variable:
        global arrowImage
        global logoImage

        logoImage= ImageTk.PhotoImage(Image.open("dart_Logo.sgi"))
        self.logoImage = Label(self.emptylabel_3, image=logoImage,bg=self.Button_bg_color, fg="grey")
        self.logoImage.grid(row=1,column=1,columnspan=2)

        arrowImage= ImageTk.PhotoImage(Image.open("arrow.sgi"))
        self.arrowImage = Label(self.emptylabel_4, image=arrowImage,bg=self.Button_bg_color, fg="grey")

        # for testing...

        #self.arrowImage.grid(row=1,column=1)

        #self.arrowImage = Label(self.emptylabel_5, image=arrowImage,bg=self.Button_bg_color, fg="grey")
        #self.arrowImage.grid(row=1,column=1)

        #self.arrowImage = Label(self.emptylabel_6, image=arrowImage,bg=self.Button_bg_color, fg="grey")
        #self.arrowImage.grid(row=1,column=1)

        #self.arrowImage = Label(self.emptylabel_7, image=arrowImage,bg=self.Button_bg_color, fg="grey")
        #self.arrowImage.grid(row=1,column=1)

    #---------------------------------------------------------------------------------------------------------------
    # SOFTWARE VERSION LABEL
    #---------------------------------------------------------------------------------------------------------------
        self.softVersionLabel = Label(master, padx=1, pady =1, text=self.softVersion,
                                       font=("Helvetica", "12","italic"), bg=self.Button_bg_color,
                                       fg="black")

        self.softVersionLabel.grid(row=14,column=0,sticky="NW")

    #-------------------------------------------------------------------------------------------------------------------
    # DEFINING FUNCTION
    #-------------------------------------------------------------------------------------------------------------------

    def function_updateStatusLabel(self,text):
        self.updateStatusLabel.destroy()
        self.updateStatusLabel = Label(self.emptylabel0, padx=1, pady=20, text=text, font=("Helvetica", 12),
                                       bg=self.Button_bg_color, fg="cyan")
        self.updateStatusLabel.grid(row=0,column=0,columnspan=1)
        return

    def function_refreshImages(self):
        self.logoImage = Label(self.emptylabel_3, image=logoImage,bg=self.Button_bg_color, fg="grey")
        self.logoImage.grid(row=1,column=1,columnspan=2)
        if self.gameStarted == True:
            self.arrowImage = Label(self.emptylabel_4, image=arrowImage,bg=self.Button_bg_color, fg="grey")
            self.arrowImage.grid(row=1,column=1)
        return



    def function_click(self, number):
        # A class "Game" with its properties must be sent to this function
        # Transfer created player to the Lobby
        if self.gameStarted == True:

            impossibleScore3 = [179, 178, 176, 175, 173, 172, 169, 166, 163]
            scoreFlag1 = False
            scoreFlag2 = False
            current = self.input_Score.get()

            if len(current) < 3:
                self.input_Score.config(state=NORMAL)
                self.input_Score.delete(0,END)
                self.input_Score.insert(0, str(current) + str(number))
                self.input_Score.config(state=DISABLED)

            if len(current) == 3:
                newValue = self.input_Score.get()
                if newValue > 1:
                    print('holla!')

        return

    def function_clear(self):
          # A class "Game" with its properties must be sent to this function
        # Transfer created player to the Lobby
        if self.nbPlayer != 1:
            self.input_Score.config(state=NORMAL)
            self.input_Score.delete(0,END)
            self.input_Score.config(state=DISABLED)

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

    def function_addPlayer(MainWindow):
        # Transfer created player to the Lobby

        MainWindow.subWin = Tk()
        MainWindow.subWin.wm_title("Ajouter Joueur #%s" % (MainWindow.nbPlayer+1))
        MainWindow.subWin.configure(background=MainWindow.Button_bg_color)
        MainWindow.subWin.resizable(False, False)

        MainWindow.subWin.emptylabel_1 = Label(MainWindow.subWin, padx=10, pady=10,background=MainWindow.Button_bg_color)
        MainWindow.subWin.emptylabel_1.grid(row=0,column=0, columnspan=4)

        MainWindow.subWin.emptylabel_2 = Label(MainWindow.subWin, padx=10, pady=2,background=MainWindow.Button_bg_color)
        MainWindow.subWin.emptylabel_2.grid(row=4,column=0, columnspan=4)

        l = Label(MainWindow.subWin, text="Entrer le Nom du Joueur #%s" % (MainWindow.nbPlayer+1),font= ("Helvetica",12),bg=MainWindow.Button_bg_color,fg=MainWindow.Button_ft_color)
        l.grid(row=1,column=0, columnspan=1, padx=50, pady=10)

        MainWindow.subWin.errorStatus = Label(MainWindow.subWin, text="",bg=MainWindow.Button_bg_color,fg="cyan")
        MainWindow.subWin.errorStatus.grid(row=2,column=1, columnspan=1, padx=1, pady=10, sticky="n")

        MainWindow.subWin.input_Name = Entry(MainWindow.subWin, width=20, bg='black',fg='yellow', borderwidth=3, font=("Helvetica", 16),justify='center')
        MainWindow.subWin.input_Name.grid(row=1,column=1, columnspan=1)

        MainWindow.subWin.button_commitAddPlayer= Button(MainWindow.subWin, text="Enregistrer", padx=10, pady =5, font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                            fg="yellow", command=MainWindow.commitAddPlayer)
        MainWindow.subWin.button_cancel = Button(MainWindow.subWin, text="Annuler", padx=10, pady =5, font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                      fg=MainWindow.Button_ft_color, command=lambda: MainWindow.subWin.destroy())

        MainWindow.subWin.button_commitAddPlayer.grid(row=3 ,column=1, columnspan=1)
        MainWindow.subWin.button_cancel.grid(row=3 ,column=0, columnspan=1)

        return

    def commitAddPlayer(MainWindow):
        # A class "Game" with its properties must be sent to this function
        # Transfer created player to the Lobby
        playerName= MainWindow.subWin.input_Name.get()

        if playerName == "":
            MainWindow.subWin.errorStatus.configure(text="Vous devez entrer un nom... ")
            return

        if MainWindow.nbPlayer == 0:
            MainWindow.button_gameStart.configure(state="normal",fg="#60ff30")

            MainWindow.player_1_label_1.config(state=NORMAL)
            MainWindow.player_1_label_1.delete(0, END)
            MainWindow.player_1_label_1.insert(0, playerName)
            MainWindow.player_1_label_1.config(state=DISABLED,disabledforeground="yellow")
            MainWindow.frame3.configure(relief='raised')
            updateStatusLabeltext= "Ajouter un deuxième joueur OU Cliquer Démarrer Partie!"

        if MainWindow.nbPlayer == 1:
            MainWindow.player_2_label_1.config(state=NORMAL)
            MainWindow.player_2_label_1.delete(0, END)
            MainWindow.player_2_label_1.insert(0, playerName)
            MainWindow.player_2_label_1.config(state=DISABLED,disabledforeground="yellow")
            MainWindow.frame4.configure(relief='raised')
            updateStatusLabeltext= "Ajouter un troisième joueur OU Cliquer Démarrer Partie!"

        if MainWindow.nbPlayer == 2:
            MainWindow.player_3_label_1.config(state=NORMAL)
            MainWindow.player_3_label_1.delete(0, END)
            MainWindow.player_3_label_1.insert(0, playerName)
            MainWindow.player_3_label_1.config(state=DISABLED,disabledforeground="yellow")
            MainWindow.frame5.configure(relief='raised')
            updateStatusLabeltext= "Ajouter un quatrième joueur OU Cliquer Démarrer Partie!"

        if MainWindow.nbPlayer == 3:
            MainWindow.player_4_label_1.config(state=NORMAL)
            MainWindow.player_4_label_1.delete(0, END)
            MainWindow.player_4_label_1.insert(0, playerName)
            MainWindow.player_4_label_1.config(state=DISABLED,disabledforeground="yellow")
            MainWindow.frame6.configure(relief='raised')
            updateStatusLabeltext= "Cliquer Démarrer Partie!"

        MainWindow.nbPlayer += 1
        print(MainWindow.nbPlayer)
        MainWindow.function_updateStatusLabel(updateStatusLabeltext)
        MainWindow.function_refreshImages()
        MainWindow.subWin.destroy()

        if MainWindow.nbPlayer >= 5:
                MainWindow.button_addPlayer.configure(state=DISABLED)

        return

    def function_gameStart(self):
        if self.gameStarted == False:
            self.gameStarted = True
            self.frame9.configure(borderwidth=0)
            self.button_gameStart.configure(borderwidth=0)
            print(self.gameStarted)
            self.button_endTurn.configure(state="normal")
            self.button_gameStart.configure(state=DISABLED,disabledforeground=self.Button_bg_color)

            if self.nbPlayer != 0:
                if self.nbPlayer == 1:
                    self.player_1_label_2.config(state=NORMAL)
                    self.player_1_label_2.config(state=DISABLED,disabledforeground="yellow")

                    self.playerIndex = list(range(1, self.nbPlayer+1))

                if self.nbPlayer == 2:
                    self.player_2_label_2.config(state=NORMAL)
                    self.player_2_label_2.config(state=DISABLED,disabledforeground="yellow")
                    self.player_1_label_2.config(state=NORMAL)
                    self.player_1_label_2.config(state=DISABLED,disabledforeground="yellow")

                    self.playerIndex = list(range(1, self.nbPlayer+1))

                if self.nbPlayer == 3:
                    self.player_3_label_2.config(state=NORMAL)
                    self.player_3_label_2.config(state=DISABLED,disabledforeground="yellow")
                    self.player_2_label_2.config(state=NORMAL)
                    self.player_2_label_2.config(state=DISABLED,disabledforeground="yellow")
                    self.player_1_label_2.config(state=NORMAL)
                    self.player_1_label_2.config(state=DISABLED,disabledforeground="yellow")

                    self.playerIndex = list(range(1, self.nbPlayer+1))

                if self.nbPlayer == 4:
                    self.player_4_label_2.config(state=NORMAL)
                    self.player_4_label_2.config(state=DISABLED,disabledforeground="yellow")
                    self.player_3_label_2.config(state=NORMAL)
                    self.player_3_label_2.config(state=DISABLED,disabledforeground="yellow")
                    self.player_2_label_2.config(state=NORMAL)
                    self.player_2_label_2.config(state=DISABLED,disabledforeground="yellow")
                    self.player_1_label_2.config(state=NORMAL)
                    self.player_1_label_2.config(state=DISABLED,disabledforeground="yellow")

                    self.playerIndex = list(range(1, self.nbPlayer+1))

        self.function_refreshImages()
        self.function_updateStatusLabel("La Partie est commencée!")

        return

    def function_endTurn(self):
        if self.gameStarted == True:

            print(self.playerIndex)

            # Remove Current arrow on active player

            # Add Arrow to the next active player considering the amount of players
            self.arrowImage = Label(self.emptylabel_4, image=arrowImage,bg=self.Button_bg_color, fg="grey")
            self.arrowImage.grid(row=1,column=1)

            self.button_endTurn.configure(state="normal")

            number = 9
            # eval performs the multiplication passed as argument
            square_number = eval('number * number')
            print(square_number)

            if self.nbPlayer != 0:
                if self.nbPlayer == 2:
                    print('loop2')

                if self.nbPlayer == 3:
                    print('loop3')

                if self.nbPlayer == 4:
                    print('loop4')

                if self.nbPlayer == 5:
                    print('loop5')

        return



e = MainWindow(root)
# The GUI is acting like a listening... Constantly waiting for something to happen.
root.mainloop()
