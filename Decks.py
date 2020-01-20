from Card import *
from Actions import *
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
        actions = [lambda c, p, g: rules_reset(c, p, g)
                   ]
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

class Fluxx3_0Deck(Deck):
    def __init__(self):
        super().__init__()
        # list of actions -- maybe try to put this in a different file
        actions = [lambda c, p, g: dnd(c, p, g),
                   lambda c, p, g: d2_u2(c, p, g),
                   lambda c, p, g: d3_p2(c, p, g),
                   lambda c, p, g: empty_trash(c, p, g),
                   lambda c, p, g: eg1(c, p, g),
                   lambda c, p, g: exch_keeps(c, p, g),
                   lambda c, p, g: go_fish(c, p, g),
                   lambda c, p, g: inag(c, p, g),
                   lambda c, p, g: ldta(c, p, g),
                   lambda c, p, g: lsimplify(c, p, g),
                   lambda c, p, g: no_lims(c, p, g),
                   lambda c, p, g: r_hands(c, p, g),
                   lambda c, p, g: rules_reset(c, p, g),
                   lambda c, p, g: scr_keeps(c, p, g),
                   lambda c, p, g: st_keep(c, p, g),
                   lambda c, p, g: taturn(c, p, g),
                   lambda c, p, g: taxation(c, p, g),
                   lambda c, p, g: trade_hands(c, p, g),
                   lambda c, p, g: trash_keep(c, p, g),
                   lambda c, p, g: trash_nrule(c, p, g),
                   lambda c, p, g: usewytake(c, p, g)]
        # list of cards -- also relocate to clean if possible
        cards = [NRule("Draw 2", [2, None, None, None]),
                 NRule("Draw 3", [3, None, None, None]),
                 NRule("Draw 4", [4, None, None, None]),
                 NRule("Draw 5", [5, None, None, None]),
                 NRule("Play 2", [None, 2, None, None]),
                 NRule("Play 3", [None, 3, None, None]),
                 NRule("Play 4", [None, 4, None, None]),
                 NRule("Hand Limit 0", [None, None, 0, None]),
                 NRule("Hand Limit 1", [None, None, 1, None]),
                 NRule("Hand Limit 2", [None, None, 2, None]),
                 NRule("Keeper Limit 2", [None, None, None, 2]),
                 NRule("Keeper Limit 3", [None, None, None, 3]),
                 NRule("Keeper Limit 4", [None, None, None, 4]),
                 NRule("Double Agenda", [None, None, None, None]),#
                 NRule("Reverse Order", [None, None, None, None]),#
                 NRule("First Play Random", [None, None, None, None]),#
                 NRule("No-Hand Bonus", [None, None, None, None]),#
                 NRule("Poor Bonus", [None, None, None, None]),#
                 NRule("Rich Bonus", [None, None, None, None]),#
                 NRule("Double Agenda", [None, None, None, None]),#
                 Action("Discard and Draw", actions[0]),
                 Action("Draw 2 & Use 'Em", actions[1]),
                 Action("Draw 3, Play 2", actions[2]),
                 Action("Empty the Trash", actions[3]),
                 Action("Everybody Gets 1", actions[4]),
                 Action("Exchange Keepers", actions[5]),
                 Action("Go Fish", actions[6]),
                 Action("I Need a Goal", actions[7]),
                 Action("Let's Do That Again", actions[8]),
                 Action("Let's Simplify", actions[9]),
                 Action("No Limits", actions[10]),
                 Action("Rotate Hands", actions[11]),
                 Action("Rules Reset", actions[12]),
                 Action("Scramble Keepers", actions[13]),
                 Action("Steal a Keeper", actions[14]),
                 Action("Take Another Turn", actions[15]),
                 Action("Taxation", actions[16]),
                 Action("Trade Hands", actions[17]),
                 Action("Trash a Keeper", actions[18]),
                 Action("Trash a New Rule", actions[19]),
                 Action("Use What You Take", actions[20]),
                 Keeper("The Brain", 0),
                 Keeper("Bread", 1),
                 Keeper("Chocolate", 2),
                 Keeper("Cookies", 3),
                 Keeper("Death", 4),
                 Keeper("Dreams", 5),
                 Keeper("Love", 6),
                 Keeper("Milk", 7),
                 Keeper("Money", 8),
                 Keeper("The Moon", 9),
                 Keeper("Peace", 10),
                 Keeper("The Rocket", 11),
                 Keeper("Sleep", 12),
                 Keeper("The Sun", 13),
                 Keeper("The Television", 14),
                 Keeper("Time", 15),
                 Keeper("The Toaster", 16),
                 Keeper("War", 17),
                 Goal("10 Cards in Hand", []),
                 Goal("5 Keepers", []),
                 Goal("All You Need is Love", []),
                 Goal("Appliances", [[14, 16]]),
                 Goal("Baked Goods", [[1, 3]]),
                 Goal("Bed Time", [[12, 15]]),
                 Goal("Brain (no TV)", []),
                 Goal("Chocolate Cookies", [[2, 3]]),
                 Goal("Chocolate Milk", [[2, 7]]),
                 Goal("Death by Chocolate", [[2, 4]]),
                 Goal("Dreamland", [[5, 12]]),
                 Goal("Hearts and Minds", [[0, 6]]),
                 Goal("Hippyism", [[6, 10]]),
                 Goal("Milk and Cookies", [[3, 7]]),
                 Goal("Night and Day", [[9, 13]]),
                 Goal("Peace (no War)", []),
                 Goal("Rocket Science", [[3, 7]]),
                 Goal("Rocket to the Moon", [[0, 11]]),
                 Goal("Squishy Chocolate", [[2, 13]]),
                 Goal("Time is Money", [[8, 15]]),
                 Goal("Toast", [[1, 16]]),
                 Goal("War = Death", [[4, 17]]),
                 Goal("Winning the Lottery", [[5, 8]])]
        # set the pile to the cards, create an empty discard pile
        self.pile = cards