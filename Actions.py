# This file contains the actions to be run by Action
#   cards in Fluxx. They are listed alphabetically.
#   The functions take in:
#       c: the Card being played
#       p: the Player who played it
#       g: the Game being played

def dnd(c, p, g):
    print("TODO")

def d2_u2(c, p, g):
    print("TODO")

def d3_p2(c, p, g):
    print("TODO")

def empty_trash(c, p, g):
    print("TODO")

def eg1(c, p, g):
    print("TODO")

def exch_keeps(c, p, g):
    print("TODO")

def go_fish(c, p, g):
    print("TODO")

def inag(c, p, g):
    print("TODO")

def ldta(c, p, g):
    print("TODO")

def lsimplify(c, p, g):
    print("TODO")

def no_lims(c, p, g):
    print("TODO")

def r_hands(c, p, g):
    print("TODO")

def rules_reset(c, p, g):
    rm = g.ruleManager
    # discard NRules in play
    while len(rm.rules):
        g.deck.discard.append(rm.rules.pop())
    # reset to basic rules (negative leads to None)
    g.ruleManager.update_rules([1, 1, -1, -1])
    print(f"Rules now: {rm.rules}")

def scr_keeps(c, p, g):
    print("TODO")

def st_keep(c, p, g):
    print("TODO")

def taturn(c, p, g):
    print("TODO")

def taxation(c, p, g):
    print("TODO")

def trade_hands(c, p, g):
    print("TODO")

def trash_keep(c, p, g):
    print("TODO")

def trash_nrule(c, p, g):
    print("TODO")

def usewytake(c, p, g):
    print("TODO")