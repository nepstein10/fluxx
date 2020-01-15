from time import sleep
from Card import Keeper

class Player(object):
    # g: Game, name: string, pID: int (10 is player 1 for now, but in players[0] of g
    def __init__(self, g, name, pID):
        self.game = g
        self.name = name
        self.ID = pID
        # start with an empty hand and no keepers
        self.hand = []
        self.keepers = []

    #   lt (either "h" or "k")
    #   st (string): prompt user to pick one of their cards
    #   fun (function): the function to pass the card to from the button
    #   FUTURE: MIGHT WANT TO INCLUDE AN ARG OF A LIST OF STUFF TO PASS THROUGH TO FUN
    def choose_card(self, lt, st, fun):
        iterable = self.hand if lt is "h" else self.keepers
        print (iterable)
        self.game.view.pick_card(self, iterable, st, fun)


    # Card; li (either "h" or "k") discard prompt
    def discard(self, stli):
        print (f"{self.name}, select a card to discard.")
        st = "card from your hand" if stli == "h" else "keeper"
        self.choose_card(stli, f"select a {st} to discard", self.manage_discard)

    def manage_discard(self, _p, card):
        self.game.deck.discard.append(card)
        self.lims_comply()


    # Boolean; wc: int list (the keepers needed to win)
    def compwin(self, wc):
        for kid in wc:
            if not kid in map(self.get_kID, self.keepers):
                print(kid)
                return False
        return True

    # k (Keeper)
    def get_kID(self, k):
        print(f"getting kID for {k}")
        return k.kID

    # discard down to hand and keeper limits
    def lims_comply(self):
        hl = self.game.ruleManager.handlim
        kl = self.game.ruleManager.keeplim
        if hl and len(self.hand) > hl:
            self.discard("h")
        elif kl and len(self.keepers) > kl:
            self.discard("k")
        else:
            self.game.ruleManager.check_compliance()


    # # get an int input
    # def get_int(self, high):
    #     sel = raw_input("Please type a number from 1-{}: ".format(high))
    #     try:
    #         sel = int(sel)
    #     except ValueError:
    #         print ("Oops, couldn't read that as a number")
    #         sel = self.get_int(high)
    #     while sel < 1 or sel > high:
    #         print ("Entry out of range")
    #         sel = self.get_int(high)
    #     return sel

    # do all the end-turn things like complying with limits, taking another
    def end_turn(self):
        self.lims_comply()


    # to_string
    def __repr__(self):
        return self.name