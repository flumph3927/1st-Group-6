#Psuedocode for character display functions, point distribution fuction, level up function, main function

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