"""
Author: Aidan Velleca, avelleca@purdue.edu
Assignment: 12.1 - Battleship
Date: 06/29/2023

Description:
    This program creates a battleship program against the computer.

Contributors:
    N/A

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
import matplotlib.pyplot as plt
import random as r
from os.path import exists

#Size of the grid for reference
gridsize = 10

#The definiton of the ships in a dictionary
ships = {
    "Mothership" : {
            "Symbol" : 'M',
            "Layout" : [['x','M','x'], ['M', 'M', 'M'], ['x','M','x']],
            "Dimensions" : [3, 3],
            "Spaces" : 5,
            "Rotateable" : False
        },
    "Battleship" : {
            "Symbol" : 'B',
            "Layout" : [['B', 'B'], ['B', 'B']],
            "Dimensions" : [2, 2],
            "Spaces" : 4,
            "Rotateable" : False
        }, 
    "Patrol Ship" : {
            "Symbol" : 'P',
            "Layout" : [['P', 'P']],
            "Dimensions" : [1, 2],
            "Spaces" : 2,
            "Rotateable" : True
        }, 
    "Stealth Ship" : {
            "Symbol" : 'S',
            "Layout" : [['S', 'S', 'S']],
            "Dimensions" : [1, 3],
            "Spaces" : 3,
            "Rotateable" : True
        }, 
    "Destroyer" : {
            "Symbol" : 'D',
            "Layout" : [['D', 'x'], ['D', 'D']],
            "Dimensions" : [2, 2],
            "Spaces" : 3,
            "Rotateable" : False
        }, 
}

#Function for rotating matrices, used for ships
def rotate_matrix(matrix):
    transposed = []
    for row in zip(*matrix):
        transposed.append(list(row))
    rotated = []
    for row in transposed:
        rotated.append(row[::-1])
    return rotated

#Function to rotate a layout and flip the dimensions randomly for ranom ship placement
def randomly_rotate_layout(layout, base_dims):
    #Variables for the new layout and dimensions
    new_layout = layout
    new_dims = base_dims
    #Randomly rotates layout 0-3 times
    for i in range(0, r.randint(0,4)):
        new_layout = rotate_matrix(new_layout)
        new_dims = [new_dims[1], new_dims[0]]
    return new_layout, new_dims   

#Check scores to make sure no invalid scores exist: need to have three elements with a string and two numbers
def checkScore(score):
    if (len(score) != 3):
        return False
    elif (str(score[1]).isdigit == False or str(score[2]).isdigit == False):
        return False
    return True

#Read the top scores from the battleship_hof.txt file
def read_top_scores():
    #Variable for filename and scores
    filename = 'battleship_hof.txt'
    h_scores = []
    #If filename exists, read it
    if (exists(filename)):
        with open(filename, 'r') as f:
            lines = f.read().split('\n')
            h_scores = []
            #Read each line skipping header line
            for i in range(1, len(lines)):
                lines[i].replace('\n','')
                data = lines[i].split(',')
                h_scores.append(data)
    #Check scores, remove invalids
    for score in h_scores:
        if (checkScore(score) == False):
            h_scores.remove(score)
    return h_scores

#Write scores to battleship_hof
def write_new_scores(h_scores):
    filename = 'battleship_hof.txt'
    with open(filename, 'w') as f:
        #Add title line
        f.write("name,hits,misses")
        for score in h_scores:
            f.write(f"\n{score[0]},{score[1]},{score[2]}")

#Get name
def get_username_for_HOF(accuracy):
    print(
    f'''
Congratulations, you have achieved a targeting accuracy
of {accuracy:.2f}% and earned a spot in the Hall of Fame.''')
    name = input("Enter your name: ")
    print()
    return name

#Print the hall of fame
def print_HOF():
    HOF = read_top_scores()
    print(
    '''
~~~~~~~~ Hall of Fame ~~~~~~~~
Rank : Accuracy :  Player Name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
    i = 1
    for score in HOF:
        print(f"{i:>4}{accuracy(score):>10.2f}%{score[0]:>15}")
        i += 1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Print the failure message
def print_failure_message(accuracy):
    print(f"\nYour targeting accuracy was {accuracy:.2f}%.")

#Get the accuracy from a score variable
def accuracy(score):
    if (len(score) >= 2):
        return int(score[1]) / (int(score[1]) + int(score[2])) * 100
    else:
        print(f"WARNING: Score only has {len(score)} arguments, accuracy cannot be computed.")
        return -1

#Check if a score should be added to the hall of fame and add it
def check_hall_of_fame(hits, tries):
    #Get the accuracy percentage and misses
    p_accuracy = (hits / tries) * 100
    misses = tries - hits
    #Get other scores
    scores = read_top_scores()
    #Index to find score location
    index = 0
    #Increase index until you exceed length of scores or player score exceeds HOF
    while (index < len(scores) and p_accuracy <= accuracy(scores[index])):
        index += 1
    #If user's place is not last (index is not 10), add him and drop 11th score
    if (index < 10):
        #Print congratulations message and add score
        name = get_username_for_HOF(p_accuracy)
        insert_score(scores, index, name, hits, misses)
        #Drop 11th score
        scores = scores[0:10]
        #Write new scores after change
        write_new_scores(scores)
        #Print the new hall of fame
        print_HOF()
    else:
        #Print not hall of fame message
        print_failure_message(p_accuracy)

def insert_score(scores, index, name, hits, misses):
    scores.insert(index, [name, hits, misses])

def empty_grid():
    grid = [['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
            ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
            ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
            ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
            ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
            ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
            ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
            ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
            ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
            ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]
    return grid
    
#Add a ship to the grid by name
def add_ships(grid):
    #Check if ship exists
    for ship in ships.keys():
        #Get important informaton from dict
        layout = ships[ship]['Layout']
        dims = ships[ship]['Dimensions']
        rotateable = ships[ship]['Rotateable']
        #Get random layout if rotateable
        if (rotateable):
            layout, dims = randomly_rotate_layout(layout, dims)
        #Choose random position and keep looping through until a clear position is found
        clear = False
        startX = 0
        startY = 0
        while (clear == False):
            clear = True
            startX = r.randint(0, gridsize - dims[0] - 1)
            startY = r.randint(0, gridsize - dims[1] - 1)
            for i in range(0, dims[0]):
                for j in range(0, dims[1]):
                    if(grid[startX + i][startY + j] != '~'):
                        clear = False
        #Once position found, add ship to the grid
        for i in range(0, dims[0]):
            for j in range(0, dims[1]):
                grid[startX + i][startY + j] = layout[i][j]
    return grid

#Create the active ships dict
def createActiveShipsDict():
    activeShips = {}
    for ship in ships.keys():
        #Add new ship and its positions to active ships under its symbol
        symbol = ships[ship]['Symbol']
        count = ships[ship]['Spaces']
        activeShips[symbol] = {'Name': ship, 'Count': count}
    return activeShips

#Print the grid
def print_grid(grid):
    print("   0  1  2  3  4  5  6  7  8  9")
    for i in range(0, gridsize):
        print(f"{chr(65 + i)}", end='')
        for j in range(0, gridsize):
            print('  ' + grid[i][j], end = '')
        print()
    print()

#Remove the spawn blockers ('x' characters)
def remove_spawnblock(grid):
    for i in range(0, gridsize):
        for j in range(0, gridsize):
            if (grid[i][j] == 'x'):
                grid[i][j] = '~'
    return grid

#Check if a hit occured
def checkHit(grid, x, y):
    val = grid[x][y]
    hit = False
    if (val != '~'):
        hit = True
    return val, hit

#Register hit
def registerHit(val, activeShips):
    #Subtract from the count
    activeShips[val]['Count'] -= 1
    #Return the hit info
    return activeShips[val]['Name'], activeShips[val]['Count']

#Remove a ship from the active ship registry
def removeShip(val, activeShips):
    del activeShips[val]

#Get the number of ships remaining
def shipsLeft(activeShips):
    return len(activeShips)
        
#Make grid
def make_grid():
    #Make empty grid
    grid = empty_grid()
    #Create an instance of each ship to spawn
    add_ships(grid)
    #Remove temporary no-spawn points
    grid = remove_spawnblock(grid)
    #Return the grid with the ships
    return grid

#Create the activeShip dict

#Given a user input string, determine whether it is a valid target. Returns 0 for False, 1 for True, and -1 for quit
def validate_target(target):
    #Quit if user enters Q
    if (target == 'Q'):
        return -1
    #Check if valid and if not return true
    if(len(target) != 2):
                print("Please enter exactly two characters.")
                return 0
    elif(ord(target[0]) < 65 or ord(target[0]) >= 75 or ord(target[1]) < 48 or ord(target[1]) > 57):
        print('Please enter a location in the form "G6".')
        return 0
    else:
        return 1

#Print instructions
def print_instructions():
    print(
    '''
Instructions:

Ships are positioned at fixed locations in a 10-by-10
grid. The rows of the grid are labeled A through J, and
the columns are labeled 0 through 9. Use menu option
"2" to see an example. Target the ships by entering the
row and column of the location you wish to shoot. A
ship is destroyed when all of the spaces it fills have
been hit. Try to destroy the fleet with as few shots as
possible. The fleet consists of the following 5 ships:

Size : Type
5 : Mothership
4 : Battleship
3 : Destroyer
3 : Stealth Ship
2 : Patrol Ship
    ''')

#View an example map
def view_example():
    grid = make_grid()
    print_grid(grid)

#Start game
def initiate_game():
    #Active ship dict helps determine when ships are removed
    activeShips = createActiveShipsDict()
    inGame = True
    #Hit and total stats
    tries = 0
    hits = 0
    #Play grid vs display grid
    grid = make_grid()
    disp_grid = empty_grid()
    while(inGame):
        #Print the display grid before every move
        #print_grid(grid)
        print_grid(disp_grid)
        #Ask user for target
        target = input("Where should we target next (q to quit)? ").capitalize()
        valid = validate_target(target)
        #Repeat this request until input validated
        while (valid !=  1):
            if (valid == -1):
                return
            else:
                target = input("Where should we target next (q to quit)? ").capitalize()
                valid = validate_target(target)
        #Convert x and y to integers using ascii codes
        x = ord(target[0]) - 65
        y = ord(target[1]) - 48
        if(disp_grid[x][y] != '~'):
            print("You've already targeted this location.")
        else:
            #Add to the tries
            tries += 1
            #Check if player got a hit
            val, hit = checkHit(grid, x, y)
            if (hit):
                #Perform hit procedure
                hits += 1
                print("\nIT'S A HIT!")
                name, count = registerHit(val, activeShips)
                if (count == 0):
                    print(f"The enemy's {name} has been destroyed.\n", end='')
                    removeShip(val, activeShips)
                    if (shipsLeft(activeShips) == 0):
                        inGame = False
                print("\n", end='')
                disp_grid[x][y] = 'x'
            else:
                #Perform miss procedure
                print("\nmiss\n")
                disp_grid[x][y] = 'o'
    #If no longer in-game, print game complete message and then check the hall of fame
    print_game_complete()
    check_hall_of_fame(hits, tries)

def print_goodbye():
    print("Goodbye\n")

def print_introduction():
        print(
        '''
               ~ Welcome to Battleship! ~               

ChatGPT has gone rogue and commandeered a space strike
fleet. It's on a mission to take over the world.  We've
located the stolen ships, but we need your superior
intelligence to help us destroy them before it's too
late.''')

def print_game_complete():
    print("You've destroyed the enemy fleet!")
    print("Humanity has been saved from the threat of AI.\n")
    print("For now ...")
    



def get_player_option():
    #Keep running loop until return breaks it
    while(True):
        print(
        '''
Menu:
  1 : Instructions
  2 : View Example Map
  3 : New Game
  4 : Hall of Fame
  5 : Quit'''
        )
        option = input("What would you like to do? ")
        print()
        if (option.isdigit()):
            if (int(option) >= 1 and int(option) <= 5):
                return option
            else:
                print("Invalid selection.  Please choose a number from the menu.")
        else:
            print("Invalid selection.  Please choose a number from the menu.")

def main():
    playing = True
    print_introduction()
    while(playing):
        option = get_player_option()
        if (option == '1'):
            print_instructions()
        elif (option == '2'):
            view_example()
        elif (option == '3'):
            initiate_game()
        elif (option == '4'):
            print_HOF()
        else:
            print_goodbye()
            playing = False
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()