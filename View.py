from Game import Game
from tkinter import *
from tkinter import ttk


class View(object):
    # gm: GameManager
    # gs: Game[]
    def __init__(self, gm, gs):
        self.gm = gm
        self.gs = gs
        self.game = None

        self.root = Tk()
        self.root.title("Welcome to Fluxx!")
        # set up the frame
        self.frame = ttk.Frame(self.root, padding="3 3 12 12")
        self.frame.grid(column=0, row=0, sticky=NSEW)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    # These next 4 methods are the sequence of views that start the game.
    #   Maybe the data should be factored out of here and through the manager?
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
        self.game = game
        self.clear_frame(self.frame)
        # get player number
        opts = game.maxPlayers+1-game.minPlayers
        for i in range (opts):
            b = ttk.Button(self.frame, text=game.minPlayers+i, command=lambda j=game.minPlayers+i: self.get_names(j))
            b.grid(column=i, row=2)
        ltitle = ttk.Label(self.frame, text="Please select number of players")
        ltitle.grid(row=0, columnspan=opts)

    def get_names(self, num):
        print(num)
        self.clear_frame(self.frame)
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
        self.game.start(players, self)

    # The board during game play
    #   players: a list of Player items
    #   goals: a list of Goal cards that are active
    #   rm: the Game's Rules object
    def game_board(self, players, goals, rm):
        # The player frame, with an inner frame for each player
        #  displaying name, hand size, and keepers
        self.clear_frame(self.frame)
        pframe = ttk.Frame(self.frame, padding="3 3 12 12")
        pframe.grid(column=0, row=0, sticky=N)
        for i in range(len(players)):
            iframe = ttk.Frame(pframe, padding="3 3 3 3")
            iframe.grid(column=i, row=0)
            p = players[i]
            # label of the player's name
            ilbl = ttk.Label(iframe, text=p.name)
            ilbl.grid(row=0, columnspan=len(p.keepers)+1)
            # indication of hand size
            hlbl = ttk.Label(iframe, text=f"H: {len(p.hand)}")
            hlbl.grid(column=0, row=1)
            # representation of each keeper
            for j in range(len(p.keepers)):
                klbl = ttk.Label(iframe, text=p.keepers[j])
                klbl.grid(column=j+1, row=1)
        # The rules frame, with a representation of each rule card
        rframe = ttk.Frame(self.frame, padding="3 3 12 12")
        rframe.grid(column=0, row=1)
        for i in range(len(rm.rules)):
            rlbl = ttk.Label(rframe, text=rm.rules[i])
            rlbl.grid(column=i,row=0)

    # Select a card from the list passed in and return it
    #   li: a list of Card objects to pick from
    #   st: a string to give instructions (label)
    # Feeds to ret_card
    #   Will popping the card remove it from the list successfully?
    def pick_card(self, li, st):
        if not len(li):
            raise IndexError
        window = Tk()
        window.title(st)
        fr = ttk.Frame(window, padding="3 3 12 12")
        fr.grid(column=0, row=0, sticky=NSEW)
        lbl = ttk.Label(fr, text=st)
        lbl.grid(column=0, row=0, columnspan=len(li))
        for i in range(len(li)):
            b = ttk.Button(fr, text=li[i], command=lambda i=i: self.ret_card(i, li, window))

    # pop the Card from the list, append None and the Card
    #   This allows the code to look for the trigger of the None
    #   Extremely clunky AND I DON'T LIKE IT
    def ret_card(self, i, li, window):
        window.destroy()
        temp = li.pop(i)
        li += [None,temp]

    def clear_frame(self, frame):
        for c in frame.winfo_children():
            c.destroy()
        print ("frame cleared")