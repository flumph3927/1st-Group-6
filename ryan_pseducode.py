#RC 1st, My part of the pseducode


#Start off the search function (Take in the dictionary containing all of the characters):
def search(characters):
    char = {}
    #Put into a loop to make sure that the input is one of the options
    while True:
        #Take their input on wether they want to search by name level or skill
        option = simple(input("Would you like to search by skill, level, or class?:"))
        #Check to see if its one of them, if it is break
        if option == "skill" or option == "level" or option == "class":
            break
        else:
            print("That is not an option...")

    #Check to see which one of the three options it is

    #If it is a name, have them input the name they want and print out all characters that have that name
    while True:
        if option == "name":
            #Allow them to select one of the characters and set that to a variable
            name = simple(input("Please tell me the characters name:"))
            if name in characters:
                char[name] = characters[name]
                break
            else:
                print("That character dosen't exist...")
        

    #If it is a class, have them input the class they want and print out all characters that have that class
    while True:
        if option == "class":
            available = []
            #Allow them to select one of the characters and set that to a variable
            clas = simple(input("Please tell me the class:"))
            if clas == "archer" or clas == "knight" or clas == "wizard":
                for key,value in characters:
                    if value[0] == clas:
                        available.append([key,value])
                    else:
                        pass
                x = 1
                for info in available:
                    print(f"{x}. {info[0]}: {info[1]}")
                    x += 1
                while True:
                    pick = input("Which character would you like to select? (Please type the number):").strip()
                    if pick.isdigit() == True and pick >0 and pick < x:
                        pick -= 1
                        break
                    else:
                        print("That is not a valid option (Its not one of the numbers listed)")
                char[available[pick[0]]] = characters[available[pick[0]]]
                break
            else:
                print("That is not a class...")

    #If it is a level, have them input the level they want and print out all characters that have that level
    while True:
        if option == "level":
            available = []
            #Allow them to select one of the characters and set that to a variable
            level = input("Please tell me the level:").strip()
            if level == "1" or level == "2":
                level = int(level)
                for key,value in characters:
                    if value[6] == level:
                        available.append([key,value])          #RIGHT HERE  WOOOOOOOOOOOOOORK
                    else: 
                        pass
                x = 1                        
                for info in available:
                    print(f"{x}. {info[0]}: {info[1]}")
                    x += 1
                while True:
                    pick = input("Which character would you like to select? (Please type the number):").strip()
                    if pick.isdigit() == True and pick >0 and pick < x:
                        pick -= 1
                        break
                    else:
                        print("That is not a valid option (Its not one of the numbers listed)")
                char[available[pick[0]]] = characters[available[pick[0]]]
                break
            else:
                print("That is not a class...")

    #Return variable


#Create a function to allow them to change stats
    #Display all of the main stats (Strength, speed, and intelligence) and there scores.
    #Ask them what is the first one they want to swap
    #Ask them what is the second one they want to swap
    #Get valid inputs

    #assign both of them to base things, 1 or 2
    #Then set first choose = to variable 2
    #Set second choose = variable 1
    #Display new stats

    #Return main dictionary


#Create a function to allow them to change there skill
    #Create a dictionary of skills for there class and what they do

    #Take there characters class and print of the skills that are allowed for that class and there level required
    
    #Put it into a while loop to make sure they choose something available
        #Ask them what of the two skills they want to use
        #Check to see if the skills exitst and if they have met the level requirements

        #If all of the requirements are met, change there skill and return the dictionary containing everything
            #Then break

        #Otherwise have them chose again until they select something that works
            #Then break



#Create a function for inventory
    #Create a while loop for there choice
        #ask them if they want to create a weapon or remove a weapon
        #If there input equals create or remove, then break

        #Else have continue

    #Check to see which of the choices they choose

    #If they chose to add an item, let them create its name and its description, adding it to the dictionary

    #If they chose to remove an item, create a for loop that will print of the name and the description
    #Get valid user input
    #Remove the choosen weapon
    
    #Return the main dictionary







#This is just here for later referance and help for logic.
#key = ["class","strength","speed","intelegence","Dictionary for the skill with discription","inventory dictionary", "level"]

#example for class would be --> dictionary[character_name][0]

def simple(input):
    input = (input).strip().lower()
    return input