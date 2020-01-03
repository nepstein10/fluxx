from RulesManager import Rules
from Player import Player
import Decks

from abc import abstractmethod
import random

class Game(object):
    # deck: the deck object
    def __init__(self, deck):
        self.ruleManager = Rules()
        self.deck = deck
        self.view = None
        self.players = []
        self.goals = []
        self.winner = None


class Fluxx(Game):
    def __init__(self, deck):
        self.minPlayers = 2
        self.maxPlayers = 6
        super().__init__(deck)

    @abstractmethod
    def start(self, players, view):
        self.view = view
        # generate players, pIDs starting at 10
        for i in range(len(players)):
            self.players.append(Player(self, players[i], i + 10))
        random.shuffle(self.players)
        print(self.players)
        self.setup()
        self.view.game_board(self.players, [], Rules())


    # shuffle the deck and deal the starting 3 to each player
    def setup(self):
        self.deck.shuffle()
        for p in self.players:
            for c in self.deck.deal(3):
                p.hand.append(c)

    # player: Player (whose turn it is); process a player's turn
    def turn(self, player):
        print (player)
        # draw correct number of cards, add them to hand
        drawn = self.ruleManager.draws
        for c in self.deck.deal(drawn):
            player.hand.append(c)
        # run correct number of plays
        p = 1
        while True:
            tot_plays = self.ruleManager.get_plays()
            if p <= tot_plays and len(player.hand) > 0:
                self.play(player)
                drawn = self.ruleManager.check_compliance(self, player, drawn)
                self.check_win()
                p += 1
            else:
                break
        player.end_turn()

    # player: Player; process an individual play
    def play(self, player):
        card = player.choose_card("h")
        card.on_play(player)

    # check all win conditions and players for victory
    ### THIS COULD PROBABLY BE MUCH MORE EFFICIENT IF ONLY CHECK CHANGED
    def check_win(self):
        for goal in self.goals:
            for wc in goal.wCon:
                for p in self.players:
                    if p.compwin(wc):
                        self.winner = p
            #             return True
            # return False

class Fluxx3_1(Fluxx):
    def __init__(self, deck):
        super().__init__(deck)
        self.maxPlayers = 5

    def start(self, players, view):
        super().start(players, view)
        d = Decks.Deck()
        print("starting 3.1")
        print(self)

    def __repr__(self):
        return "Fluxx 3.1"

class FluxxSample(Fluxx):
    def __init__(self, deck):
        super().__init__(deck)
        self.maxPlayers = 4

    def start(self, players, view):
        super().start(players, view)
        d = Decks.SampleFluxxDeck()
        print ("Starting SampleFluxx")
        print(self)

    def __repr__(self):
        return "Fluxx Sample"