from helper import *

class Player:
    util = None

    def __init__(self, player):
        global util
        util = Util(player)
        print "Initializing " + str(util.get_key("bcim.json", "name"))

    def addhonor(self, amt):
        util.increment_key("bcim.json", "honor", amt)

    def permhp(self, amt):
        util.increment_key("class.json", "max hp", amt)

    def addhp(self, amt):
        thenhp = util.get_key("class.json", "current hp")
        util.increment_key("class.json", "current hp", amt)
        print "HP: " + str(thenhp) + " -> " + str(util.get_key("class.json", "current hp"))

    def ki(self):
        util.increment_key("class.json", "level", 2)
        util.increment_key("class.json", "thaco", -2)

    def unki(self):
        util.increment_key("class.json", "level", -2)
        util.increment_key("class.json", "thaco", 2)

    def whoami(self):
        print
        print "\t" + str(util.get_key("bcim.json", "name"))
        print "\tLevel: " + str(util.get_key("class.json", "level")) + " Exp: " + str(util.get_key("class.json", "exp")) + "/" + str(util.get_key("class.json", "next level"))
        print "\tHonor: " + str(util.get_key("bcim.json", "honor")) + " Tael: " + str(util.get_key("bcim.json", "tael"))
        print "\t\tHP: " + str(util.get_key("class.json", "current hp")) + "/" + str(util.get_key("class.json", "max hp")) +  " Status: " +  str(util.get_key("class.json", "status"))
        print "\t\t+" + str(util.compute_tohit()) + " HIT/ +" + str(util.compute_damage()) + " DMG"
        print "\t\tAC: " + str(util.get_key("class.json", "base ac"))
        print "\t\tthAC0: " + str(util.get_key("class.json", "thaco"))
        print

    def hit(self, enemyac):
        thaco = util.get_key("class.json", "thaco")-enemyac-util.compute_tohit()
        if thaco < 2:
            print "Don't roll a 1"
        else:
            print "Roll a " + str(thaco)

    def ouch(self, dmg):
        thenhp = util.get_key("class.json", "current hp")
        util.increment_key("class.json", "current hp", ((-1)*dmg))
        print "HP: " + str(thenhp) + " -> " + str(util.get_key("class.json", "current hp"))

    def bank(self, key, amt):
        util.increment_key("bcim.json", key, amt)

    def exp(self, amt):
        util.increment_key("class.json", "exp", amt)

    def who(self):
        util.print_full()

    def saves(self):
        util.print_saves()

    def levelup(self):
        util.increment_key("class.json","level", 1)
        util.increment_key("class.json","thaco", -1)

    def setac(self, ac):
        util.set_key("class.json", "base ac", ac)

    def meet(self):
        util.print_encounters()

    def addmeet(self, key, blurb):
        util.add_encounter(key, blurb)

    def remmeet(self, key):
        util.rem_encounter(key)

    def pack(self):
        util.print_pack()

    def additem(self, key, blurb):
        util.add_packitem(key, blurb)

    def remitem(self, key):
        util.rem_packitem(key)

    def pay(self, key, amt):
        util.increment_key("bcim.json", key, ((-1)*amt))

    def createchar(self):
        util.create_character()

    def switchchar(self, who):
        self.__init__(who)

    def cmd(self):
        print "====================Commands===================="

        commands = ["whoami", "bank <currency> <amt>", "exp <amt>", "ouch <amt>", "hit <enemyAC>", "addhp <amt>", "permhp <amt>", "ki", "unki", "who", "saves", "levelup", "setac <baseac>", "meet", "addmeet <person> <blurb>", "remmeet <person>","pack", "additem <item> <desc>", "remitem <item>", "create","addhonor <amt>", "switch <character>", "pay <currency> <amt>"]

        for x in commands:
            print x
        print "================================================"
