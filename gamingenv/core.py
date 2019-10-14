from helper import *

class Player:
    util = None
    edition = 0
    commands = []
    filenames = []

    def __init__(self):
        print "Loading player module."

    def initialize_player(self, player):
        global util, commands, edition, filenames
        util = Util(player)

        edition = int(util.get_key("bcim.json", "edition"))
        if (edition == 2):
            commands = ["whoami", "bank <currency> <amt>", "exp <amt>", "ouch <amt>", "hit <enemyAC>", "addhp <amt>", "permhp <amt>", "ki", "unki", "who", "saves", "levelup", "setac <baseac>", "meet", "addmeet <person> <blurb>", "remmeet <person>","pack", "additem <item> <desc>", "remitem <item>", "create","addhonor <amt>", "switch <character>", "pay <currency> <amt>", "status <health status>", "set <key>"]
            filenames = ["bcim.json", "class.json", "saves.json", "stats.json"]
        elif (edition == 5):
            commands = ["whoami", "bank <currency> <amt>", "exp <amt>", "ouch <amt>","hit <enemyAC>", "addhp <amt>", "permhp <amt>", "who", "saves", "levelup", "setac <baseac>", "meet", "addmeet <person> <blurb>", "remmeet <person>","pack", "additem <item> <desc>", "remitem <item>", "addlimiteditem <item>", "addfeat <feat>", "remfeat <feat>", "feat", "addspell <spell>", "remspell <spellname>", "spell", "create", "addhonor <amt>", "switch <character>", "pay <currency> <amt>", "status <health status>", "set <key>"]
            filenames = ["bcim.json", "class.json", "saves.json", "skills.json"]
        else:
            print "Unknown edition " + str(edition) + "."
            exit(1)

        print "Loaded " + str(edition) + "ed character class."
        print "Initialized " + str(util.get_key("bcim.json", "name") + ".")

    def addhonor(self, amt):
        util.increment_key("bcim.json", "honor", amt)

    def permhp(self, amt):
        util.increment_key("class.json", "max hp", amt)

    def addhp(self, amt):
        util.increment_key("class.json", "current hp", amt)

    def ki(self):
        if (util.get_key("bcim.json", "edition") == 2):
            util.increment_key("class.json", "level", 2)
            util.increment_key("class.json", "thaco", -2)
        else:
            print "Error: Command for 2ed only."

    def unki(self):
        if (util.get_key("bcim.json", "edition") == 2):
            util.increment_key("class.json", "level", -2)
            util.increment_key("class.json", "thaco", 2)  
        else:
            print "Error: Command for 2ed only."
    
    def whoami(self):
        if (util.get_key("bcim.json", "edition") == 2):
            print
            print "\t" + str(util.get_key("bcim.json", "name")) + " (" + str(util.get_key("bcim.json", "edition")) + " edition)"
            print "\tLevel: " + str(util.get_key("class.json", "level")) + " Exp: " + str(util.get_key("class.json", "exp")) + "/" + str(util.get_key("class.json", "next level"))
            print "\tHonor: " + str(util.get_key("bcim.json", "honor")) + " Tael: " + str(util.get_key("bcim.json", "tael"))
            print "\t\tHP: " + str(util.get_key("class.json", "current hp")) + "/" + str(util.get_key("class.json", "max hp")) +  " Status: " +  str(util.get_key("class.json", "status"))
            print "\t\t+" + str(util.compute_tohit()) + " HIT/ +" + str(util.compute_damage()) + " DMG"
            print "\t\tAC: " + str(util.get_key("class.json", "base ac"))
            print "\t\tthAC0: " + str(util.get_key("class.json", "thaco"))
            print
            print "\tNotes: " + str(util.get_key("class.json", "tips"))
            print
        else:
            multiclass = " / " + str(util.get_key("class.json", "multiclass")) + " " + str(util.get_key("class.json", "multilevel"))
            print
            print "\t" + str(util.get_key("bcim.json", "name")) + " (" + str(util.get_key("class.json", "class")) + " " + str(util.get_key("class.json", "level")) + (multiclass if (str(util.get_key("class.json", "multiclass")) != "") else "") + ")"
            print "\tExp: " + str(util.get_key("class.json", "exp")) + "/" + str(util.get_key("class.json", "next level"))
            print "\tAC: " + str(util.get_key("class.json", "base ac")) + " Gold: " + str(util.get_key("bcim.json", "gold"))
            print "\t\tHP: " + str(util.get_key("class.json", "current hp")) + "/" + str(util.get_key("class.json", "max hp")) +  " Status: " +  str(util.get_key("class.json", "status"))
            print "\t\tPerception: " + str(util.get_key("class.json", "passive perception"))
            print "\t\tProficiency Bonus: " + str(util.get_key("class.json", "proficiency bonus"))
            print
            print "\tTraits: " + str(util.get_key("class.json", "traits"))
            print "\tFlaws: " + str(util.get_key("class.json", "flaws"))
            print "\tLanguages: " + str(util.get_key("class.json", "languages"))
            print "\tNotes: " + str(util.get_key("class.json", "tips"))
            print
        
    def hit(self, enemyac):
        if (util.get_key("bcim.json", "edition") == 2):
            print "Roll a " + str(util.get_key("class.json", "thaco")-enemyac-util.compute_tohit())
        else:
            print "TODO"

    def ouch(self, dmg):
        util.increment_key("class.json", "current hp", ((-1)*dmg))

    def bank(self, key, amt):
        util.increment_key("bcim.json", key, amt)

    def status(self, status):
        util.set_key("class.json", "status", status)

    def exp(self, amt):
        util.increment_key("class.json", "exp", amt)
    
    def who(self):
        util.print_full(edition)
    
    def saves(self):
        util.print_saves()    
    
    def levelup(self):
        if (util.get_key("bcim.json", "edition") == 2):
            util.increment_key("class.json","level", 1)
            util.increment_key("class.json","thaco", -1)
        else:
            util.increment_key("class.json","level", 1)
            print "Don't forget to add HP! Check player's manual to make sure everything is implemented in the program."

    def setac(self, ac):
        util.set_key("class.json", "base ac", ac)

    def setkey(self, key, value):
        successful = False;
        for f in filenames:
            try:
                test = util.get_key(f, key)
                if (isinstance(test,int)):
                    util.set_key(f, key, int(value))
                    successful = True;
                else:
                    util.set_key(f, key, value)
                    successful = True;
            except (KeyError):
                continue

            if not successful:
                print "The key " + key + " could not be found."
            
    def meet(self):
        util.print_encounters()
    
    def addmeet(self, key, blurb):
        util.add_encounter(key, blurb)

    def spell(self):
        util.print_spells()
    
    def addspell(self, key, blurb):
        util.add_spell(key, blurb)
    
    def remspell(self, key):
        util.rem_spell(key)

    def feat(self):
        util.print_feats()
    
    def addfeat(self, key, blurb):
        util.add_feat(key, blurb)
    
    def remfeat(self, key):
        util.rem_feat(key)
    
    def remmeet(self, key):
        util.rem_encounter(key)

    def pack(self):
        util.print_pack()

    def addlimiteditem(self, key, blurb):
        util.add_limiteditem(key, blurb)

    def additem(self, key, blurb):
        util.add_packitem(key, blurb)

    def useitem(self, key):
        util.increment_key("pack.json", key, (-1))

    def remitem(self, key):
        util.rem_packitem(key)

    def pay(self, key, amt):
        util.increment_key("bcim.json", key, ((-1)*amt))
    
    def createchar(self):
        util.create_character()
    
    def switchchar(self, who):
        self.__init__(who)

    def cmd(self):
        print "====================" + str(edition) + "e Commands===================="
        for x in commands:
            print x
        print "================================================"
        