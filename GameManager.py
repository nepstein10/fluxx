from Game import Game
from random import shuffle
from View import View


# play the game
def main():
    gm = GM()
    # v = View(gm)
    # v.game_select()
    # people = gm.get_player_names(v)
    # g = Game(people)
    # print g.players
    # g.setup()
    # shuffle(g.players)
    # turn_num = 0
    # while g.winner is None:
    #     g.turn(g.players[turn_num % len(g.players)])
    #     for p in g.players:
    #         print "{}, {}, {}".format(p.name, p.hand, p.keepers)
    #     print g.ruleManager.rules
    #     turn_num += 1
    # print "{} is the winner!".format(g.winner.name)
    # return


class GM(object):
    def __init__(self):
        # NEED TO UPDATE THIS WITH ALL GAME OPTIONS
        game_opts = [FluxxSample(), Fluxx3_1()]
        self.v = View(self, game_opts)
        self.game_select(self.v)

    # print then to view
    def game_select(self, view):
        print "Welcome to Fluxx!"
        view.game_select()

    ### Phasing out the below ###
    # play Fluxx 3.1
    def f3_1(self, people):
        g = Game(people)
        print g.players

    def sample(self, people):
        g = Game(people)
        print g.players

class Fluxx(object):
    def __init__(self):
        self.minPlayers = 2
        self.maxPlayers = 6

class Fluxx3_1(Fluxx):
    def __init__(self):
        super.__init__()
        self.maxPlayers = 5

    def __repr__(self):
        return "Fluxx 3.1"

class FluxxSample(Fluxx):
    def __init__(self):
        super.__init__(self)
        self.minPlayers = 1

    def __repr__(self):
        return "Fluxx Sample"


if __name__ == '__main__':
    main()