from tkinter import *
from PIL import ImageTk, Image
import pandas as pd

# To display all log data in console
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

class MainWindow:

    def __init__(self, master):

        # Create variables (temporary method))
        self.softVersion = "ver 1.0"
        self.nbPlayer = 0
        self.Button_bg_color = "#245042"
        self.Button_ft_color = "#D3DBE5"
        self.activeButton_bg_color = "#9aa794"
        self.activeButton_ft_color = "#D3DBE5"
        self.gameMode = [] #
        self.gameStarted = False
        self.playerIndex = []  # Variable tracking player turn and total number of players
        self.turnIndexLog = [] #
        self.keyBindSetup(master)
        self.editScoreMode = False
        self.editNameMode = False

        # --------------------------------------------------------------------------------------------------------------
        #   Create Frames for the UI Layout
        # --------------------------------------------------------------------------------------------------------------

        # Add player button frame
        self.frame0 = LabelFrame(master, padx=5, pady=5, bg=self.Button_bg_color)
        self.frame0.grid(row=0, column=0, columnspan=7, sticky="W")

        # To create horizontal space between frames (this area provide instructions & Game Status)
        self.emptylabel0 = Label(master, padx=25, pady=30, bg=self.Button_bg_color)
        self.emptylabel0.grid(row=2, column=1, columnspan=3)

        # To create a vertical space between first column of frames
        self.emptylabel_1 = Label(master, padx=20, pady=5, bg=self.Button_bg_color)
        self.emptylabel_1.grid(row=2, column=0, rowspan=14)

        # Calculator and submit button frame
        self.frame1 = LabelFrame(master, padx=10, pady=10, bg=self.Button_bg_color)
        self.frame1.grid(row=5, column=1, columnspan=3, rowspan=5)

        # To create a vertical space after first column of frames
        self.emptylabel_2 = Label(master, padx=20, pady=10, bg=self.Button_bg_color)
        self.emptylabel_2.grid(row=5, column=4, rowspan=2)

        # To create vertical space between frames
        self.emptylabel_3 = Label(master, padx=25, pady=2, bg=self.Button_bg_color)
        self.emptylabel_3.grid(row=0, column=10, columnspan=5, rowspan=5)

        # Entry Score frame
        self.frame2 = LabelFrame(master, padx=10, pady=10, bg=self.Button_bg_color)
        self.frame2.grid(row=3, column=1, columnspan=3)

        # Start Game button frame
        self.frame9 = LabelFrame(master, padx=10, pady=10, bg=self.Button_bg_color)
        self.frame9.grid(row=3, column=5, columnspan=2, rowspan=1)

        # Turn arrow panel for player 1
        self.arrowLabel_1 = Label(master, padx=10, pady=0, bg=self.Button_bg_color)
        self.arrowLabel_1.grid(row=4, column=5, rowspan=2, columnspan=3, ipady=1)

        # Turn arrow panel for player 2
        self.arrowLabel_2 = Label(master, padx=10, pady=0, bg=self.Button_bg_color)
        self.arrowLabel_2.grid(row=4, column=9, rowspan=2, columnspan=3, ipady=1)

        # Turn arrow panel for player 3
        self.arrowLabel_3 = Label(master, padx=10, pady=0, bg=self.Button_bg_color)
        self.arrowLabel_3.grid(row=7, column=5, rowspan=2, columnspan=3, ipady=8)

        # Turn arrow panel for player 4
        self.arrowLabel_4 = Label(master, padx=10, pady=0, bg=self.Button_bg_color)
        self.arrowLabel_4.grid(row=7, column=9, rowspan=2, columnspan=3, ipady=8)

        # End turn button frame
        self.frame7 = LabelFrame(master, padx=10, pady=5, bg=self.Button_bg_color)
        self.frame7.grid(row=10, column=2, columnspan=1)

        # Previous (Ctrl Z) (AND Y) button frame
        self.frame20 = Label(master, bg=self.Button_bg_color, borderwidth=0)
        self.frame20.grid(row=10, column=11, columnspan=8, rowspan=2,sticky='W')

        # player 1 frame
        self.frame3 = LabelFrame(master, padx=30, pady=20, bg=self.Button_bg_color)
        self.frame3.grid(row=5, column=5, columnspan=4, rowspan=3)

        # player 2 frame
        self.frame4 = LabelFrame(master, padx=30, pady=20, bg=self.Button_bg_color)
        self.frame4.grid(row=5, column=9, columnspan=4, rowspan=3)

        # player 3 frame
        self.frame5 = LabelFrame(master, padx=30, pady=20, background=self.Button_bg_color)
        self.frame5.grid(row=7, column=5, columnspan=4, rowspan=8)

        # fourth player 4 frame
        self.frame6 = LabelFrame(master, padx=30, pady=20, bg=self.Button_bg_color)
        self.frame6.grid(row=7, column=9, columnspan=4, rowspan=8)

        # --------------------------------------------------------------------------------------------------------------
        #   CREATING BUTTONS
        # --------------------------------------------------------------------------------------------------------------

        # Define buttons
        self.button_1 = Button(self.frame1, text="1", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                               fg=self.Button_ft_color, command=lambda: self.function_click(1),
                               activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

        self.button_2 = Button(self.frame1, text="2", padx=40, pady=20, font=("Helvetica", 25), bg= self.Button_bg_color,
                               fg=self.Button_ft_color, command=lambda: self.function_click(2),
                               activebackground= self.activeButton_bg_color, activeforeground= self.activeButton_ft_color)

        self.button_3 = Button(self.frame1, text="3", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                               fg=self.Button_ft_color, command=lambda: self.function_click(3),
                               activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

        self.button_4 = Button(self.frame1, text="4", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                               fg=self.Button_ft_color, command=lambda: self.function_click(4),
                               activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

        self.button_5 = Button(self.frame1, text="5", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                               fg=self.Button_ft_color, command=lambda: self.function_click(5),
                               activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

        self.button_6 = Button(self.frame1, text="6", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                               fg=self.Button_ft_color, command=lambda: self.function_click(6),
                               activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

        self.button_7 = Button(self.frame1, text="7", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                               fg=self.Button_ft_color, command=lambda: self.function_click(7),
                               activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

        self.button_8 = Button(self.frame1, text="8", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                               fg=self.Button_ft_color, command=lambda: self.function_click(8),
                               activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

        self.button_9 = Button(self.frame1, text="9", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                               fg=self.Button_ft_color, command=lambda: self.function_click(9),
                               activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

        self.button_0 = Button(self.frame1, text="0", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                               fg=self.Button_ft_color, command=lambda: self.function_click(0),
                               activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

        self.button_commitScore = Button(self.frame1, text="Soumettre", padx=100, pady=20, font=("Helvetica", 25),
                                         bg=self.Button_bg_color, fg="yellow", command=self.button_commitScore,
                                         activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color,
                                         state="disabled")

        self.button_clear = Button(self.frame1, text="C", padx=99.49999, pady=20, font=("Helvetica", 25),
                                   bg=self.Button_bg_color, fg=self.Button_ft_color, command=self.function_clear,
                                   activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

        self.button_addPlayer = Button(self.frame0, text="Ajouter Joueur", padx=35, pady=3, font=("Helvetica", 12),
                                       bg=self.Button_bg_color, fg=self.Button_ft_color, command=self.function_addPlayer,
                                       activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

        self.button_gameMode = Button(self.frame0, text="Mode de Jeu", padx=35, pady=3, font=("Helvetica", 12),
                                      bg=self.Button_bg_color, fg=self.Button_ft_color, state=DISABLED,
                                      activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

        self.button_editScore = Button(self.frame0, text="Modifier Pointage", padx=20, pady=3, font=("Helvetica", 12),
                                       bg=self.Button_bg_color, fg=self.Button_ft_color, command=self.function_editScore,
                                       activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color,
                                       state= "disabled")

        self.button_editName = Button(self.frame0, text="Renommer Joueur", padx=20, pady=3, font=("Helvetica", 12),
                                      bg=self.Button_bg_color, fg=self.Button_ft_color, state=DISABLED, command=self.function_editName,
                                      activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

        self.button_gameStart = Button(self.frame9, text="Démarrer Partie!", padx=40, pady=5, font=("Helvetica", 14, "bold"),
                                       bg=self.Button_bg_color, fg=self.Button_ft_color, command=self.function_gameStart,
                                       activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color, state="disabled")

        self.button_endTurn = Button(self.frame7, text="Tour terminé", padx=40, pady=5, font=("Helvetica", 12),
                                     bg=self.Button_bg_color, fg=self.Button_ft_color,
                                     command=self.function_endTurn, state="disabled",
                                     activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

        self.button_goBack = Button(self.frame20, text="<<", padx=5, pady=1, font=("Helvetica", 10),
                                    bg=self.Button_bg_color, fg=self.Button_ft_color, state="normal",relief="groove",
                                    activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

        self.button_forward = Button(self.frame20, text=">>", padx=5, pady=1, font=("Helvetica", 10),
                                     bg=self.Button_bg_color, fg=self.Button_ft_color, state="normal",relief="groove",
                                     activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

        self.button_quit = Button(master, text="Quitter", padx=40, pady=5, font=("Helvetica", 12),
                                  bg=self.Button_bg_color, fg=self.Button_ft_color,
                                  activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color,
                                  command=master.quit)

        self.restartBoard = Button(master, text="Réinitialiser Jeu", padx=40, pady=5, font=("Helvetica", 12),
                                   bg=self.Button_bg_color, fg=self.Button_ft_color,
                                   activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color,
                                   command=function_restartBoard)

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
        self.button_addPlayer.grid(row=0, column=0, columnspan=1)
        self.button_gameMode.grid(row=0, column=2, columnspan=1)
        self.button_editScore.grid(row=0, column=3, columnspan=1)
        self.button_editName.grid(row=0, column=4, columnspan=1)
        self.button_endTurn.grid(row=0, column=0, columnspan=1)
        self.button_gameStart.grid(row=0, column=3, columnspan=1)
        self.button_goBack.grid(row=0, column=0,ipadx=5)
        self.button_forward.grid(row=0, column=1,ipadx=5)
        self.restartBoard.grid(row=13, column=10, columnspan=1, sticky="SE")
        self.button_quit.grid(row=13, column=11, columnspan=1, sticky="SE")

        # ---------------------------------------------------------------------------------------------------------------
        # CREATING ENTRY BOXES
        # ---------------------------------------------------------------------------------------------------------------
        # Create Score Entry box
        self.input_Score = Entry(self.frame2, width=5, bg='black', fg='yellow', borderwidth=3, font=("Helvetica", 50),
                                 justify='center', disabledbackground='black', disabledforeground="yellow",
                                 state=DISABLED)
        self.input_Score.grid(row=0, column=0, columnspan=3)

        # CREATING PLAYERS ENTRY BOXES
        # First Player Name and Score
        self.player_1_label_1 = Entry(self.frame3, width=16, bg=self.Button_bg_color, fg="grey", borderwidth=0,
                                      font=("Helvetica", 14),
                                      justify='center', disabledbackground=self.Button_bg_color,
                                      disabledforeground="grey")

        self.player_1_label_2 = Entry(self.frame3, width=5, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                      font=("Helvetica", 30),
                                      justify='center', disabledbackground=self.Button_bg_color,
                                      disabledforeground="grey")

        self.player_1_label_3 = Entry(self.frame3, width=10, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                      font=("Helvetica", 8),
                                      justify='right', disabledbackground=self.Button_bg_color,
                                      disabledforeground="grey",border=0)

        self.player_1_label_4 = Entry(self.frame3, width=10, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                      font=("Helvetica", 8),
                                      justify='right', disabledbackground=self.Button_bg_color,
                                      disabledforeground="grey", border=0)

        self.player_1_label_1.grid(row=0, column=0)
        self.player_1_label_1.insert(0, "Ajoutez le Joueur #1")
        self.player_1_label_1.config(state=DISABLED)

        self.player_1_label_2.grid(row=2, column=0, pady=10)
        self.player_1_label_2.insert(0, "501")
        self.player_1_label_2.config(state=DISABLED)

        self.player_1_label_3.grid(row=3, column=0, pady=0, sticky='SW')
        self.player_1_label_3.insert(0, "Avr:")
        self.player_1_label_3.config(state=DISABLED)

        self.player_1_label_4.grid(row=4, column=0, pady=0, sticky='SW')
        self.player_1_label_4.insert(0, "HighScore:")
        self.player_1_label_4.config(state=DISABLED)


        # Second Player Name and Score
        self.player_2_label_1 = Entry(self.frame4, width=16, bg=self.Button_bg_color, fg="grey", borderwidth=0,
                                      font=("Helvetica", 14),
                                      justify='center', disabledbackground=self.Button_bg_color,
                                      disabledforeground="grey")
        self.player_2_label_2 = Entry(self.frame4, width=5, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                      font=("Helvetica", 30),
                                      justify='center', disabledbackground=self.Button_bg_color,
                                      disabledforeground="grey")

        self.player_2_label_3 = Entry(self.frame4, width=10, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                      font=("Helvetica", 8),
                                      justify='right', disabledbackground=self.Button_bg_color,
                                      disabledforeground="grey",border=0)

        self.player_2_label_4 = Entry(self.frame4, width=10, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                      font=("Helvetica", 8),
                                      justify='right', disabledbackground=self.Button_bg_color,
                                      disabledforeground="grey", border=0)

        self.player_2_label_1.grid(row=0, column=0)
        self.player_2_label_1.insert(0, "Ajoutez le Joueur #2")
        self.player_2_label_1.config(state=DISABLED)
        self.player_2_label_2.grid(row=2, column=0, pady=10)
        self.player_2_label_2.insert(0, "501")
        self.player_2_label_2.config(state=DISABLED)

        self.player_2_label_3.grid(row=3, column=0, pady=0, sticky='SW')
        self.player_2_label_3.insert(0, "Avr:")
        self.player_2_label_3.config(state=DISABLED)

        self.player_2_label_4.grid(row=4, column=0, pady=0, sticky='SW')
        self.player_2_label_4.insert(0, "HighScore:")
        self.player_2_label_4.config(state=DISABLED)

        # Third Player Name and Score
        self.player_3_label_1 = Entry(self.frame5, width=16, bg=self.Button_bg_color, fg="grey", borderwidth=0,
                                      font=("Helvetica", 14),
                                      justify='center', disabledbackground=self.Button_bg_color,
                                      disabledforeground="grey")
        self.player_3_label_2 = Entry(self.frame5, width=5, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                      font=("Helvetica", 30),
                                      justify='center', disabledbackground=self.Button_bg_color,
                                      disabledforeground="grey")

        self.player_3_label_3 = Entry(self.frame5, width=10, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                      font=("Helvetica", 8),
                                      justify='right', disabledbackground=self.Button_bg_color,
                                      disabledforeground="grey",border=0)

        self.player_3_label_4 = Entry(self.frame5, width=10, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                      font=("Helvetica", 8),
                                      justify='right', disabledbackground=self.Button_bg_color,
                                      disabledforeground="grey", border=0)

        self.player_3_label_1.grid(row=0, column=0)
        self.player_3_label_1.insert(0, "Ajoutez le Joueur #3")
        self.player_3_label_1.config(state=DISABLED)
        self.player_3_label_2.grid(row=2, column=0, pady=10)
        self.player_3_label_2.insert(0, "501")
        self.player_3_label_2.config(state=DISABLED)

        self.player_3_label_3.grid(row=3, column=0, pady=0, sticky='SW')
        self.player_3_label_3.insert(0, "Avr:")
        self.player_3_label_3.config(state=DISABLED)

        self.player_3_label_4.grid(row=4, column=0, pady=0, sticky='SW')
        self.player_3_label_4.insert(0, "HighScore:")
        self.player_3_label_4.config(state=DISABLED)

        # Fourth Player Name and Score
        self.player_4_label_1 = Entry(self.frame6, width=16, bg=self.Button_bg_color, fg="grey", borderwidth=0,
                                      font=("Helvetica", 14),
                                      justify='center', disabledbackground=self.Button_bg_color,
                                      disabledforeground="grey")
        self.player_4_label_2 = Entry(self.frame6, width=5, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                      font=("Helvetica", 30),
                                      justify='center', disabledbackground=self.Button_bg_color,
                                      disabledforeground="grey")

        self.player_4_label_3 = Entry(self.frame6, width=10, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                      font=("Helvetica", 8),
                                      justify='right', disabledbackground=self.Button_bg_color,
                                      disabledforeground="grey",border=0)

        self.player_4_label_4 = Entry(self.frame6, width=10, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                      font=("Helvetica", 8),
                                      justify='right', disabledbackground=self.Button_bg_color,
                                      disabledforeground="grey", border=0)

        self.player_4_label_1.grid(row=0, column=0)
        self.player_4_label_1.insert(0, "Ajoutez le Joueur #4")
        self.player_4_label_1.config(state=DISABLED)
        self.player_4_label_2.grid(row=2, column=0, pady=10)
        self.player_4_label_2.insert(0, "501")
        self.player_4_label_2.config(state=DISABLED)

        self.player_4_label_3.grid(row=3, column=0, pady=0, sticky='SW')
        self.player_4_label_3.insert(0, "Avr:")
        self.player_4_label_3.config(state=DISABLED)

        self.player_4_label_4.grid(row=4, column=0, pady=0, sticky='SW')
        self.player_4_label_4.insert(0, "HighScore:")
        self.player_4_label_4.config(state=DISABLED)

        # ---------------------------------------------------------------------------------------------------------------
        # CREATING STATUS
        # ---------------------------------------------------------------------------------------------------------------
        self.updateStatusLabel = Label(self.emptylabel0, padx=1, pady=20, text="Ajoutez au moins un Joueur!",
                                       font=("Helvetica", 12), bg=self.Button_bg_color,
                                       fg="cyan")
        self.updateStatusLabel.grid(row=0, column=0)

        # ---------------------------------------------------------------------------------------------------------------
        # CREATING IMAGES (from .SGI files)
        # ---------------------------------------------------------------------------------------------------------------
        global logoImage
        global arrowImage


        logoImage = ImageTk.PhotoImage(Image.open("dart_Logo2.sgi"))
        self.logoImage = Label(self.emptylabel_3, image=logoImage, bg=self.Button_bg_color, fg="grey")
        self.logoImage.grid(row=1, column=1, columnspan=3)

        arrowImage = ImageTk.PhotoImage(Image.open("arrow.sgi"))
        self.arrowImage = Label(self.arrowLabel_1, image=arrowImage, bg=self.Button_bg_color, fg="grey")

        # ---------------------------------------------------------------------------------------------------------------
        # SOFTWARE VERSION LABEL
        # ---------------------------------------------------------------------------------------------------------------
        self.softVersionLabel = Label(master, padx=1, pady=1, text=self.softVersion,
                                      font=("Helvetica", "12", "italic"), bg=self.Button_bg_color,
                                      fg="black")

        self.softVersionLabel.grid(row=13, column=0, rowspan=2, sticky="SW")

    # -------------------------------------------------------------------------------------------------------------------
    # DEFINING FUNCTION
    # -------------------------------------------------------------------------------------------------------------------

    def keyBindSetup(self,master):
        master.bind("1", lambda event: MainWindow.function_click(self, 1))
        master.bind("2", lambda event: MainWindow.function_click(self, 2))
        master.bind("3", lambda event: MainWindow.function_click(self, 3))
        master.bind("4", lambda event: MainWindow.function_click(self, 4))
        master.bind("5", lambda event: MainWindow.function_click(self, 5))
        master.bind("6", lambda event: MainWindow.function_click(self, 6))
        master.bind("7", lambda event: MainWindow.function_click(self, 7))
        master.bind("8", lambda event: MainWindow.function_click(self, 8))
        master.bind("9", lambda event: MainWindow.function_click(self, 9))
        master.bind("0", lambda event: MainWindow.function_click(self, 0))
        master.bind("<Return>", lambda event: MainWindow.button_commitScore(self))
        master.bind("<space>", lambda event: MainWindow.function_endTurn(self))
        return

    def function_updateStatusLabel(self, text):
        self.updateStatusLabel.destroy()
        self.updateStatusLabel = Label(self.emptylabel0, padx=1, pady=20, text=text, font=("Helvetica", 12),
                                       bg=self.Button_bg_color, fg="cyan")
        self.updateStatusLabel.grid(row=0, column=0, columnspan=1)
        return

    def function_refreshImages(self):
        self.logoImage = Label(self.emptylabel_3, image=logoImage, bg=self.Button_bg_color, fg="grey")
        self.logoImage.grid(row=1, column=1, columnspan=2)
        if self.gameStarted:

            currentPlayer = self.playerIndex[:1]
            if currentPlayer == [1]:
                self.arrowImage = Label(self.arrowLabel_1, image=arrowImage, bg=self.Button_bg_color, fg="grey")
                self.arrowImage.grid(row=1, column=1)

            if currentPlayer == [2]:
                self.arrowImage = Label(self.arrowLabel_2, image=arrowImage, bg=self.Button_bg_color, fg="grey")
                self.arrowImage.grid(row=1, column=1)
            if currentPlayer == [3]:
                self.arrowImage = Label(self.arrowLabel_3, image=arrowImage, bg=self.Button_bg_color, fg="grey")
                self.arrowImage.grid(row=1, column=1)
            if currentPlayer == [4]:
                self.arrowImage = Label(self.arrowLabel_4, image=arrowImage, bg=self.Button_bg_color, fg="grey")
                self.arrowImage.grid(row=1, column=1)
        return

    def function_click(self, number):
        # A class "Game" with its properties must be sent to this function
        # Transfer created player to the Lobby
        if self.gameStarted == True:

            impossibleScores = [179, 178, 176, 175, 173, 172, 169, 166, 163]
            scoreFlag1 = False
            scoreFlag2 = False

            if self.editScoreMode == False:
                current = self.input_Score.get()

                if len(current) < 3:
                    self.input_Score.config(state=NORMAL)
                    self.input_Score.delete(0, END)
                    self.input_Score.insert(0, str(current) + str(number))
                    self.input_Score.config(state=DISABLED)

                # Will change the state of the button depending of what is now inside
                newCurrent = self.input_Score.get()
                if len(newCurrent) > 0:
                    self.button_commitScore.configure(state=NORMAL)
                if len(newCurrent) < 0:
                    self.button_commitScore.configure(state=DISABLED)

            if self.editScoreMode == True:
                currentPlayer = self.playerIndex[:1]  # Who is playing
                currentScore = eval("self.player_"+str(currentPlayer[0])+"_label_2.get()", {"self": self})
                if len(currentScore) < 3:
                    eval("self.player_"+str(currentPlayer[0])+"_label_2.config(state=NORMAL)")
                    eval("self.player_"+str(currentPlayer[0])+"_label_2.delete(0, END)")
                    eval("self.player_"+str(currentPlayer[0])+"_label_2.insert(0, str(currentScore) + str(number))")
                    eval("self.player_"+str(currentPlayer[0])+"_label_2.config(state=DISABLED)")
                    newCurrentScore = eval("self.player_"+str(currentPlayer[0])+"_label_2.get()", {"self": self})

                    # Will change the state of the button depending of what is now inside
                    if len(newCurrentScore) > 0:
                        self.button_commitScore.configure(state=NORMAL)
                    elif len(newCurrentScore) <= 0:
                        self.button_commitScore.configure(state=DISABLED)
        return

    def function_clear(self):
        # A class "Game" with its properties must be sent to this function
        # Transfer created player to the Lobby
        if self.editScoreMode == False:
            self.input_Score.config(state=NORMAL)
            self.input_Score.delete(0, END)
            self.input_Score.config(state=DISABLED)
            self.button_commitScore.configure(state=DISABLED) # Clearing is also disabling the commit score button

        if self.editScoreMode == True:
            currentPlayer = self.playerIndex[:1]
            eval("self.player_"+str(currentPlayer[0])+"_label_2.config(state=NORMAL)")
            eval("self.player_"+str(currentPlayer[0])+"_label_2.delete(0, END)")
            eval("self.player_"+str(currentPlayer[0])+"_label_2.config(state=DISABLED)")
            self.button_commitScore.configure(state=DISABLED)
        return

    def button_commitScore(self):

        if self.editScoreMode == True:
                self.function_editScore()
                self.updateIndexLog()

        elif self.editScoreMode == False:
            scoreToInput = self.input_Score.get()
            if scoreToInput != '':
                self.whiteCommitScore()
                self.updateIndexLog()
        return

    def whiteCommitScore(self):
        # get Current Player turn over the total nb of player
        scoreToInput = self.input_Score.get()
        if scoreToInput != '':
            scoreToInput = int(self.input_Score.get())
            currentPlayer = self.playerIndex[:1]
            self.input_Score.config(state=NORMAL)
            self.input_Score.delete(0, END)
            self.input_Score.config(state=DISABLED)

            currentPlayerScore = eval("self.player_"+str(currentPlayer[0])+"_label_2.get()", {"self": self})

            if int(currentPlayerScore) >= int(scoreToInput):
                eval("self.player_"+str(currentPlayer[0])+"_label_2.config(state=NORMAL)")
                eval("self.player_"+str(currentPlayer[0])+"_label_2.delete(0, END)")
                eval("self.player_"+str(currentPlayer[0])+"_label_2.insert(0, str(int(currentPlayerScore) - scoreToInput))")
                eval("self.player_"+str(currentPlayer[0])+"_label_2.config(state=DISABLED)")

            self.button_commitScore.configure(state=DISABLED)
        return

    def updateIndexLog(self):
        if self.gameStarted == False:  # If the game is not started, create the Index Log with all added players
            # get Current Player turn over the total nb of player
            totalPlayer = self.playerIndex[1:]

            if totalPlayer == [1]:
                self.turnIndexLog = pd.DataFrame([[1, 0, 501]],
                                            columns=['gameTurn', 'Player_1_Turn', 'Player_1_Score'])
            elif totalPlayer == [2]:
                 self.turnIndexLog = pd.DataFrame([[1, 0, 501, 0, 501]],
                                             columns=['gameTurn', 'Player_1_Turn', 'Player_1_Score',
                                                      'Player_2_Turn', 'Player_2_Score'])
            elif totalPlayer == [3]:
                self.turnIndexLog = pd.DataFrame([[1, 0, 501, 0, 501, 0, 501]],
                                            columns=['gameTurn', 'Player_1_Turn', 'Player_1_Score', 'Player_2_Turn',
                                                     'Player_2_Score','Player_3_Turn', 'Player_3_Score'])
            elif totalPlayer == [4]:
                self.turnIndexLog = pd.DataFrame([[1, 0, 501, 0, 501, 0, 501, 0, 501]],
                                            columns=['gameTurn', 'Player_1_Turn', 'Player_1_Score', 'Player_2_Turn',
                                                     'Player_2_Score', 'Player_3_Turn', 'Player_3_Score',
                                                     'Player_4_Turn', 'Player_4_Score'])

        # If the game is started, add the committed score to the selected (current player)
        if self.gameStarted:
            currentGameTurn = self.turnIndexLog['gameTurn'].iloc[-1]
            totalPlayer = self.playerIndex[1:]
            currentPlayer = self.playerIndex[:1]

            if currentPlayer == [1]:
                CommitedScoreToLog = int(self.player_1_label_2.get())
                toAppend = pd.DataFrame([[currentGameTurn, 1, CommitedScoreToLog]], columns=['gameTurn', 'Player_1_Turn', 'Player_1_Score'])
                self.turnIndexLog = pd.concat([self.turnIndexLog, toAppend])

            elif currentPlayer == [2]:
                CommitedScoreToLog = int(self.player_2_label_2.get())
                toAppend = pd.DataFrame([[currentGameTurn, 1, CommitedScoreToLog]], columns=['gameTurn', 'Player_2_Turn', 'Player_2_Score'])
                self.turnIndexLog = pd.concat([self.turnIndexLog, toAppend])

            elif currentPlayer == [3]:
                CommitedScoreToLog = int(self.player_3_label_2.get())
                toAppend = pd.DataFrame([[currentGameTurn, 1, CommitedScoreToLog]], columns=['gameTurn', 'Player_3_Turn', 'Player_3_Score'])
                self.turnIndexLog = pd.concat([self.turnIndexLog, toAppend])

            elif currentPlayer == [4]:
                CommitedScoreToLog = int(self.player_4_label_2.get())
                toAppend = pd.DataFrame([[currentGameTurn, 1, CommitedScoreToLog]], columns=['gameTurn', 'Player_4_Turn', 'Player_4_Score'])
                self.turnIndexLog = pd.concat([self.turnIndexLog, toAppend])


        print(self.turnIndexLog)
        return

    def function_editScore(self):

        if self.gameStarted:
            currentPlayer = self.playerIndex[:1]  # Who is playing

            if self.editScoreMode == False:
                self.button_editScore.config(fg=self.activeButton_ft_color, bg=self.activeButton_bg_color, relief=SUNKEN)
                self.input_Score.config(state=NORMAL)
                self.input_Score.delete(0, END)
                self.input_Score.config(state=DISABLED)
                self.button_commitScore.configure(state=DISABLED)
                self.input_Score.config(disabledbackground=self.Button_bg_color)
                eval("self.player_"+str(currentPlayer[0])+"_label_2.config(disabledbackground='black')")
                self.editScoreMode = True

            elif self.editScoreMode == True:
                self.button_editScore.config(fg=self.Button_ft_color, bg=self.Button_bg_color, relief=RAISED)
                self.input_Score.config(disabledbackground='black')
                eval("self.player_"+str(currentPlayer[0])+"_label_2.config(disabledbackground=self.Button_bg_color)")
                self.editScoreMode = False
        return

    def function_editName(self):

        if self.gameStarted:
            currentPlayer = self.playerIndex[:1]  # Who is playing

            if self.editNameMode == False:
                self.function_addPlayer()
                self.editNameMode = True

            elif self.editNameMode == True:
                self.editNameMode = False
        return


    def function_addPlayer(MainWindow):

        if MainWindow.editNameMode == True:
            print('yoyo')
            return

        MainWindow.button_addPlayer.config(state=DISABLED)

        MainWindow.subWin = Tk()
        MainWindow.subWin.eval('tk::PlaceWindow . center')
        MainWindow.subWin.wm_title("Ajouter Joueur #%s" % (MainWindow.nbPlayer + 1))
        MainWindow.subWin.configure(background=MainWindow.Button_bg_color)
        MainWindow.subWin.resizable(False, False)

        MainWindow.subWin.emptylabel_1 = Label(MainWindow.subWin, padx=10, pady=10, bg=MainWindow.Button_bg_color)
        MainWindow.subWin.emptylabel_1.grid(row=0, column=0, columnspan=4)

        MainWindow.subWin.emptylabel_2 = Label(MainWindow.subWin, padx=10, pady=2, bg=MainWindow.Button_bg_color)
        MainWindow.subWin.emptylabel_2.grid(row=4, column=0, columnspan=4)

        if MainWindow.editNameMode == False:

            l = Label(MainWindow.subWin, text="Entrer le Nom du Joueur #%s" % (MainWindow.nbPlayer + 1),
                      font=("Helvetica", 12), bg=MainWindow.Button_bg_color, fg=MainWindow.Button_ft_color)
            l.grid(row=1, column=0, columnspan=1, padx=50, pady=10)

            MainWindow.subWin.errorStatus = Label(MainWindow.subWin, text="", bg=MainWindow.Button_bg_color, fg="cyan")
            MainWindow.subWin.errorStatus.grid(row=2, column=1, columnspan=1, padx=1, pady=10, sticky="n")

            MainWindow.subWin.input_Name = Entry(MainWindow.subWin, width=20, bg='black', fg='yellow', borderwidth=3,
                                                 font=("Helvetica", 16), justify='center')

            MainWindow.subWin.input_Name.grid(row=1, column=1, columnspan=1)

            MainWindow.subWin.button_commitAddPlayer = Button(MainWindow.subWin, text="Enregistrer", padx=10, pady=5,
                                                              font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                                              fg="yellow", command=MainWindow.commitAddPlayer,
                                                              activebackground=MainWindow.activeButton_bg_color,
                                                              activeforeground=MainWindow.activeButton_ft_color)

            MainWindow.subWin.button_cancel = Button(MainWindow.subWin, text="Annuler", padx=10, pady=5,
                                                     font=("Helvetica", 12), bg=MainWindow.Button_bg_color,
                                                     fg=MainWindow.Button_ft_color,
                                                     activebackground=MainWindow.activeButton_bg_color,
                                                     activeforeground=MainWindow.activeButton_ft_color,
                                                     command=lambda: MainWindow.destroySubWin())

            MainWindow.subWin.button_commitAddPlayer.grid(row=3, column=1, columnspan=1)
            MainWindow.subWin.button_cancel.grid(row=3, column=0, columnspan=1)

            MainWindow.subWin.bind("<Return>", lambda event: MainWindow.commitAddPlayer())
            MainWindow.subWin.after(1, lambda: MainWindow.subWin.focus_force())
            MainWindow.subWin.after(1, lambda: MainWindow.subWin.input_Name.focus_force())

        return

    def destroySubWin(MainWindow):
        MainWindow.button_addPlayer.config(state=NORMAL)
        MainWindow.subWin.destroy()
        return


    def commitAddPlayer(MainWindow):
        # A class "Game" with its properties must be sent to this function
        # Transfer created player to the Lobby
        playerName = MainWindow.subWin.input_Name.get()

        if playerName == "":
            MainWindow.subWin.errorStatus.configure(text="Vous devez entrer un nom... ")
            return

        if MainWindow.nbPlayer == 0:
            MainWindow.button_gameStart.configure(state="normal", fg="#60ff30")

            MainWindow.player_1_label_1.config(state=NORMAL)
            MainWindow.player_1_label_1.delete(0, END)
            MainWindow.player_1_label_1.insert(0, playerName)
            MainWindow.player_1_label_1.config(state=DISABLED, disabledforeground="yellow")
            MainWindow.frame3.configure(relief='raised')
            updateStatusLabeltext = "Ajouter un deuxième joueur OU Cliquer Démarrer Partie!"

        if MainWindow.nbPlayer == 1:
            MainWindow.player_2_label_1.config(state=NORMAL)
            MainWindow.player_2_label_1.delete(0, END)
            MainWindow.player_2_label_1.insert(0, playerName)
            MainWindow.player_2_label_1.config(state=DISABLED, disabledforeground="yellow")
            MainWindow.frame4.configure(relief='raised')
            updateStatusLabeltext = "Ajouter un troisième joueur OU Cliquer Démarrer Partie!"

        if MainWindow.nbPlayer == 2:
            MainWindow.player_3_label_1.config(state=NORMAL)
            MainWindow.player_3_label_1.delete(0, END)
            MainWindow.player_3_label_1.insert(0, playerName)
            MainWindow.player_3_label_1.config(state=DISABLED, disabledforeground="yellow")
            MainWindow.frame5.configure(relief='raised')
            updateStatusLabeltext = "Ajouter un quatrième joueur OU Cliquer Démarrer Partie!"

        if MainWindow.nbPlayer == 3:
            MainWindow.player_4_label_1.config(state=NORMAL)
            MainWindow.player_4_label_1.delete(0, END)
            MainWindow.player_4_label_1.insert(0, playerName)
            MainWindow.player_4_label_1.config(state=DISABLED, disabledforeground="yellow")
            MainWindow.frame6.configure(relief='raised')
            updateStatusLabeltext = "Cliquer Démarrer Partie!"

        MainWindow.nbPlayer += 1
        print(MainWindow.nbPlayer)
        MainWindow.function_updateStatusLabel(updateStatusLabeltext)
        MainWindow.function_refreshImages()
        MainWindow.subWin.destroy()
        MainWindow.button_addPlayer.config(state=NORMAL)

        if MainWindow.nbPlayer >= 4:
            MainWindow.button_addPlayer.configure(state=DISABLED)

        return

    def function_gameStart(self):
        if ~self.gameStarted:
            self.frame9.configure(borderwidth=0)
            self.button_gameStart.configure(borderwidth=0)
            print(self.gameStarted)
            self.button_gameStart.configure(state=DISABLED, disabledforeground=self.Button_bg_color)
            self.button_addPlayer.configure(state=DISABLED)

            if self.nbPlayer != 0:
                if self.nbPlayer == 1:
                    self.player_1_label_2.config(state=NORMAL)
                    self.player_1_label_2.config(state=DISABLED, disabledforeground="yellow")

                    self.playerIndex = [1, 1]

                if self.nbPlayer == 2:
                    self.player_2_label_2.config(state=NORMAL)
                    self.player_2_label_2.config(state=DISABLED, disabledforeground="yellow")
                    self.player_1_label_2.config(state=NORMAL)
                    self.player_1_label_2.config(state=DISABLED, disabledforeground="yellow")

                    self.playerIndex = [1, 2]

                if self.nbPlayer == 3:
                    self.player_3_label_2.config(state=NORMAL)
                    self.player_3_label_2.config(state=DISABLED, disabledforeground="yellow")
                    self.player_2_label_2.config(state=NORMAL)
                    self.player_2_label_2.config(state=DISABLED, disabledforeground="yellow")
                    self.player_1_label_2.config(state=NORMAL)
                    self.player_1_label_2.config(state=DISABLED, disabledforeground="yellow")

                    self.playerIndex = [1, 3]

                if self.nbPlayer == 4:
                    self.player_4_label_2.config(state=NORMAL)
                    self.player_4_label_2.config(state=DISABLED, disabledforeground="yellow")
                    self.player_3_label_2.config(state=NORMAL)
                    self.player_3_label_2.config(state=DISABLED, disabledforeground="yellow")
                    self.player_2_label_2.config(state=NORMAL)
                    self.player_2_label_2.config(state=DISABLED, disabledforeground="yellow")
                    self.player_1_label_2.config(state=NORMAL)
                    self.player_1_label_2.config(state=DISABLED, disabledforeground="yellow")

                    self.playerIndex = [1, 4]

        self.updateIndexLog()
        self.gameStarted = True
        self.button_editScore.config(state=NORMAL)
        self.button_editName.config(state=NORMAL)
        self.button_endTurn.configure(state=NORMAL)
        self.function_refreshImages()
        self.function_updateStatusLabel("La Partie est commencée!")

        return

    def function_endTurn(self):
        if self.gameStarted == True:

            print(self.playerIndex)
            self.button_endTurn.configure(state=DISABLED) #De-activate button for safety

            # get Current Player turn over the total nb of player
            currentPlayer = self.playerIndex[:1]  # Who is playing
            totalPlayer = self.playerIndex[1:] # Total number of players

            if currentPlayer < totalPlayer:
                if currentPlayer == [1]: # if player #1 turn
                    self.playerIndex[0] = 2
                if currentPlayer == [2]:
                    self.playerIndex[0] = 3
                if currentPlayer == [3]:
                     self.playerIndex[0] = 4
                if currentPlayer == [4]:
                    self.playerIndex[0] = 1

            if currentPlayer == totalPlayer:
                self.playerIndex[0] = 1

            #if this is the last player to play, the log "game turn" is updated by 1  **To be removed...
            currentGameTurn = self.turnIndexLog['gameTurn'].iloc[-1]
            if currentPlayer == totalPlayer:
                currentGameTurn += 1
                toAppend = pd.DataFrame([[currentGameTurn]], columns=['gameTurn'])
                self.turnIndexLog = pd.concat([self.turnIndexLog, toAppend])

            self.arrowImage.grid_forget()
            self.button_endTurn.configure(state=NORMAL)
            self.function_refreshImages()

        return


if __name__ == "__main__":

    def function_restartBoard():
        root.destroy()
        initializeWindow()

    def center(win):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    def initializeWindow():
        global root
        root = Tk()
        root.title("Score Board")
        root.geometry("1125x875")
        center(root)
        root.resizable(False, False)
        root.iconbitmap("dart_icon.ico")
        root.configure(background="#245042")
        # Call Constructor
        e = MainWindow(root)
        # The GUI is acting like a listening... Constantly waiting for something to happen.

    initializeWindow()
    root.mainloop()


