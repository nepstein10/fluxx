# This file contains the actions to be run by Action
#   cards in Fluxx. They are listed alphabetically.
#   The functions take in:
#       c: the Card being played
#       p: the Player who played it
#       g: the Game being played

def rules_reset(c, p, g):
    rm = g.ruleManager
    # discard NRules in play
    while len(rm.rules):
        g.deck.discard.append(rm.rules.pop())
    # reset to basic rules (negative leads to None)
    g.ruleManager.update_rules([1, 1, -1, -1])
    print(f"Rules now: {rm.rules}")