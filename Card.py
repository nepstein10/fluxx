from PIL import ImageTk, Image
from pathlib import Path
from tkinter import ttk

class Card(object):
    # name: string
    def __init__(self, name):
        self.name = name
        path = str(Path(__file__).parent.absolute())
        self.imglbl = ttk.Label()
        self.img = ImageTk.PhotoImage(Image.open(f"{path}/cimgs/{self.name}.jpg").resize((70, 60)), master=self.imglbl)
        img = ImageTk.PhotoImage(Image.open(f"{path}/cimgs/{self.name}.jpg").resize((70, 60)))
        self.imglbl['image'] = img


    def on_play(self, player, g):
        print (f"Played {self.name}")

    def __repr__(self):
        return self.name


class NRule(Card):
    # name: string, game: Game, rules: int list ([draws, plays, hlim, klim])
    def __init__(self, name, rules):
        super().__init__(name)
        self.rules = rules

    # update the game rules with card-specific rules
    def on_play(self, player, g):
        super().on_play(player, g)
        g.ruleManager.add_rule(self)

class Action(Card):
    # name: string, game: Game, action: function (from actions list in Deck)
    def __init__(self, name, action):
        super().__init__(name)
        self.action = action

    # do the action - still to implement
    def on_play(self, player, g):
        super().on_play(player, g)
        self.action(self, player, g)
        g.deck.discard.append(self)


class Keeper(Card):
    # name: string, game: Game, kID: int
    def __init__(self, name, kID):
        super().__init__(name)
        self.kID = kID

    # play the keeper
    def on_play(self, player, g):
        super().on_play(player, g)
        player.keepers.append(self)


class Goal(Card):
    #special cases (5 keepers, 10 CiH) not built in yet, and not compatible
        # aslo not compatible are expansion goals of "either/or" potentially
    # name: string, game: Game, wCon: int list (the keepers needed to win)
    def __init__(self, name, wCon):
        super().__init__(name)
        self.wCon = wCon

    # play the goal
    def on_play(self, player, g):
        super().on_play(player, g)
        if not g.ruleManager.double_ag:
            g.goals = []
        g.goals.append(self)