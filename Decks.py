from Card import *
from random import shuffle

class Deck(object):
    # g: Game
    def __init__(self, g):
        # list of actions -- maybe try to put this in a different file
        actions = [lambda g: None]
        # list of cards -- also relocate to clean if possible
        cards = [NRule("Draw 2", g, [2, None, None, None]),
                 NRule("Draw 3", g, [3, None, None, None]),
                 NRule("Play 2", g, [None, 2, None, None]),
                 NRule("Play 3", g, [None, 3, None, None]),
                 NRule("Play 4", g, [None, 4, None, None]),
                 NRule("Hand Limit 1", g, [None, None, 1, None]),
                 NRule("Keeper Limit 3", g, [None, None, None, 3]),
                 Action("Rules Reset", g, actions[0]),
                 Keeper("Chocolate", g, 0),
                 Keeper("Cookies", g, 1),
                 Keeper("Milk", g, 2),
                 Keeper("The Sun", g, 3),
                 Keeper("The Moon", g, 4),
                 Goal("Milk and Cookies", g, [[1,2]]),
                 Goal("Chocolate Milk", g, [[0,2]]),
                 Goal("Squishy Chocolate", g, [[0,3]]),
                 Goal("Night and Day", g, [[3,4]])]
        # set the pile to the cards, create an empty discard pile
        self.pile = cards
        self.discard = []

    # randomize the order of the cards in the deck (maybe factor this out)
    def shuffle(self):
        shuffle(self.pile)

    # Card list; cards: int (number of cards to deal)
    def deal(self, cards):
        dealt = []
        for i in range(cards):
            if len(self.pile) == 0:
                self.pile = self.discard
                self.shuffle()
            dealt.append(self.pile.pop(0))
        return dealt