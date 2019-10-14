import json, os
from pprint import pprint

class Util:

    my_self = ""

    def __init__(self, key):
        global my_self
        my_self=key

    def print_pack(self):
        print "========================================PACK========================================"
        with open('resources/' + my_self + '/pack.json') as infile:    
            data = json.load(infile)  
        for key in data.keys():
            print key + ": " + str(data[key]) 
        print "===================================================================================="

    def rem_packitem(self, key):
        with open('resources/' + my_self + '/pack.json', 'r+') as infile:
            data = json.load(infile)
            del data[key]
            infile.seek(0)        # <--- should reset file position to the beginning.
            json.dump(data, infile, indent=4)
            infile.truncate()     # remove remaining part 

    def add_packitem(self, key, blurb):
        with open('resources/' + my_self + '/pack.json', 'r+') as infile:
            data = json.load(infile)
            data[key] = blurb 
            infile.seek(0)        # <--- should reset file position to the beginning.
            json.dump(data, infile, indent=4)
            infile.truncate()     # remove remaining part        

    def add_limiteditem(self, key, blurb):
        with open('resources/' + my_self + '/pack.json', 'r+') as infile:
            data = json.load(infile)
            data[key] = blurb 
            infile.seek(0)        # <--- should reset file position to the beginning.
            json.dump(data, infile, indent=4)
            infile.truncate()     # remove remaining part  
    
    def print_encounters(self):
        print "================================Encounters=========================================="
        with open('resources/' + my_self + '/encounters.json') as infile:    
            data = json.load(infile)  
        for key in data.keys():
            print key + ": " + str(data[key])     
        print "===================================================================================="
    
    def add_encounter(self, key, blurb):
        with open('resources/' + my_self + '/encounters.json', 'r+') as infile:
            data = json.load(infile)
            data[key] = blurb 
            infile.seek(0)        # <--- should reset file position to the beginning.
            json.dump(data, infile, indent=4)
            infile.truncate()     # remove remaining part    

    def print_spells(self):
        print "================================Spells=========================================="
        with open('resources/' + my_self + '/spells.json') as infile:    
            data = json.load(infile)  
        for key in data.keys():
            print key + ": " + str(data[key]) + "\n"     
        print "===================================================================================="
    
    def add_spell(self, key, blurb):
        with open('resources/' + my_self + '/spells.json', 'r+') as infile:
            data = json.load(infile)
            data[key] = blurb 
            infile.seek(0)        # <--- should reset file position to the beginning.
            json.dump(data, infile, indent=4)
            infile.truncate()     # remove remaining part 

    def rem_spell(self, key):
        with open('resources/' + my_self + '/spells.json', 'r+') as infile:
            data = json.load(infile)
            del data[key]
            infile.seek(0)        # <--- should reset file position to the beginning.
            json.dump(data, infile, indent=4)
            infile.truncate()     # remove remaining part 

    def print_feats(self):
        print "================================Feats=========================================="
        with open('resources/' + my_self + '/feats.json') as infile:    
            data = json.load(infile)
        for key in data.keys():
            print key + ": " + str(data[key]) + "\n"
        print "===================================================================================="
    
    def add_feat(self, key, blurb):
        with open('resources/' + my_self + '/feats.json', 'r+') as infile:
            data = json.load(infile)
            data[key] = blurb 
            infile.seek(0)        # <--- should reset file position to the beginning.
            json.dump(data, infile, indent=4)
            infile.truncate()     # remove remaining part 

    def rem_feat(self, key):
        with open('resources/' + my_self + '/feats.json', 'r+') as infile:
            data = json.load(infile)
            del data[key]
            infile.seek(0)        # <--- should reset file position to the beginning.
            json.dump(data, infile, indent=4)
            infile.truncate()     # remove remaining part 

    def rem_encounter(self, key):
        with open('resources/' + my_self + '/encounters.json', 'r+') as infile:
            data = json.load(infile)
            del data[key]
            infile.seek(0)        # <--- should reset file position to the beginning.
            json.dump(data, infile, indent=4)
            infile.truncate()     # remove remaining part 

    def print_saves(self):
        print "===================================Saves============================================"
        with open('resources/' + my_self + '/saves.json') as infile:    
            data = json.load(infile)  
        for key in data.keys():
            print key + ": " + str(data[key])
        print "===================================================================================="

    def print_full(self, edition):
        print

        # TODO Get this extra code out of here
        if (edition == 2):
            filenames = ["bcim.json", "class.json", "saves.json", "stats.json"]
        else:
            filenames = ["bcim.json", "class.json", "saves.json", "skills.json"]

        for name in filenames:
            with open('resources/' + my_self + '/' + name) as infile:    
                data = json.load(infile)  
            for key in data.keys():
                print key + ": " + str(data[key])
            print  
        print

    def compute_damage(self):
        with open('resources/' + my_self + '/stats.json') as infile:    
            data = json.load(infile)  
        
        thesum = 0
        for key in data.keys():
            if (key == "specialization damage" or key == "strength damage" or key == "weapon damage"):
                thesum+=data[key]
        return thesum

    def compute_tohit(self):
        with open('resources/' + my_self + '/stats.json') as infile:    
            data = json.load(infile)  
        
        thesum = 0
        for key in data.keys():
            if (key == "specialization to hit" or key == "strength to hit" or key == "weapon to hit"):
                thesum+=data[key]
        return thesum

    def get_key(self, filename, key):
        with open('resources/' + my_self + '/' + filename) as infile:    
            data = json.load(infile)  
        
        value = data[key]

        return value    

    def increment_key(self, filename, key, increment):
        with open('resources/' + my_self + '/' + filename) as infile:    
            data = json.load(infile)

        data[key]+=increment

        with open('resources/' + my_self + '/' + filename, 'w') as outfile:
            json.dump(data, outfile)        

    def set_key(self, filename, key, value):
        with open('resources/' + my_self + '/' + filename) as infile:    
            data = json.load(infile)

        data[key]=value

        with open('resources/' + my_self + '/' + filename, 'w') as outfile:
            json.dump(data, outfile)
    
    def create_character(self):

        bcim_dict = {
            "fen": 0,
            "chao": 0,
            "chien": 0,
            "yuan": 0,
            "tael": 0,
            "honor": 0
        }

        class_dict = {
            "status": "healthy",
            "level": 1,
            "exp": 0,
        }

        stats_dict = {}
        encounters_dict = {}
        pack_dict = {}
        saves_dict = {}

        print "Character Nickname: (str)"
        foldername = raw_input()
        print "Character Name: (str) of (str)"
        name = raw_input()
        print "Age: (int)"
        age = raw_input()
        print "Sex: (m/f)"
        sex = raw_input()
        print "Race: (str)"
        race = raw_input()
        print "Alignment: (str) (str)"
        align = raw_input()
        print "Family Honor: (int)"
        fhonor = raw_input()
        
        print "Character Class: (str)"
        cclass = raw_input()
        print "Attack Description: (# attacks/# rounds)"
        atkdsc = raw_input()
        print "Starting HP: (int)"
        starthp = raw_input()
        currhp = starthp
        print "Starting AC: (int)"
        startac = raw_input()
        print "Starting thAC0: (int)"
        thaco = raw_input()
        print "Experience to next level: (int)"
        expnext = raw_input()
        print "Roll for Strength [4d6 and throw away the lowest, percentile dice for second number]: (str#:str#)"
        stren = raw_input()
        print "Roll for Constitution [4d6 and throw away the lowest]: (str#)"
        const = raw_input()
        print "Roll for Dexterity [4d6 and throw away the lowest]: (str#)"
        dex = raw_input()
        print "Roll for Intelligence [4d6 and throw away the lowest]: (str#)"
        intel = raw_input()
        print "Roll for Charisma [4d6 and throw away the lowest]: (str#)"
        charis = raw_input()
        print "Roll for Comeliness [4d6 and throw away the lowest]: (str#)"
        comeli = raw_input()
        print "Roll for Wisdom [4d6 and throw away the lowest]: (str#)"
        wisdom = raw_input()

        print "Specialization to hit: (int)"
        spechit = raw_input()
        print "Weapon to hit: (int)"
        weaphit = raw_input()
        print "Strength to hit: (int)"
        strenhit = raw_input()
        print "Specialization damage: (int)"
        specdam = raw_input()
        print "Weapon damage: (int)"
        weapdam = raw_input()

        print "Strength damage: (int)"      
        strendam = raw_input()
        print "Save vs Para/Poison/Death: (int)"
        ppd = raw_input()
        print "Save vs Petri/Poly: (int)"
        pp = raw_input()
        print "Save vs Rod/Staff/Wand: (int)"
        rod = raw_input()
        print "Save vs Breath Weapon: (int)"
        breath = raw_input()
        print "Save vs Spells: (int)"  
        spells = raw_input()

        bcim_dict["folder name"] = foldername
        bcim_dict["name"] = name
        bcim_dict["age"] = int(age)
        bcim_dict["sex"] = sex
        bcim_dict["race"] = race
        bcim_dict["align"] = align
        bcim_dict["family honor"] = int(fhonor)

        class_dict["class"] = cclass
        class_dict["attacks"] = atkdsc
        class_dict["max hp"] = int(starthp)
        class_dict["current hp"] = int(currhp)
        class_dict["base ac"] = int(startac)
        class_dict["thaco"] = int(thaco)
        class_dict["next level"] = int(expnext)
        class_dict["strength"] = stren
        class_dict["constitution"] = int(const)
        class_dict["dexterity"] = int(dex)
        class_dict["intelligence"] = int(intel)
        class_dict["charisma"] = int(charis)
        class_dict["comeliness"] = int(comeli)
        class_dict["wisdom"] = int(wisdom)
        
        stats_dict["specialization to hit"] = int(spechit)
        stats_dict["strength to hit"] = int(weaphit)
        stats_dict["weapon to hit"] = int(strenhit)
        stats_dict["specialization damage"] = int(specdam)
        stats_dict["strength damage"] = int(strendam)
        stats_dict["weapon damage"] = int(weapdam)
        
        saves_dict["ppd"] = int(ppd)
        saves_dict["pp"] = int(pp)
        saves_dict["rod"] = int(rod)
        saves_dict["breath"] = int(breath)
        saves_dict["spells"] = int(spells)

        if not os.path.exists('resources/' + foldername):
            os.makedirs('resources/' + foldername) 

        f = open('resources/' + foldername + '/bcim.json', 'w')
        json.dump(bcim_dict, f)
        f = open('resources/' + foldername + '/class.json', 'w')
        json.dump(class_dict, f)
        f = open('resources/' + foldername + '/stats.json', 'w')
        json.dump(stats_dict, f)
        f = open('resources/' + foldername + '/saves.json', 'w')
        json.dump(saves_dict, f)
        f = open('resources/' + foldername + '/encounters.json', 'w')
        json.dump(encounters_dict, f)      
        f = open('resources/' + foldername + '/pack.json', 'w')
        json.dump(pack_dict, f)       

        print "Character '" + name + "' created."
        print "Switch to the new character with the 'switch' command"        

                       