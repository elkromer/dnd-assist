import json
from pprint import pprint

class Util:
    def print_pack(self):
        print "========================================PACK========================================"
        with open('resources/pack.json') as infile:    
            data = json.load(infile)  
        for key in data.keys():
            print key + ": " + str(data[key]) 
        print "===================================================================================="

    def rem_packitem(self, key):
        with open('resources/pack.json', 'r+') as infile:
            data = json.load(infile)
            del data[key]
            infile.seek(0)        # <--- should reset file position to the beginning.
            json.dump(data, infile, indent=4)
            infile.truncate()     # remove remaining part 

    def add_packitem(self, key, blurb):
        with open('resources/pack.json', 'r+') as infile:
            data = json.load(infile)
            data[key] = blurb 
            infile.seek(0)        # <--- should reset file position to the beginning.
            json.dump(data, infile, indent=4)
            infile.truncate()     # remove remaining part        

    def print_encounters(self):
        print "================================Encounters=========================================="
        with open('resources/encounters.json') as infile:    
            data = json.load(infile)  
        for key in data.keys():
            print key + ": " + str(data[key])     
        print "===================================================================================="

    def add_encounter(self, key, blurb):
        with open('resources/encounters.json', 'r+') as infile:
            data = json.load(infile)
            data[key] = blurb 
            infile.seek(0)        # <--- should reset file position to the beginning.
            json.dump(data, infile, indent=4)
            infile.truncate()     # remove remaining part        

    def print_saves(self):
        print "===================================Saves============================================"
        with open('resources/saves.json') as infile:    
            data = json.load(infile)  
        for key in data.keys():
            print key + ": " + str(data[key])
        print "===================================================================================="

    def print_full(self):
        print
        filenames = ["bcim.json", "class.json", "saves.json", "stats.json"]

        for name in filenames:
            with open('resources/' + name) as infile:    
                data = json.load(infile)  
            for key in data.keys():
                print key + ": " + str(data[key])
            print  
        print

    def compute_damage(self):
        with open('resources/stats.json') as infile:    
            data = json.load(infile)  
        
        thesum = 0
        for key in data.keys():
            if (key == "specialization damage" or key == "strength damage" or key == "weapon damage"):
                thesum+=data[key]
        return thesum

    def compute_tohit(self):
        with open('resources/stats.json') as infile:    
            data = json.load(infile)  
        
        thesum = 0
        for key in data.keys():
            if (key == "specialization to hit" or key == "strength to hit" or key == "weapon to hit"):
                thesum+=data[key]
        return thesum

    def get_key(self, filename, key):
        with open('resources/' + filename) as infile:    
            data = json.load(infile)  

        return data[key]      

    def increment_key(self, filename, key, increment):
        with open('resources/' + filename) as infile:    
            data = json.load(infile)

        data[key]+=increment

        with open('resources/' + filename, 'w') as outfile:
            json.dump(data, outfile)        

    def set_key(self, filename, key, value):
        with open('resources/' + filename) as infile:    
            data = json.load(infile)

        data[key]=value

        with open('resources/' + filename, 'w') as outfile:
            json.dump(data, outfile)