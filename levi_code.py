#Psuedocode (and now code) for character display functions, point distribution fuction, level up function, main function

import ryan_pseducode, random

#create function display_characters, get dictionary of characters as CHARS
def display_characters(chars):
    #loop through CHARS as CHAR
    print('\nCharacters:')
    for char in chars.keys():
        #display name, class, and level of character represented by CHAR list
        print(f'{char.title()}: level {chars[char][-1]} {chars[char][0]}')

#create function show_character, get character list as CHAR
def show_character(char):
    name=list(char.keys())[0]
    #display name, class, and level of CHAR
    print(f'\n{name.title()}\nLevel {char[name][6]} {char[name][0]}\n')
    #display attribute scores
    print(f'Strength: {char[name][1]}\nSpeed: {char[name][2]}\nIntelligence: {char[name][3]}\n')
    #display skills in CHAR
    print(f'Active skill:\n{list(char[name][4].keys())[0]}: {char[name][4][list(char[name][4].keys())[0]]}\n')
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
    print(f'\nYou have {points} points.')
    #get (valid) user input for how many points to put into strength
    while True:
        try:
            scor=int(ryan_pseducode.simple(input('\nHow many points do you want to put into strength? ')))
            if points-scor >=0 and scor>=0:
            #subtract that number from POINTS
                points-=scor
            else:
                print('\nInvalid input. Try again.')
                continue
            break
        except:
            print('\nInvalid input, try again.')
    #add that number of points to first in SCORES
    scores[0]+=scor
    #display you have POINTS points
    print(f'\nYou have {points} points remaining.')
    #get (valid) user input for how many points to put into speed
    while True:
        try:
            scor=int(ryan_pseducode.simple(input('\nHow many points do you want to put into speed? (The remaining points will go into intelligence) ')))
            if points-scor >=0 and scor>=0:
            #subtract that number from POINTS
                points-=scor
            else:
                print('\nInvalid input. Try again.')
                continue
            break
        except:
            print('\nInvalid input, try again.')
    #add that number of points to second in SCORES
    scores[1]+=scor
    #display you have POINTS points put into intelligence
    print(f'\nThe remaining {points} point go into intelligence.')
    #add POINTS to third in SCORES
    scores[2]+=points
    #return SCORES
    return scores[0],scores[1],scores[2]

#create function level_up, get character list as CHAR, get skills as SKILLS
def level_up(char,skills):
    name=list(char.keys())[0]
    #if CHAR is second level
    if char[name][6]==2:
        #display character is max level
        print(f'\n{name} is max level.')
        #return CHAR
        return char
    #set CHAR level to 2
    char[name][6]=2
    #add function distribute called on random number between 5 and 10 to CHAR scores
    distr=distribute(random.randint(5,10))
    for i in range(3):
        char[name][i+1] += distr[i]
    #display all skills in SKILLS that are for CHAR class
    print('\nSkills Avaliable:')
    for i,x in skills[char[name][0]].items():
        print(f'{i}: {x}')
    #set skill in CHAR to (valid) user input for which skill they want
    skil=ryan_pseducode.simple(input('\nWould you like to use the first or the second skill?(1/2) '))
    while skil not in ['1','2']:
        print('\nInvalid input. Try again.')
        skil=ryan_pseducode.simple(input('\nWould you like to use the first or the second skill?(1/2) '))
    if skil=='1':
        char[name][4]={list(skills[char[name][0]].keys())[0]:skills[char[name][0]][list(skills[char[name][0]].keys())[0]]}
    elif skil=='2':
        char[name][4]={list(skills[char[name][0]].keys())[1]:skills[char[name][0]][list(skills[char[name][0]].keys())[1]]}
    #return CHAR
    return char
