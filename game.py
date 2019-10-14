print "Commandline Player Assistant "
print "Reese K. 2018 reesek@cdata.com"
# Reese Krome 10/6/2018 v1.0 reesek@cdata.com
# 8/3/2019 v1.1

import gamingenv,sys
from os import system

p = gamingenv.Player()
p.initialize_player(sys.argv[1])

clear = lambda: system('cls')

while True:
    raw = raw_input("#> ")

    args = raw.split(" ")

    command = args[0]
    if command == "whoami":
        p.whoami()
    elif command == "bank":
        p.bank(args[1], int(args[2]))
    elif command == "exp":
        p.exp(int(args[1]))
    elif command == "ouch":
        p.ouch(int(args[1]))
    elif command == "hit":
        p.hit(int(args[1]))
    elif command == "addhp":
        p.addhp(int(args[1]))
    elif command == "permhp":
        p.permhp(int(args[1]))
    elif command == "ki":
        p.ki()
    elif command == "unki":
        p.unki()
    elif command == "who":
        p.who()
    elif command == "saves":
        p.saves()
    elif command == "levelup":
        p.levelup()
    elif command == "setac":
        p.setac(int(args[1]))
    elif command == "set":
        key_name = ""
        for i in range(len(args)):
            if (i == 0):
                continue
            key_name += args[i] + ("" if (i == len(args) - 1) else " ")            
        key_value = raw_input("value #> ")
        p.setkey(key_name, key_value)    
    elif command == "status":
        p.status(args[1])
    elif command == "meet":
        p.meet()
    elif command == "addmeet":
        meet_name = ""
        for i in range(len(args)):
            if (i == 0):
                continue
            meet_name += args[i] + ("" if (i == len(args) - 1) else " ")            
        meet_desc = raw_input("description #> ")
        p.addmeet(meet_name, meet_desc)
    elif command == "feat":
        p.feat()
    elif command == "addfeat":
        feat_name = ""
        for i in range(len(args)):
            if (i == 0):
                continue
            feat_name += args[i] + ("" if (i == len(args) - 1) else " ")            
        feat_desc = raw_input("description #> ")
        p.addfeat(feat_name, feat_desc)
    elif command == "remfeat":
        feat_name = ""
        for i in range(len(args)):
            if (i == 0):
                continue
            feat_name += args[i] + ("" if (i == len(args) - 1) else " ")            
        p.remfeat(feat_name)  
    elif command == "spell":
        p.spell()
    elif command == "addspell":
        spell_name = ""
        for i in range(len(args)):
            if (i == 0):
                continue
            spell_name += args[i] + ("" if (i == len(args) - 1) else " ")            
        spell_desc = raw_input("description #> ")
        p.addspell(spell_name, spell_desc)
    elif command == "remspell":
        spell_name = ""
        for i in range(len(args)):
            if (i == 0):
                continue
            spell_name += args[i] + ("" if (i == len(args) - 1) else " ")            
        p.remspell(spell_name)        
    elif command == "pack":
        p.pack()
    elif command == "additem":
        item_name = ""
        for i in range(len(args)):
            if (i == 0):
                continue
            item_name += args[i] + ("" if (i == len(args) - 1) else " ")
        item_desc = raw_input("description #> ")
        p.additem(item_name, item_desc)
    elif command == "remitem":
        item_name = ""
        for i in range(len(args)):
            if (i == 0):
                continue
            item_name += args[i] + ("" if (i == len(args) - 1) else " ")
        p.remitem(item_name)
    elif command == "addlimiteditem":
        item_name = ""
        for i in range(len(args)):
            if (i == 0):
                continue
            item_name += args[i] + ("" if (i == len(args) - 1) else " ")            
        item_count = int(raw_input("initial count #> "))
        p.addlimiteditem(item_name, item_count)
    elif command == "useitem":
        item_name = ""
        for i in range(len(args)):
            if (i == 0):
                continue
            item_name += args[i] + ("" if (i == len(args) - 1) else " ") 
        p.useitem(item_name)
    elif command == "pay":
        p.pay(args[1], int(args[2]))
    elif command == "exit":
        exit(0)
    elif command == "clear":
        clear()
    else:
        p.cmd()

