class Card(object):
    # name: string, game: Game
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def on_play(self, player):
        print (f"Played {self.name}")

    def __repr__(self):
        return self.name


class NRule(Card):
    # name: string, game: Game, rules: int list ([draws, plays, hlim, klim])
    def __init__(self, name, game, rules):
        self.name = name
        self.game = game
        self.rules = rules

    # update the game rules with card-specific rules
    def on_play(self, player):
        super().on_play(player)
        self.game.ruleManager.add_rule(self)

class Action(Card):
    # name: string, game: Game, action: function (from actions list in Deck)
    def __init__(self, name, game, action):
        self.name = name
        self.game = game
        self.action = action

    # do the action - most still to implement
    def on_play(self, player):
        super().on_play(player)
        self.action(self.game)
        self.game.deck.discard.append(self)


class Keeper(Card):
    # name: string, game: Game, kID: int
    def __init__(self, name, game, kID):
        self.name = name
        self.game = game
        self.kID = kID

    # play the keeper
    def on_play(self, player):
        super().on_play(player)
        player.keepers.append(self)

class Goal(Card):
    #special cases (5 keepers, 10 CiH) not built in yet, and not compatible
        # aslo not compatible are expansion goals of "either/or" potentially
    # name: string, game: Game, wCon: int list (the keepers needed to win)
    def __init__(self, name, game, wCon):
        self.name = name
        self.game = game
        self.wCon = wCon

    # play the goal
    def on_play(self, player):
        super(Goal, self).on_play(player)
        if not self.game.ruleManager.double_ag:
            self.game.goals = []
        self.game.goals.append(self)