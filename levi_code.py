#Psuedocode (and now code) for character display functions, point distribution fuction, level up function, main function

#create function display_characters, get dictionary of characters as CHARS
def display_characters(chars):
    #loop through CHARS as CHAR
    for char in chars.keys():
        #display name, class, and level of character represented by CHAR list
        print(f'{char}: level {chars[char][-1]} {chars[char][0]}')

#create function show_character, get character list as CHAR
def show_character(char):
    name=char.keys()[0]
    #display name, class, and level of CHAR
    print(f'{name}\nLevel {char[name][6]} {char[name][0]}\n')
    #display attribute scores
    print(f'Strength: {char[name][1]}\nSpeed: {char[name][2]}\nIntelligence: {char[name][3]}\n')
    #display skills in CHAR
    print(f'Active skill:\n{char[name][4][0]}:\n{char[name][4][char[name][4].keys()[0]]}\n')
    #display inventory of CHAR
    print('Inventory:')
    for i in char[name][5].keys():
        print(f'{i}:\n{char[name][5][i]}')
    if char[name][5].keys()==False:
        print('Inventory empty.')

#create function distribute, get POINTS
def distribute(points):
    #set SCORES to list of three 0s
    scores=[0,0,0]
    #display you have POINTS points
    print(f'You have {points} points.')
    #get (valid) user input for how many points to put into strength
    while True:
        try:
            scor=int(simple(input('How many points do you want to put into strength? ')))
            if points-scor >=0 and scor>=0:
            #subtract that number from POINTS
                points-=scor
            else:
                print('Invalid input. Try again.')
                continue
            break
        except:
            print('Invalid input, try again.')
    #add that number of points to first in SCORES
    scores[0]+=scor
    #display you have POINTS points
    print(f'you have {points} points remaining.')
    #get (valid) user input for how many points to put into speed
    while True:
        try:
            scor=int(simple(input('How many points do you want to put into speed? (The remaining points will go into intelligence) ')))
            if points-scor >=0 and scor>=0:
            #subtract that number from POINTS
                points-=scor
            else:
                print('Invalid input. Try again.')
                continue
            break
        except:
            print('Invalid input, try again.')
    #add that number of points to second in SCORES
    scores[1]+=scor
    #display you have POINTS points put into intelligence
    print(f'The remaining {points} point go into intelligence.')
    #add POINTS to third in SCORES
    scores[2]+=points
    #return SCORES
    return scores[0],scores[1],scores[2]

#create function level_up, get character list as CHAR, get skills as SKILLS
def level_up(char,skills):
    name=char.keys()[0]
    #if CHAR is second level
    if char[name][6]==2:
        #display character is max level
        print(f'{name} is max level.')
        #return CHAR
        return char
    #set CHAR level to 2
    char[name][6]=2
    #add function distribute called on random number between 5 and 10 to CHAR scores
    char[name][1],char[name][2],char[name][3] += distribute                          #I REALLY HOPE THIS WORKS BUT IT MIGHT NOT IT DOESNT
    #display all skills in SKILLS that are for CHAR class
    #set skill in CHAR to (valid) user input for which skill they want
    #return CHAR

#create function main
    #set CHARS to empty dictionary
    #set SKILLS to dictionary, keys classes and values lists of the two avaliable skills for that class
    #loop
        #ask user if they would like to view, create characters, or exit
        #if they choose view and the CHARS is not empty
            #call function display_characters on CHARS
            #ask user if they want to view specific character, modify or delete a character, or return to start
            #if they choose to view specific character
                #call function show_character on called function search on CHARS
            #else if they choose to modify or delete
                #set SELECT to called search function on CHARS
                #ask user if they want to modify inventory, level up, remove, or change stats
                #if user chooses to modify inventory
                    #set CHARS to call function inventory on SELECT
                #else if user chooses to level up
                    #set SELECT to call function level_up on CHARS and SKILLS
                #else if user chooses to remove
                    #remove SELECT from CHARS
                #else if user chooses to change stats
                    #ask user if they want to change skills or scores
                        #if user wants to change skills, set SELECT to function call skills on SELECT
                        #else if user wants to change scores, set SELECT to function call stats on SELECT
                #update modified character in CHARS with SELECT
            #else if they choose to return to start
                #go to next loop iteration
        #if they choose create, set CHARS to run function create on CHARS
        #if they choose exit, break out of loop