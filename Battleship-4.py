# """
# *******************************************************************************
# * Program:  Battleship Project
# * File:Battleship.py
# * Language: Python 3.7.0
# *
# * Description: This program is checks the answer of driver license exam.
# *
# * College: Husson University
# * Author: Kamal Basnet
# * Course: IT 262 Fall
# *
# * Edit History / Change Log
# * DATE                  CHANGE DESCRIPTION
# * ----------------------------------------
# * 2018-11-21            Initial program
# * 2018-11-25            Functions workflow
# * 2018-11-30            Turns Workflow
# * 2018-12-05            Validating input
# * 2018-12-15            Final Touches.
# *******************************************************************************
# """
import random

humanPlayer = [['O','O','O','O','O','O','O','O','O','O'], ['O','O','O','O','O','O','O','O','O','O'],
               ['O','O','O','O','O','O','O','O','O','O'], ['O','O','O','O','O','O','O','O','O','O'],
               ['O','O','O','O','O','O','O','O','O','O'], ['O','O','O','O','O','O','O','O','O','O']
               ,['O','O','O','O','O','O','O','O','O','O'], ['O','O','O','O','O','O','O','O','O','O'],
               ['O','O','O','O','O','O','O','O','O','O'],['O','O','O','O','O','O','O','O','O','O']]
# List for the human side of the grid
HumanGuess = [['O','O','O','O','O','O','O','O','O','O'], ['O','O','O','O','O','O','O','O','O','O'],
               ['O','O','O','O','O','O','O','O','O','O'], ['O','O','O','O','O','O','O','O','O','O'],
               ['O','O','O','O','O','O','O','O','O','O'], ['O','O','O','O','O','O','O','O','O','O']
               ,['O','O','O','O','O','O','O','O','O','O'], ['O','O','O','O','O','O','O','O','O','O'],
               ['O','O','O','O','O','O','O','O','O','O'],['O','O','O','O','O','O','O','O','O','O']]
computerPlayer = [['O','O','O','O','O','O','O','O','O','O'], ['O','O','O','O','O','O','O','O','O','O'],
                  ['O','O','O','O','O','O','O','O','O','O'], ['O','O','O','O','O','O','O','O','O','O'],
               ['O','O','O','O','O','O','O','O','O','O'], ['O','O','O','O','O','O','O','O','O','O']
               , ['O','O','O','O','O','O','O','O','O','O'], ['O','O','O','O','O','O','O','O','O','O'],
               ['O','O','O','O','O','O','O','O','O','O'],['O','O','O','O','O','O','O','O','O','O']]
usedLocation = [] # list to store the input
counter = 0 # to keep track of hits for human
count = 0 # keep track of winning for computer
# List of computer Side of the grid
def board():
    print('   Human Player                           Guess On Computer')
    print('   --------------------------------------------------------------------')
    print('    A  B  C  D  E  F  G  H  I  J           A  B  C  D  E  F  G  H  I  J  ' )

    for humanRow in range(10): # each row ranging from 1 -10 or length of the list
        rowOutput = str(humanRow + 1) +''  # makes the row 1-9
        if humanRow !=9:
            rowOutput = ' ' + str(humanRow + 1) + ''
        else:
            rowOutput = str(humanRow + 1) + '' # makes the row 10
        for humanCol in range(10):
            rowOutput = rowOutput + '  ' + str(humanPlayer[humanRow][humanCol])
        rowOutput = rowOutput + '         '
        for cpCol in range(10):
            rowOutput = rowOutput + '  ' + str(HumanGuess[humanRow][cpCol])

        print(rowOutput)
    print()

