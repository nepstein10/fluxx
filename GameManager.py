from Game import *
from View import View
from Decks import *


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
        game_opts = [FluxxSample(), Fluxx3_0()]
        self.v = View(game_opts)
        self.game_select(self.v)

    # print then to view
    def game_select(self, view):
        print ("Welcome to Fluxx!")
        view.game_select()



if __name__ == '__main__':
    main()