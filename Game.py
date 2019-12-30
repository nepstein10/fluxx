from RulesManager import Rules
from Decks import *
from Player import Player


class Game(object):
    # people: string list (names of players)
    # deck: the deck object
    def __init__(self, people, deck):
        self.ruleManager = Rules()
        self.deck = deck
        self.players = []
        self.goals = []
        self.winner = None
        # generate players, pIDs starting at 10
        for i in range(len(people)):
            self.players.append(Player(self, people[i], i + 10))

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