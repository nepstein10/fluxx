from Game import Game
from Tkinter import *
import ttk


class View(object):
    def __init__(self, gm, gs):
        self.gm = gm
        self.root = Tk()
        self.gs = gs

        # for child in f0.winfo_children():
        #     child.grid_configure(padx=5, pady=5)
        # root.mainloop()
        # f0 = ttk.Frame(root)
        # f0.grid(column=0, row=0, stick=(N,W,E,S))
        # ttk.Button(f0, text="YAY", command=self.celebrate)
        # root.mainloop()

    def game_select(self):
        self.root.title("Welcome to Fluxx!")
        f0 = ttk.Frame(self.root, padding="3 3 12 12")
        f0.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        # ideally figure out a way to get the buttons to generate automatically based on a list (in GameManager.py?)
        for i in range(len(self.gs)):
            print(self.gs[1])
            b = ttk.Button(f0, text=self.gs[i], command=lambda: self.get_player_info(i, f0))
            b.grid(column=i, row=2)
        ltitle = ttk.Label(f0, text="Please pick a game to play!")
        ltitle.grid(column=0, row=0, sticky=(W,E), columnspan=len(self.gs))
        self.root.mainloop()


    def get_player_info(self, gamenum, frame):
        print "hi"
        self.clear_frame(frame)
        gameopts = [self.gm.f3_1, self.gm.sample]
        self.people = []
        # add player name collection info
        ltitle = ttk.Label(frame, text="Please select number of players")

        b2 = ttk.Button(frame, text="2", command=lambda: self.get_names(2))
        # prompt = StringVar()
        # prompt.set("Please enter the name for Player {} or 'done':".format(len(self.people) + 1))
        # prlabel = ttk.Label(f0, textvariable=prompt)
        # newname = StringVar
        # nentry = ttk.Entry(f0, textvariable=newname)
        # addbutton = ttk.Button(f0, text="Add This Player", command=lambda: self.people.append(str(newname)))
        # donebutton = ttk.Button(f0, text="Play Game", command=gameopts[gamenum](self.people))


    def clear_frame(self, frame):
        for c in frame.winfo_children():
            c.destroy()
        print ("frame cleared")