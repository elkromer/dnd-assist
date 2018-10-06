from helper import *

class Player:

    def __init__(self):
        print "initializing player"

    def permhp(self, amt):
        Util().increment_key("class.json", "max hp", amt)

    def addhp(self, amt):
        Util().increment_key("class.json", "current hp", amt)

    def ki(self):
        Util().increment_key("class.json","level", 2)
        Util().increment_key("class.json", "thaco", -2)
    
    def unki(self):
        Util().increment_key("class.json","level", -2)
        Util().increment_key("class.json", "thaco", 2)  
    
    def whoami(self):
        print
        print "\t" + str(Util().get_key("bcim.json", "name"))
        print "\tLevel: " + str(Util().get_key("class.json", "level")) + " Exp: " + str(Util().get_key("class.json", "exp")) + "/" + str(Util().get_key("class.json", "next level"))
        print "\tHonor: " + str(Util().get_key("bcim.json", "honor")) + " Tael: " + str(Util().get_key("bcim.json", "tael"))
        print "\t\tHP: " + str(Util().get_key("class.json", "current hp")) + "/" + str(Util().get_key("class.json", "max hp")) +  " Status: " +  str(Util().get_key("class.json", "status"))
        print "\t\t+" + str(Util().compute_tohit()) + " HIT/ +" + str(Util().compute_damage()) + " DMG"
        print "\t\tAC: " + str(Util().get_key("class.json", "base ac"))
        print "\t\tthAC0: " + str(Util().get_key("class.json", "thaco"))
        print
        
    def hit(self, enemyac):
        print "Roll a " + str(Util().get_key("class.json", "thaco")-enemyac-Util().compute_tohit())

    def ouch(self, dmg):
        Util().increment_key("class.json", "current hp", ((-1)*dmg))

    def cash(self, key, amt):
        Util().increment_key("bcim.json", key, amt)
    
    def exp(self, amt):
        Util().increment_key("class.json", "exp", amt)
    
    def who(self):
        Util().print_full()
    
    def saves(self):
        Util().print_saves()    
    
    def levelup(self):
        Util().increment_key("class.json","level", 1)
        Util().increment_key("class.json","thaco", -1)
    
    def setac(self, ac):
        Util().set_key("class.json", "base ac", ac)

    def meet(self):
        Util().print_encounters()
    
    def addmeet(self, key, blurb):
        Util().add_encounter(key, blurb)

    def pack(self):
        Util().print_pack()
    
    def additem(self, key, blurb):
        Util().add_packitem(key, blurb)

    def remitem(self, key):
        Util().rem_packitem(key)

    def pay(self, key, amt):
        Util().increment_key("bcim.json", key, ((-1)*amt))

    def cmd(self):
        print "====================Commands===================="

        commands = ["whoami()", "cash('currency', amt)", "exp(amt)", "ouch(amt)", "hit(enemyAC)", "addhp(amt)", "permhp(amt)", "ki()", "unki()", "who()", "saves()", "levelup()", "setac(AC)", "meet()", "addmeet('person', 'blurb')", "pack()", "additem('item', 'desc')", "remitem('item')", "pay('currency', amt)"]

        for x in commands:
            print x
        print "================================================"
        