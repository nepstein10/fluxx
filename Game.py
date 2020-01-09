from RulesManager import Rules
from Player import Player
import Decks

from abc import abstractmethod
import random
from time import sleep

class Game(object):
    # deck: the deck object
    def __init__(self, deck):
        self.ruleManager = Rules()
        self.deck = deck
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
    def __init__(self, deck):
        self.minPlayers = 2
        self.maxPlayers = 6
        super().__init__(deck)

    def start(self, players, view):
        self.view = view
        # generate players, pIDs starting at 10
        for i in range(len(players)):
            self.players.append(Player(self, players[i], i + 10))
        random.shuffle(self.players)
        print(self.players)
        self.setup()
        print (f"Starting {self}")
        self.gameon(self.players)

    def gameon(self, players):
        self.view.game_board(self.players, self.goals, self.ruleManager)
        sleep(.5)
        self.taketurn(players[self.turn % len(players)])
        if self.winner:
            print(f"{self.winner} wins!")
            self.view.root.destroy()
        else:
            self.gameon(players)


    # shuffle the deck and deal the starting 3 to each player
    def setup(self):
        self.deck.shuffle()
        for p in self.players:
            for c in self.deck.deal(3):
                p.hand.append(c)

    # player: Player (whose turn it is); process a player's turn
    def taketurn(self, player):
        print (f"{player}'s turn")
        # draw correct number of cards, add them to hand
        drawn = self.ruleManager.draws
        for c in self.deck.deal(drawn):
            player.hand.append(c)
            print (f"drew {c}")
        self.dtt = drawn
        # run correct number of plays
        self.ptt = 0
        self.run_play(player)
        tot_plays = self.ruleManager.get_plays()
        while played <= tot_plays and len(player.hand) > 0:
            # Player selects a card from the popup hand
            self.play(player)
            # this draws up to new draw rule and complies players w/ rules
            drawn = self.ruleManager.check_compliance(self, player, drawn)
            if self.check_win(): break
            self.view.game_board(self.players, self.goals, self.ruleManager)
            played += 1
            tot_plays = self.ruleManager.get_plays()
        self.turn += 1

    def run_play(self, player):
        self.dtt = self.ruleManager.check_compliance(self, player, self.dtt)
        tot_plays = self.ruleManager.get_plays()
        if self.ptt < tot_plays and len(player.hand) > 0:
            self.ptt += 1
            # Player selects a card from the popup hand
            card = player.choose_card("h", "Pick a card from your hand")
        else: self.turn += 1


    # player: Player; process an individual play
    # card: Card
    def play(self, player, card):
        card.on_play(player, self)

    # check all win conditions and players for victory
    ### THIS COULD PROBABLY BE MUCH MORE EFFICIENT IF ONLY CHECK CHANGED
    def check_win(self):
        for goal in self.goals:
            for wc in goal.wCon:
                for p in self.players:
                    if p.compwin(wc):
                        self.winner = p
                        return True
                    else: return False

class Fluxx3_1(Fluxx):
    def __init__(self, deck):
        super().__init__(deck)
        self.maxPlayers = 5

    def __repr__(self):
        return "Fluxx 3.1"

class FluxxSample(Fluxx):
    def __init__(self, deck):
        super().__init__(deck)
        self.maxPlayers = 3

    def __repr__(self):
        return "Fluxx Sample"