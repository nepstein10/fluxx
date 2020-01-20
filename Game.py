from RulesManager import Rules
from Player import Player
from Decks import *

from abc import abstractmethod
import random
from time import sleep

class Game(object):
    # deck: the deck object
    def __init__(self):
        self.ruleManager = Rules(self)
        self.deck = None
        self.view = None
        self.players = []
        self.goals = []
        self.turn = 0
        self.winner = None
        self.ptt = 0
        self.dtt = 0

    @abstractmethod
    def start(self, players, view):
        print ("Not implemented yet")

class Fluxx(Game):
    def __init__(self):
        self.minPlayers = 2
        self.maxPlayers = 6
        super().__init__()

    def start(self, players, view):
        self.view = view
        # generate players, pIDs starting at 10
        self.players = []
        self.ruleManager = Rules(self)
        self.goals = []
        self.turn = 0
        self.winner = None
        self.ptt = 0
        self.dtt = 0
        for i in range(len(players)):
            self.players.append(Player(self, players[i], i + 10))
        random.shuffle(self.players)
        print(self.players)
        self.setup()
        print (f"Starting {self}")
        self.gameon()

    # shuffle the deck and deal the starting 3 to each player
    def setup(self):
        self.deck.shuffle()
        for p in self.players:
            for c in self.deck.deal(3):
                p.hand.append(c)

    def gameon(self,):
        self.start_turn(self.players[self.turn % len(self.players)])
        if self.winner:
            print(f"{self.winner} wins!")
            self.view.root.destroy()
        else:
            self.gameon()


    # player: Player (whose turn it is); process a player's turn
    def start_turn(self, player):
        self.view.notifytext = f"{player}'s turn"
        # draw correct number of cards, add them to hand
        #   KNOWN BUG: No limits check before drawing. Can result in empty deck
        drawn = self.ruleManager.draws
        for c in self.deck.deal(drawn):
            player.hand.append(c)
            print (f"drew {c}")
        self.dtt = drawn
        # run correct number of plays
        self.ptt = 0
        self.run_play(player)

    def run_play(self, player):
        self.ruleManager.ap = player
        self.ruleManager.ops = self.players.copy()
        self.ruleManager.ops.remove(player)
        self.ruleManager.draw_up(player, self.dtt)
        self.ruleManager.check_compliance()

    def cont_play(self, player):
        self.view.game_board(self)
        tot_plays = self.ruleManager.get_plays()
        if self.ptt < tot_plays and len(player.hand) > 0:
            self.ptt += 1
            # Player selects a card from the popup hand
            player.choose_card("h", "Pick a card from your hand to play", self.play)
        else:
            self.turn += 1
            self.gameon()


    # player: Player; process an individual play
    # card: Card
    def play(self, player, card):
        card.on_play(player, self)
        if self.check_win():
            self.view.game_board(self)
        else: self.run_play(player)


    # check all win conditions and players for victory
    ### THIS COULD PROBABLY BE MUCH MORE EFFICIENT IF ONLY CHECK CHANGED
    def check_win(self):
        for goal in self.goals:
            for wc in goal.wCon:
                for p in self.players:
                    if p.compwin(wc):
                        self.winner = p
                        self.view.notifytext = f"{p} wins!"
                        return True
        return False


class Fluxx3_0(Fluxx):
    def __init__(self):
        super().__init__()
        self.maxPlayers = 5

    def setup(self):
        self.deck = Fluxx3_0Deck()
        super().setup()

    def __repr__(self):
        return "Fluxx 3.0"

class FluxxSample(Fluxx):
    def __init__(self):
        super().__init__()
        self.maxPlayers = 3

    def setup(self):
        self.deck = SampleFluxxDeck()
        super().setup()

    def __repr__(self):
        return "Fluxx Sample"