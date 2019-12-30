class Player(object):
    # g: Game, pID: int (10 is player 1 for now, but in players[0] of g
    def __init__(self, g, name, pID):
        self.game = g
        self.name = name
        self.ID = pID
        # start with an empty hand and no keepers
        self.hand = []
        self.keepers = []

    # Card; li (either "h" or "k") prompt user to pick one of their cards to pop and return
    def choose_card(self, li):
        iterable = None
        if li is "h":
            iterable = self.hand
        else:
            iterable = self.keepers
        print (iterable)
        high = len(iterable)
        sel = self.get_int(high)
        return iterable.pop(sel - 1)

    # Card; li (either "h" or "k") discard prompt
    def discard(self, li):
        print (f"{self.name}, the select a card to discard.")
        return self.choose_card(li)

    # Boolean; wc: int list (the keepers needed to win)
    def compwin(self, wc):
        for k in wc:
            if not k in self.keepers:
                return False
        return True

    # discard down to hand and keeper limits
    def lims_comply(self):
        hl = self.game.ruleManager.handlim
        kl = self.game.ruleManager.keeplim
        if hl:
            while len(self.hand) > hl:
                self.discard("h")
        if kl:
            while len(self.keepers) > kl:
                self.discard("k")

    # get an int input
    def get_int(self, high):
        sel = raw_input("Please type a number from 1-{}: ".format(high))
        try:
            sel = int(sel)
        except ValueError:
            print ("Oops, couldn't read that as a number")
            sel = self.get_int(high)
        while sel < 1 or sel > high:
            print ("Entry out of range")
            sel = self.get_int(high)
        return sel

    # do all the end-turn things like complying with limits, taking another
    def end_turn(self):
        self.lims_comply()

    # to_string
    def __repr__(self):
        return "{self.name} (Player {self.ID-9})"