from Card import *
from random import shuffle

class Deck(object):
    # g: Game
    def __init__(self):
        self.pile = []
        self.discard = []

    # randomize the order of the cards in the deck (maybe factor this out)
    def shuffle(self):
        shuffle(self.pile)

    # Card list; cards: int (number of cards to deal)
    def deal(self, cards):
        dealt = []
        for i in range(cards):
            # Nothing to draw -> reshuffle
            if not len(self.pile):
                print("reshuffling discard")
                print(self.discard)
                list(map(self.pile.append, self.discard))
                self.discard = []
                self.shuffle()
            dealt.append(self.pile.pop(0))
        return dealt


class SampleFluxxDeck(Deck):
    def __init__(self):
        super().__init__()
        # list of actions -- maybe try to put this in a different file
        actions = [lambda: print("RR not implemented")]
        # list of cards -- also relocate to clean if possible
        cards = [NRule("Draw 2", [2, None, None, None]),
                 NRule("Draw 3", [3, None, None, None]),
                 NRule("Play 2", [None, 2, None, None]),
                 NRule("Play 3", [None, 3, None, None]),
                 NRule("Play 4", [None, 4, None, None]),
                 NRule("Hand Limit 1", [None, None, 1, None]),
                 NRule("Keeper Limit 2", [None, None, None, 2]),
                 Action("Rules Reset", actions[0]),
                 Keeper("Chocolate", 0),
                 Keeper("Cookies", 1),
                 Keeper("Milk", 2),
                 Keeper("The Sun", 3),
                 Keeper("The Moon", 4),
                 Goal("Milk and Cookies", [[1, 2]]),
                 Goal("Chocolate Milk", [[0, 2]]),
                 Goal("Squishy Chocolate", [[0, 3]]),
                 Goal("Night and Day", [[3, 4]])]
        # set the pile to the cards, create an empty discard pile
        self.pile = cards