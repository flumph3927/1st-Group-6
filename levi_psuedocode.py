#Psuedocode for character display functions, level up function, main function

#create function display_characters, get dictionary of characters as CHARS
    #loop through CHARS as CHAR
        #display name, class, and level of character represented by CHAR list

#create function show_character, get character list as CHAR
    #display name, class, and level of CHAR
    #display attribute scores
    #display skills in CHAR
    #display inventory of CHAR

#create function distribute, get POINTS
    #set SCORES to list of three 0s
    #display you have POINTS points
    #get (valid) user input for how many points to put into strength
    #add that number of points to first in SCORES
    #subtract that number from POINTS
    #display you have POINTS points
    #get (valid) user input for how many points to put into speed
    #add that number of points to second in SCORES
    #subtract that number from POINTS
    #display you have POINTS points put into intelligence
    #add POINTS to third in SCORES
    #return SCORES

#create function level_up, get character list as CHAR, get skills as SKILLS
    #if CHAR is second level
        #display character is max level
        #return CHAR
    #set CHAR level to 2
    #add function distribute called on random number between 5 and 10 to CHAR scores
    #display all skills in SKILLS that are for CHAR class
    #set skill in CHAR to (valid) user input for which skill they want
    #return CHAR