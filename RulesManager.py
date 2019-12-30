class Rules(object):
    # def __init__(self, r):
    #     self.draws = r[0]
    #     self.plays = r[1]
    #     self.handlim = r[2]
    #     self.keeplim = r[3]

    def __init__(self):
        self.rules = []
        self.draws = 1
        self.plays = 1
        self.handlim = None
        self.keeplim = None
        self.double_ag = None

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
        self.rules.append(r)
        self.update_rules(r.rules)


    # int (number now drawn); make all players comply w/ hand/keep lims, new draws
    def check_compliance(self, g, p, d):
        # make sure player drew enough cards if new rule adds draws
        if d < self.draws:
            # draw cards one at a time
            for c in g.deck.deal(self.draws - d):
                p.hand.append(c)
        # comply other players with hand and keeper limits
        for player in g.players:
            if not p is player:
                player.lims_comply()
        return self.draws