def HumanPlay():
    try:
        print("Please Choose one of the options for preassigned ships")
        print("For Choice 1, enter 1")
        print("For Choice 2, enter 2")
        print("For Choice 3, enter 3")
        print()
        HChoice = int(input('Please pick one of the following options to place your Battleships:')) # asks the human
        ## player to enter the options for choice of ship placement.
        print()
        if HChoice == 1: # if the choice is 1
            # below are the ships placement for Human Player
            #Carrier (5 Spaces)
            humanPlayer[7][0] = 'C'
            humanPlayer[7][1] = 'C'
            humanPlayer[7][2] = 'C'
            humanPlayer[7][3] = 'C'
            humanPlayer[7][4] = 'C'

            #Battleship (4 Spaces)
            humanPlayer[3][1] = 'B'
            humanPlayer[4][1] = 'B'
            humanPlayer[5][1] = 'B'
            humanPlayer[6][1] = 'B'

            #Crusier (3 Spaces)
            humanPlayer[5][5] = 'R'
            humanPlayer[5][6] = 'R'
            humanPlayer[5][7] = 'R'

            #Submarine (3 Spaces)
            humanPlayer[1][6] = 'S'
            humanPlayer[2][6] = 'S'
            humanPlayer[3][6] = 'S'

            #Destroyer (2 Spaces)
            humanPlayer[0][0] = 'D'
            humanPlayer[0][1] = 'D'

        elif HChoice == 2: # if choice is 2
            # Carrier (5 Spaces)
            humanPlayer[5][0] = 'C'
            humanPlayer[5][1] = 'C'
            humanPlayer[5][2] = 'C'
            humanPlayer[5][3] = 'C'
            humanPlayer[5][4] = 'C'

            # Battleship (4 Spaces)
            humanPlayer[0][8] = 'B'
            humanPlayer[1][8] = 'B'
            humanPlayer[2][8] = 'B'
            humanPlayer[3][8] = 'B'

            # Crusier (3 Spaces)
            humanPlayer[9][4] = 'R'
            humanPlayer[9][5] = 'R'
            humanPlayer[9][6] = 'R'

            # Submarine (3 Spaces)
            humanPlayer[0][3] = 'S'
            humanPlayer[1][3] = 'S'
            humanPlayer[2][3] = 'S'

            # Destroyer (2 Spaces)
            humanPlayer[2][4] = 'D'
            humanPlayer[2][5] = 'D'

        elif HChoice == 3: # and if the choice is 3
            # Carrier (5 Spaces)
            humanPlayer[1][3] = 'C'
            humanPlayer[1][4] = 'C'
            humanPlayer[1][5] = 'C'
            humanPlayer[1][6] = 'C'
            humanPlayer[1][7] = 'C'

            # Battleship (4 Spaces)
            humanPlayer[4][7] = 'B'
            humanPlayer[5][7] = 'B'
            humanPlayer[6][7] = 'B'
            humanPlayer[7][7] = 'B'

            # Cruiser (3 Spaces)
            humanPlayer[1][2] = 'R'
            humanPlayer[2][2] = 'R'
            humanPlayer[3][2] = 'R'

            # Submarine (3 Spaces)
            humanPlayer[9][4] = 'S'
            humanPlayer[9][5] = 'S'
            humanPlayer[9][6] = 'S'

            # Destroyer (2 Spaces)
            humanPlayer[5][5] = 'D'
            humanPlayer[5][6] = 'D'

        else: # otherwise it prints the following message.
            print(" You entered a invalid choice, Please enter a valid choice in order to play")
        board()
    except ValueError:
        print()
        print('You have entered a wrong choice, please enter either 1, 2, or 3')
        HumanPlay()
def humanTurn():
    global counter
    try:
        while counter != 17: # as long as counter is not 17 stay in the loop
            locationFire = input("Please Enter the Location where you would like to Fire: Such as A5, D2 or C3: ")
            # user input for location
            if locationFire in usedLocation: # if the location is already used
                print('You have guessed this before. Please guess Another Location.') # then prints this message
                humanTurn()
            else: # if location was not used before then moves forward with the game
                cpRow = locationFire[1]
                cpCol = locationFire[0].lower()
                col_Indexes = 'abcdefghij'
                Real_Col = col_Indexes.index(cpCol)
                Real_Row = int(cpRow)-1

                firelocationValue = computerPlayer[Real_Row][Real_Col]
                if firelocationValue in ('S', 'D', 'B', 'R', 'C'): # if location is where ships are
                    print()
                    print('Congrats, You hit the ship!') # then it's a hit
                    HumanGuess[Real_Row][Real_Col] = 'H' # marks it as hit
                    counter += 1 # adds to the counter to keep track of hits
                else:
                    print()
                    print('Sorry You missed the ship') # prints if missed
                    HumanGuess[Real_Row][Real_Col] = 'M' # marks the board as M
                usedLocation.append(locationFire) # adds to the usedLocation list to keep track of user input
                compTurn() # turns goes to computer.

        else:
            print('Congratulation! You have won. You are a Superior Being.')

    except IndexError:
        print()
        print('You entered the invalid location, Please enter the location again.')
        print()
        humanTurn()
    except ValueError:
        print()
        print('You entered the invalid location, Please enter the location again.')
        print()
        humanTurn()

