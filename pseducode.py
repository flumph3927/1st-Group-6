#Main pseducode file

#Ryan
#Start off the search function (Take in the dictionary containing all of the characters):
    #Put into a loop to make sure that the input is one of the options
        #Take their input on wether they want to search by name level or skill
        #Check to see if its one of them, if it is break

    #Check to see which one of the three options it is

    #If it is a name, have them input the name they want and print out all characters that have that name
        #Allow them to select one of the characters and set that to a variable

    #If it is a class, have them input the class they want and print out all characters that have that class
        #Allow them to select one of the characters and set that to a variable

    #If it is a level, have them input the level they want and print out all characters that have that level
        #Allow them to select one of the characters and set that to a variable

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


#Edwing

#make a funtion create

    #make the user choose a name, and add it t the character dictionary as a key 

    #print the names of the name of the classes the user can choose 

    #make class equals input what their character class is going to be, with numbers to be easier, and stupid profe
    #add class to character information

    #call distribute
    #print stats
    #add stats to character information
    #print skill and say that to unlock another one they need to level up
    #add skill to character information

    #add empty inventory to character information

    #return chaacter dictionary

#Levi

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