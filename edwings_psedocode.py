import random
import ryan_pseducode
import levi_code
#make a funtion create
def create(characters,skills):
    #make the user choose a name, and add it t the character dictionary as a key 
    name = ryan_pseducode.simple(input("What would you wish your name to be?: "))
    characters[name] = ['',0,0,0,{'name':'description'},{},1]
    #create a while loop
    while True:
    #make class equals input what their character class is going to be, with numbers to be easier, and stupid profe
        clas = input("\nPlease select the class you want to choose\n1:Archer\n2:Knight\n3:Wizard ")
        if clas == "1" or clas == "2" or clas == "3":
            break
        else:
            print("Select again")
            continue
    if clas == "1":
        clas='archer'
        #add class to character information
        characters[name][0] = clas
    elif clas == "2":
        clas='knight'
        #add class to character information
        characters[name][0] = clas
    elif clas == "3":
        clas='wizard'
        #add class to character information
        characters[name][0] = clas
    #print stats
    print("Your stats are:\n Strength\nSpeed\nIntelligence")
    #add stats to character information
    characters[name][1], characters[name][2],characters[name][3] = levi_code.distribute(random.randint(5,10))
    #print skill and say that to unlock another one they need to level up
    print("You have one skill right now, but if you level up, you will unlock more")
    #add skill to character information
    characters[name][4]={skills[clas].keys()[0]:skills[clas][skills[clas].keys()[0]]}
    #return chaacter dictionary
    return characters