def ComputerPlay():

    choice = random.randint(1,3) # Makes a random choice from 1-3
    if choice == 1: # below is the ship placement for choice 1
        # Carrier (5 Spaces)
        computerPlayer[8][0] = 'C'
        computerPlayer[8][1] = 'C'
        computerPlayer[8][2] = 'C'
        computerPlayer[8][3] = 'C'
        computerPlayer[8][4] = 'C'

        # Battleship (4 Spaces)
        computerPlayer[3][2] = 'B'
        computerPlayer[4][2] = 'B'
        computerPlayer[5][2] = 'B'
        computerPlayer[6][2] = 'B'

        # Crusier (3 Spaces)
        computerPlayer[6][5] = 'R'
        computerPlayer[6][6] = 'R'
        computerPlayer[6][7] = 'R'

        # Submarine (3 Spaces)
        computerPlayer[1][6] = 'S'
        computerPlayer[2][6] = 'S'
        computerPlayer[3][6] = 'S'

        # Destroyer (2 Spaces)
        computerPlayer[0][0] = 'D'
        computerPlayer[0][1] = 'D'

    elif choice == 2: # below is the ship placement for choice 2
        # Carrier (5 Spaces)
        computerPlayer[0][3] = 'C'
        computerPlayer[0][4] = 'C'
        computerPlayer[0][5] = 'C'
        computerPlayer[0][6] = 'C'
        computerPlayer[0][7] = 'C'

        # Battleship (4 Spaces)
        computerPlayer[4][9] = 'B'
        computerPlayer[5][9] = 'B'
        computerPlayer[6][9] = 'B'
        computerPlayer[7][9] = 'B'

        # Crusier (3 Spaces)
        computerPlayer[1][2] = 'R'
        computerPlayer[2][2] = 'R'
        computerPlayer[3][2] = 'R'

        # Submarine (3 Spaces)
        computerPlayer[9][0] = 'S'
        computerPlayer[9][1] = 'S'
        computerPlayer[9][2] = 'S'

        # Destroyer (2 Spaces)
        computerPlayer[5][5] = 'D'
        computerPlayer[5][6] = 'D'

    elif choice == 3: # below is the ship placement for choice 3
        # Carrier (5 Spaces)
        computerPlayer[5][0] = 'C'
        computerPlayer[5][1] = 'C'
        computerPlayer[5][2] = 'C'
        computerPlayer[5][3] = 'C'
        computerPlayer[5][4] = 'C'

        # Battleship (4 Spaces)
        computerPlayer[0][9] = 'B'
        computerPlayer[1][9] = 'B'
        computerPlayer[2][9] = 'B'
        computerPlayer[3][9] = 'B'

        # Cruiser (3 Spaces)
        computerPlayer[9][4] = 'R'
        computerPlayer[9][5] = 'R'
        computerPlayer[9][6] = 'R'

        # Submarine (3 Spaces)
        computerPlayer[0][0] = 'S'
        computerPlayer[1][0] = 'S'
        computerPlayer[2][0] = 'S'

        # Destroyer (2 Spaces)
        computerPlayer[2][4] = 'D'
        computerPlayer[2][5] = 'D'
def compTurn(): # makes the way for computer to play
    hpRow = random.randint(0,9) # random row from 0-9
    hpCol = random.randint(0,9) # random col from 0-9
    global count # count is global
    firelocationValue = humanPlayer[hpRow][hpCol]

    if firelocationValue in ('S', 'D', 'B', 'R',  'C'):
        print('The enemy has hit your ship!')
        print()
        humanPlayer[hpRow][hpCol] = 'H' # if hit then marks as H
        count += 1 # adds to the count to keep track of hits
    else:
        print('The enemy missed the shot')
        print()
        humanPlayer[hpRow][hpCol] = 'M' # if missed then marks as M
    if count == 17: # if 17 hits then computer wins.
        print('Sorry, Computer has won!')
        print('Thank you for playing the game. Hope you enjoyed it. ')
    else:
        board()
        humanTurn()

def main():
    board()
    HumanPlay()
    ComputerPlay()
    humanTurn()

main() # calls the whole battleship game





