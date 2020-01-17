from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from pathlib import Path


class View(object):
    # gs: Game[]
    def __init__(self, gs):
        self.gs = gs
        self.game = None

        self.root = Tk()
        self.root.title("Welcome to Fluxx!")
        # set up the frame
        self.frame = ttk.Frame(self.root, padding="3 3 12 12")
        self.frame.grid(column=0, row=0, sticky=NSEW)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        path = str(Path(__file__).parent.absolute())
        self.brules_img = ImageTk.PhotoImage(Image.open(f"{path}/cimgs/Draw 1, Play 1.jpg").resize((70, 60)))
        self.notifytext = "This is Fluxx in progress!"

    # These next 4 methods are the sequence of views that start the game.
    #   Maybe the data should be factored out of here and through the manager?
    def game_select(self):
        self.new_game()
        self.root.mainloop()

    def new_game(self):
        self.clear_frame(self.frame)
        # generate and grid the buttons
        for i in range(len(self.gs)):
            game = self.gs[i]
            b = ttk.Button(self.frame, text=game, command=lambda game=game: self.get_player_num(game))
            b.grid(column=i, row=2)
        # generate and grid the label
        ltitle = ttk.Label(self.frame, text="Please pick a game to play!")
        ltitle.grid(column=0, row=0, columnspan=len(self.gs))

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
    #   g: Game
    def game_board(self, g):
        self.clear_frame(self.frame)
        self.frame.master.geometry(f"{len(g.players)*200 + 100}x400")
        bs = ttk.Style()
        bs.configure('Bordered.TFrame', background="black", height=100)
        # The player frame, with an inner frame for each player
        #  displaying name, hand size, and keepers
        pframe = ttk.Frame(self.frame, padding="3 12")
        pframe.grid(column=0, row=0, sticky=N)
        for i in range(len(g.players)):
            iframe = ttk.Frame(pframe, height=100, padding=3,
                               borderwidth=1, relief="sunken",
                               style='Bordered.TFrame')
            iframe.grid(column=i, row=0)
            p = g.players[i]
            # label of the player's name
            ilbl = ttk.Label(iframe, text=p.name)
            ilbl.grid(row=0, columnspan=len(p.keepers)+1)
            # indication of hand size
            hlbl = ttk.Label(iframe, text=f"H: {len(p.hand)}")
            hlbl.grid(column=0, row=1)
            # representation of each keeper
            for j in range(len(p.keepers)):
                klbl = ttk.Label(iframe, image=p.keepers[j].img)
                klbl.grid(column=j+1, row=1)
        # The rules frame, with a representation of each rule card
        rframe = ttk.Frame(self.frame, height=100, padding=3,
                           borderwidth=1, relief="sunken",
                           style='Bordered.TFrame')
        rframe.grid(column=0, row=1, sticky=W)
        rlabel = ttk.Label(rframe, text="Rules:")
        rlabel.grid(column=0, row=0, sticky=W)
        brules = ttk.Label(rframe, image=self.brules_img)
        brules.grid(column=0, row=1, sticky=W)
        for i in range(len(g.ruleManager.rules)):
            rlbl = ttk.Label(rframe, image=g.ruleManager.rules[i].img)
            rlbl.grid(column=i+1,row=1)
        # The goal(s), below the rules on the left
        gframe = ttk.Frame(self.frame, padding="3",
                           borderwidth=1, relief="sunken",
                           style='Bordered.TFrame')
        gframe.grid(column=0, row=2, sticky=W)
        glabel = ttk.Label(gframe, text="Goal(s):")
        glabel.grid(column=0, row=0, sticky=W)
        for i in range(len(g.goals)):
            glbl = ttk.Label(gframe, image=g.goals[i].img)
            glbl.grid(column=i+1, row=0)
        notify = ttk.Label(self.frame, text=self.notifytext)
        notify.grid(column=0, row=8, columnspan=3)
        if g.winner:
            ngb = ttk.Button(self.frame, text="New Game?", command=self.new_game)
            ngb.grid(column=3, row=10)
            qbutton = ttk.Button(self.frame, text="Quit", command=self.root.destroy)
            qbutton.grid(column=4, row=10)

    # Select a card from the list passed in and return it
    #   li: a list of Card objects to pick from
    #   st: a string to give instructions (label)
    #   fn: the function to continue with
    #   p: the Player who's choosing a card
    # Feeds to ret_card
    #   Will popping the card remove it from the list successfully?
    def pick_card(self, p, li, st, fn):
        print("starting pick_card")
        if not len(li):
            raise IndexError
        window = Tk()
        window.title(st)
        fr = ttk.Frame(window, padding="3 3 12 12")
        fr.grid(column=0, row=0, sticky=NSEW)
        lbl = ttk.Label(fr, text=f"{p}, {st}")
        lbl.grid(column=0, row=0, columnspan=len(li))
        for i in range(len(li)):
            b = ttk.Button(fr, text=li[i], command=lambda i=i: self.ret_card(p, li.pop(i), window, fn))
            b['image'] = li[i].img
            b.grid(column=i, row=1)
        window.geometry(f"{max(len(li)*150, 400)}x50+500+250")
        window.mainloop()
        print("done pick_card")

    # Close the window and pass the card to fn
    #   p (Player): the Player choosing the card
    #   c (Card): the card chosen
    #   window (Tk): the chose card window to close
    #   fn (function): the function to pass the card to
    def ret_card(self, p, c, window, fn):
        print(f"chose {c}")
        window.destroy()
        # call the function to pass the card to. current fn(s):
        #   Game.run_play
        fn(p, c)

    def clear_frame(self, frame):
        for c in frame.winfo_children():
            c.destroy()
        print ("frame cleared")