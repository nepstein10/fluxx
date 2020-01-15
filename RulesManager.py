class Rules(object):
    # def __init__(self, r):
    #     self.draws = r[0]
    #     self.plays = r[1]
    #     self.handlim = r[2]
    #     self.keeplim = r[3]

    def __init__(self, g):
        self.game = g
        self.rules = [] # a list of the NRule objects in play
        self.draws = 1
        self.plays = 1
        self.handlim = None
        self.keeplim = None
        self.double_ag = None
        # for check_compliance:
        self.ops = None
        self.ap = None

    def get_plays(self):
        return self.plays

    # rules: int list (the rules to update to, with None if no change)
    def update_rules(self, rules):
        options = [self.draws, self.plays, self.handlim, self.keeplim]
        for r in range(len(rules)):
            # update any rules that need updating
            if not rules[r] is None:
                options[r] = rules[r]
                print ("rule {r} updated")
        self.draws = options[0]
        self.plays = options[1]
        self.handlim = options[2]
        self.keeplim = options[3]

    # r: Card (a New Rule card)
    def add_rule(self, r):
        for rule in range(len(r.rules)):
            if r.rules[rule]:
                for c in self.rules:
                    if c.rules[rule]:
                        self.rules.remove(c)
                        self.game.deck.discard.append(c)
                        break
        self.rules.append(r)
        self.update_rules(r.rules)

    # g: Game
    # p: Player (the active player)
    # d: int (number already drawn)
    def draw_up(self, p, d):
        # make sure player drew enough cards if new rule adds draws
        if d < self.draws:
            # draw cards one at a time
            for c in self.game.deck.deal(self.draws - d):
                p.hand.append(c)
            self.game.dtt = self.draws

    # ops: a list of the other players
    # make all players comply w/ hand/keep lims, new draws
    def check_compliance(self):
        # comply other players with hand and keeper limits
        if len(self.ops):
            self.ops.pop(0).lims_comply()
        else:
            self.game.cont_play(self.ap)
