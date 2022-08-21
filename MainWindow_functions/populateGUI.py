from tkinter import *
import centerWindow as cW
from PIL import ImageTk, Image


def populateGUI(self, master):
    master.configure(bg=self.Button_bg_color)
    master.title("Score Board")
    master.geometry("1125x875")
    master.resizable(False, False)
    master.iconbitmap("dart_icon.ico")
    cW.centerWindow(master)

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
    self.arrowLabel_3.grid(row=7, column=5, rowspan=2, columnspan=3, ipady=10)

    # Turn arrow panel for player 4
    self.arrowLabel_4 = Label(master, padx=10, pady=0, bg=self.Button_bg_color)
    self.arrowLabel_4.grid(row=7, column=9, rowspan=2, columnspan=3, ipady=10)

    # End turn button frame
    self.frame7 = LabelFrame(master, padx=10, pady=5, bg=self.Button_bg_color)
    self.frame7.grid(row=10, column=2, columnspan=1)

    # player 1 frame
    self.frame_player_1 = LabelFrame(master, padx=30, pady=20, bg=self.Button_bg_color)
    self.frame_player_1.grid(row=5, column=5, columnspan=4, rowspan=3)

    # player 2 frame
    self.frame_player_2 = LabelFrame(master, padx=30, pady=20, bg=self.Button_bg_color)
    self.frame_player_2.grid(row=5, column=9, columnspan=4, rowspan=3)

    # player 3 frame
    self.frame_player_3 = LabelFrame(master, padx=30, pady=20, background=self.Button_bg_color)
    self.frame_player_3.grid(row=7, column=5, columnspan=4, rowspan=8)

    # fourth player 4 frame
    self.frame_player_4 = LabelFrame(master, padx=30, pady=20, bg=self.Button_bg_color)
    self.frame_player_4.grid(row=7, column=9, columnspan=4, rowspan=8)

    # --------------------------------------------------------------------------------------------------------------
    #   CREATING BUTTONS
    # --------------------------------------------------------------------------------------------------------------

    # Define buttons

    self.button_0 = Button(self.frame1, text="0", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(0),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_1 = Button(self.frame1, text="1", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(1),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_2 = Button(self.frame1, text="2", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(2),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_3 = Button(self.frame1, text="3", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(3),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_4 = Button(self.frame1, text="4", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(4),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_5 = Button(self.frame1, text="5", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(5),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_6 = Button(self.frame1, text="6", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(6),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_7 = Button(self.frame1, text="7", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(7),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_8 = Button(self.frame1, text="8", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(8),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_9 = Button(self.frame1, text="9", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(9),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_commitScore = Button(self.frame1, text="Soumettre", padx=100, pady=20, font=("Helvetica", 25),
                                     bg=self.Button_bg_color, fg="yellow", command=self.commitScore,
                                     activebackground=self.activeButton_bg_color,
                                     activeforeground=self.activeButton_ft_color,
                                     state="disabled")

    self.button_clear = Button(self.frame1, text="C", padx=99.49999, pady=20, font=("Helvetica", 25),
                               bg=self.Button_bg_color, fg=self.Button_ft_color, command=self.clearClickPad,
                               activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_addPlayer = Button(self.frame0, text="Ajouter Joueur", padx=35, pady=3, font=("Helvetica", 12),
                                   bg=self.Button_bg_color, fg=self.Button_ft_color, command=self.addPlayer,
                                   activebackground=self.activeButton_bg_color,
                                   activeforeground=self.activeButton_ft_color)

    self.button_gameMode = Button(self.frame0, text="Mode de Jeu", padx=35, pady=3, font=("Helvetica", 12),
                                  bg=self.Button_bg_color, fg=self.Button_ft_color, state='normal',
                                  command=self.function_gameMode,
                                  activebackground=self.activeButton_bg_color,
                                  activeforeground=self.activeButton_ft_color)

    self.button_editScore = Button(self.frame0, text="Modifier Pointage", padx=20, pady=3, font=("Helvetica", 12),
                                   bg=self.Button_bg_color, fg=self.Button_ft_color, command=self.editScore,
                                   activebackground=self.activeButton_bg_color,
                                   activeforeground=self.activeButton_ft_color,
                                   state="disabled")

    self.button_editName = Button(self.frame0, text="Renommer Joueur", padx=20, pady=3, font=("Helvetica", 12),
                                  bg=self.Button_bg_color, fg=self.Button_ft_color, state=DISABLED,
                                  command=self.editName,
                                  activebackground=self.activeButton_bg_color,
                                  activeforeground=self.activeButton_ft_color)

    self.button_gameStart = Button(self.frame9, text="Démarrer Partie!", padx=40, pady=5,
                                   font=("Helvetica", 14, "bold"),
                                   bg=self.Button_bg_color, fg=self.Button_ft_color, command=self.startGame,
                                   activebackground=self.activeButton_bg_color,
                                   activeforeground=self.activeButton_ft_color, state="disabled")

    self.button_endTurn = Button(self.frame7, text="Tour terminé", padx=40, pady=5, font=("Helvetica", 12),
                                 bg=self.Button_bg_color, fg=self.Button_ft_color,
                                 command=self.endTurn, state="disabled",
                                 activebackground=self.activeButton_bg_color,
                                 activeforeground=self.activeButton_ft_color)

    # self.button_goBack = Button(master, text="<<", padx=5, pady=1, font=("Helvetica", 10),
    #                           bg=self.Button_bg_color, fg=self.Button_ft_color, state="normal", relief="groove",
    #                          activebackground=self.activeButton_bg_color,
    #                         activeforeground=self.activeButton_ft_color)

    # self.button_forward = Button(master, text=">>", padx=5, pady=1, font=("Helvetica", 10),
    #                            bg=self.Button_bg_color, fg=self.Button_ft_color, state="normal", relief="groove",
    #                           activebackground=self.activeButton_bg_color,
    #                          activeforeground=self.activeButton_ft_color)

    self.button_quit = Button(master, text="Quitter", padx=40, pady=5, font=("Helvetica", 12),
                              bg=self.Button_bg_color, fg=self.Button_ft_color,
                              activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color,
                              command=master.quit)

    self.button_restartBoard = Button(master, text="Réinitialiser Jeu", padx=40, pady=5, font=("Helvetica", 12),
                               bg=self.Button_bg_color, fg=self.Button_ft_color, command=self.resetBoard(master), state= DISABLED,
                               activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    # Put the buttons on the screen
    self.button_0.grid(row=4, column=0)
    self.button_1.grid(row=3, column=0)
    self.button_2.grid(row=3, column=1)
    self.button_3.grid(row=3, column=2)
    self.button_4.grid(row=2, column=0)
    self.button_5.grid(row=2, column=1)
    self.button_6.grid(row=2, column=2)
    self.button_7.grid(row=1, column=0)
    self.button_8.grid(row=1, column=1)
    self.button_9.grid(row=1, column=2)
    self.button_commitScore.grid(row=5, column=0, columnspan=3)
    self.button_clear.grid(row=4, column=1, columnspan=2)
    self.button_addPlayer.grid(row=0, column=0, columnspan=1)
    self.button_gameMode.grid(row=0, column=2, columnspan=1)
    self.button_editScore.grid(row=0, column=3, columnspan=1)
    self.button_editName.grid(row=0, column=4, columnspan=1)
    self.button_endTurn.grid(row=0, column=0, columnspan=1)
    self.button_gameStart.grid(row=0, column=3, columnspan=1)
    #self.button_goBack.grid(row=13, column=5, ipadx=5, columnspan=1, sticky="SE")
    #self.button_forward.grid(row=13, column=6, ipadx=5, columnspan=1, sticky="SW")
    self.button_restartBoard.grid(row=13, column=10, columnspan=1, sticky="SE")
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
    self.player_1_label_1 = Entry(self.frame_player_1, width=16, bg=self.Button_bg_color, fg="grey", borderwidth=0,
                                  font=("Helvetica", 14),
                                  justify='center', disabledbackground=self.Button_bg_color,
                                  disabledforeground="grey")

    self.player_1_label_2 = Entry(self.frame_player_1, width=6, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                  font=("Helvetica", 30),
                                  justify='center', disabledbackground=self.Button_bg_color,
                                  disabledforeground="grey")

    self.player_1_label_3 = Entry(self.frame_player_1, width=10, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                  font=("Helvetica", 8),
                                  justify='right', disabledbackground=self.Button_bg_color,
                                  disabledforeground="grey", border=0)

    self.player_1_label_4 = Entry(self.frame_player_1, width=10, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                  font=("Helvetica", 8),
                                  justify='right', disabledbackground=self.Button_bg_color,
                                  disabledforeground="grey", border=0)

    # self.player_1_checkbox = Checkbutton(self.frame_player_1, text='DoubleIn', onvalue=1, offvalue=0,
    #                                     font=("Helvetica", 8), bg=self.Button_bg_color, fg="grey")

    self.player_1_label_1.grid(row=0, column=0)
    self.player_1_label_1.insert(0, "Ajoutez le Joueur #1")
    self.player_1_label_1.config(state=DISABLED)

    self.player_1_label_2.grid(row=2, column=0, pady=10)
    self.player_1_label_2.insert(0, "501")
    self.player_1_label_2.config(state=DISABLED)

    # self.player_1_checkbox.grid(row=3, column=0, pady=0, sticky='SW')

    self.player_1_label_3.grid(row=4, column=0, pady=0, sticky='SW')
    self.player_1_label_3.insert(0, "Avr:")
    self.player_1_label_3.config(state=DISABLED)

    self.player_1_label_4.grid(row=5, column=0, pady=0, sticky='SW')
    self.player_1_label_4.insert(0, "HighScore:")
    self.player_1_label_4.config(state=DISABLED)

    # Second Player Name and Score
    self.player_2_label_1 = Entry(self.frame_player_2, width=16, bg=self.Button_bg_color, fg="grey", borderwidth=0,
                                  font=("Helvetica", 14),
                                  justify='center', disabledbackground=self.Button_bg_color,
                                  disabledforeground="grey")
    self.player_2_label_2 = Entry(self.frame_player_2, width=6, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                  font=("Helvetica", 30),
                                  justify='center', disabledbackground=self.Button_bg_color,
                                  disabledforeground="grey")

    self.player_2_label_3 = Entry(self.frame_player_2, width=10, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                  font=("Helvetica", 8),
                                  justify='right', disabledbackground=self.Button_bg_color,
                                  disabledforeground="grey", border=0)

    self.player_2_label_4 = Entry(self.frame_player_2, width=10, bg=self.Button_bg_color, fg="grey", borderwidth=1,
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
    self.player_3_label_1 = Entry(self.frame_player_3, width=16, bg=self.Button_bg_color, fg="grey", borderwidth=0,
                                  font=("Helvetica", 14),
                                  justify='center', disabledbackground=self.Button_bg_color,
                                  disabledforeground="grey")
    self.player_3_label_2 = Entry(self.frame_player_3, width=6, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                  font=("Helvetica", 30),
                                  justify='center', disabledbackground=self.Button_bg_color,
                                  disabledforeground="grey")

    self.player_3_label_3 = Entry(self.frame_player_3, width=10, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                  font=("Helvetica", 8),
                                  justify='right', disabledbackground=self.Button_bg_color,
                                  disabledforeground="grey", border=0)

    self.player_3_label_4 = Entry(self.frame_player_3, width=10, bg=self.Button_bg_color, fg="grey", borderwidth=1,
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
    self.player_4_label_1 = Entry(self.frame_player_4, width=16, bg=self.Button_bg_color, fg="grey", borderwidth=0,
                                  font=("Helvetica", 14),
                                  justify='center', disabledbackground=self.Button_bg_color,
                                  disabledforeground="grey")
    self.player_4_label_2 = Entry(self.frame_player_4, width=6, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                  font=("Helvetica", 30),
                                  justify='center', disabledbackground=self.Button_bg_color,
                                  disabledforeground="grey")

    self.player_4_label_3 = Entry(self.frame_player_4, width=10, bg=self.Button_bg_color, fg="grey", borderwidth=1,
                                  font=("Helvetica", 8),
                                  justify='right', disabledbackground=self.Button_bg_color,
                                  disabledforeground="grey", border=0)

    self.player_4_label_4 = Entry(self.frame_player_4, width=10, bg=self.Button_bg_color, fg="grey", borderwidth=1,
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
    self.StatusLabel = Label(self.emptylabel0, padx=1, pady=20, text="Ajoutez au moins un Joueur!",
                                   font=("Helvetica", 12), bg=self.Button_bg_color,
                                   fg="cyan")
    self.StatusLabel.grid(row=0, column=0)

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

    return
