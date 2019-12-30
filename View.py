from Game import Game
from tkinter import *
from tkinter import ttk


class View(object):
    def __init__(self, gm, gs):
        self.gm = gm
        self.root = Tk()
        self.gs = gs
        self.root.title("Welcome to Fluxx!")
        # set up the frame
        self.frame = ttk.Frame(self.root, padding="3 3 12 12")
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def game_select(self):
        # generate and grid the buttons
        for i in range(len(self.gs)):
            game = self.gs[i]
            b = ttk.Button(self.frame, text=game, command=lambda game=game: self.get_player_num(game))
            b.grid(column=i, row=2)
        # generate and grid the label
        ltitle = ttk.Label(self.frame, text="Please pick a game to play!")
        ltitle.grid(column=0, row=0, columnspan=len(self.gs))
        self.root.mainloop()

    def get_player_num(self, game):
        self.clear_frame()
        # get player number
        for i in range (game.minPlayers, game.maxPlayers+1):
            b = ttk.Button(self.frame, text=i, command=lambda j=i: self.get_names(j))
            b.grid(column=i, row=2)
        ltitle = ttk.Label(self.frame, text="Please select number of players")
        ltitle.grid(column=0, row=0, columnspan=game.maxPlayers - game.minPlayers + 1)

    def get_names(self, num):
        print(num)
        self.clear_frame()
        ltitle = ttk.Label(self.frame, text="Enter player names")
        ltitle.grid(column=0, row=0, columnspan=2)
        entries = []
        for i in range(num):
            pl = ttk.Label(self.frame, text=f"Player {i+1}")
            pl.grid(column=0, row=i+1)
            pb = ttk.Entry(self.frame)
            pb.grid(column=1, row=i+1)
            entries.append(pb)
        submit = ttk.Button(self.frame, text="Play!", command=lambda: self.start_game(entries))
        submit.grid(column=1, row=num+1)

    def start_game(self, entries):
        players = []
        for e in entries:
            players.append(e.get())
            if players[-1] == "": players[-1] = f"Player {len(players)}"
        print(players)


    def clear_frame(self):
        for c in self.frame.winfo_children():
            c.destroy()
        print ("frame cleared")