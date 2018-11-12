print "Commandline Player Assistant"
print "Reese K. 2018 reesek@cdata.com"
# Reese Krome 10/6/2018 reesek@cdata.com
import gamingenv, sys
from os import system

p = gamingenv.player
clear = lambda: system('cls')

while True:
    
    commands = ["whoami","bank","exp","ouch","hit","addhp","permhp","ki","unki","who","saves","levelup","setac","meet","addmeet", "remmeet","pack","additem","remitem", "addhonor", "pay", "cmd", "clear", "create", "switch","exit"]

    raw = raw_input("#> ")
    
    try:
        cmd = raw[0:raw.index(" ")]
    except ValueError:
        cmd = raw
    try:
        arglist = raw[raw.index(" ")+1:]
    except ValueError:
        arglist = ""   

    if (cmd in commands):
    
        if cmd == "whoami":
            p.whoami()
        elif cmd == "bank":
            key = arglist[0:arglist.index(" ")]
            amt = arglist[arglist.index(" ")+1:]
            p.bank(key, int(amt))
        elif cmd == "exp":
            p.exp(int(arglist))
        elif cmd == "ouch":
            p.ouch(int(arglist))
        elif cmd == "hit":
            p.hit(int(arglist))
        elif cmd == "addhp":
            p.addhp(int(arglist))
        elif cmd == "permhp":
            p.permhp(int(arglist))
        elif cmd == "ki":
            p.ki()
        elif cmd == "unki":
            p.unki()
        elif cmd == "addhonor":
            p.addhonor(int(arglist))
        elif cmd == "who":
            p.who()
        elif cmd == "saves":
            p.saves()
        elif cmd == "levelup":
            p.levelup()
        elif cmd == "setac":
            p.setac(int(arglist))
        elif cmd == "meet":
            p.meet()
        elif cmd == "addmeet":
            name = arglist[0:arglist.index(" ")]
            desc = arglist[arglist.index(" ")+1:]
            p.addmeet(name, desc)
            print "Added entry for " + name
        elif cmd == "remmeet":
            p.remmeet(arglist)  
            print "Removed entry for " + arglist          
        elif cmd == "pack":
            p.pack()
        elif cmd == "additem":
            item = arglist[0:arglist.index(" ")]
            desc = arglist[arglist.index(" ")+1:]
            p.additem(item, desc)
            print "Added entry for " + item
        elif cmd == "remitem":
            p.remitem(arglist)
            print "Removed entry for " + arglist
        elif cmd == "pay":
            curr=arglist[0:arglist.index(" ")]
            amt=int(arglist[arglist.index(" ")+1:])
            p.pay(curr, amt)
        elif cmd == "create":
            p.createchar()
        elif cmd == "switch":
            p.switchchar(arglist)
        elif cmd == "exit":
            exit(0)
        elif cmd == "clear":
            clear()
        else:
            p.cmd()


