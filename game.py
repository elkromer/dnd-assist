print "Commandline Player Assistant"
print "Reese K. 2018 reesek@cdata.com"
# Reese Krome 10/6/2018 reesek@cdata.com
import gamingenv, sys
from os import system

p = gamingenv.player
clear = lambda: system('cls')

while True:
    
    commands = ["whoami","bank","exp","ouch","hit","addhp","permhp","ki","unki","who","saves","levelup","setac","meet","addmeet","pack","additem","remitem","pay", "cmd", "clear", "exit"]

    raw = raw_input("#> ")

    args = raw.split(" ")

    if (args[0] in commands):
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
        elif command == "meet":
            p.meet()
        elif command == "addmeet":
            meet_name = args[1]
            meet_desc = raw_input("description #>")
            p.addmeet(meet_name, meet_desc)
        elif command == "pack":
            p.pack()
        elif command == "additem":
            item_name = args[1]
            item_desc = raw_input("description #> ")
            p.additem(item_name, item_desc)
        elif command == "remitem":
            p.remitem(args[1])
        elif command == "pay":
            p.pay(args[1], int(args[2]))
        elif command == "exit":
            exit(0)
        elif command == "clear":
            clear()
        else:
            p.cmd()


