#Noah Giustini
#30041939

#print sections that can be un-commented to see the AI's hats are found in lines:
# 192, 212 and 223

#I have solved all three parts of the assignment - Noah Giustini (30041939)

#importing modules
#random will be needed to generate sudo random numbers for the AI's turn
#copy is needed for its deepcopy() function copying our hats
import random
import copy

#the welcoming statment that will get our initial amount of nuts on the table
#also makes sure that the value the player inputs is within the range of 10 and 100
#assumes the input it recieves will be an numerical value
def welcome():
    print("Welcome to the game of nuts!")
    initial_nuts = 0
    while initial_nuts < 10 or initial_nuts > 100:
        initial_nuts = int(input("How many nuts are on the table initally?? (10-100) : "))
        if initial_nuts < 10 or initial_nuts > 100:
            print("Please enter an integer value between 10 and 100")
    return initial_nuts

#function that will control the player's turn. Ensures the player input is a value of either 1 2 or 3
#assumes that the input it recives will be a numerical integer value
#takes the parameter of the player number followed by the amount of nuts on the table
def playerTurn(x,amount):
    print("Player",x ,"how many nuts will you take?")
    inRange = False
    while inRange == False:
        take = int(input("please enter an integer between 1 and 3 "))
        if take == 1 or take == 2 or take == 3:
            inRange = True
        else:
            inRange = False
    nuts = amount - take
    return nuts

#menu that will allow the player to select between the three game modes we have
#assumes for the input it recieves to be a while integer number
def mainMenu():
    print()
    print("How would you like to play?")
    print(" Player vs player (1)")
    print(" Player vs computer (2)")
    print(" Player vs trained computer (3)")
    validMode = False
    while validMode == False:
        mode = int(input("What mode would you like? (1,2, or 3): "))
        if mode == 1 or mode == 2 or mode == 3:
            validMode = True
        else:
            validMode = False
    return mode

#the game that runs for the PVP game allowing for a 2 human player game
#utelizes the above created playerTurn() function created above
#has one parameter of the abount of nuts initially on the table
def PvP (initial_nuts):
    nuts = initial_nuts
    while nuts > 0:
        print()
        print("There are ",nuts,"  nuts on the table.")
        print()
        nuts = playerTurn(1,nuts)
        if nuts <= 0:
            print("Player 1, you lose!")
            break
        print()
        print("There are ",nuts,"  nuts on the table.")
        print()
        nuts = playerTurn(2,nuts)
        if nuts <= 0:
            print("Player 2, you lose!")
            break

#initializing the number of hats we are going to create for the AI to utelize
#one parameter of the amount of nuts initially on the table
def initHats( numberOfNuts ):
    #assumes numberOfNuts is a positive integer value
    hats =[]
    for i in range(numberOfNuts):
        #add a row to each list of hats
        #each hat starts with 3 ones(1) 
        hats.append([1,1,1])
    return hats

#function to select how many nuts the AI will take from the table
#takes the lists we have created above and uses them as a probability function
#parameter of p is the input of the hats list
def select(p):
    # assumes p is a list of three positive integers
    total = p[0] + p[1] + p[2]
    r_int = random.randint(1, total)
    if (r_int <= p[0]):
        move = 1
    elif (r_int <= p[0] + p[1]):
        move = 2
    else:
        move = 3
    return move

#funtion to ask if the player wants to play another game
#function assumes that the input will be an integer value
#returns the game value to be used to determine if another game is going to be played.
def anotherGame():
    inRange = False
    while inRange == False:
        game = int(input("Would you like to play another game? yes (1) / no (2) "))
        if game == 1 or game == 2:
            inRange = True
        else:
            inRange = False
    return game
        
#the AI function that controls the actual computer player
#takes the inputs of hats initial_nuts and both our hat copies
#assumes that initial_nuts will be a positive integer value
#assumes that all three hat inputs are a list of lists contiaing only positive integer numbers
def AI(hats,initial_nuts,tempHatsPlus,tempHatsMinus):
    nuts = initial_nuts
    take = select(hats[nuts - 1])
    location = take - 1
    tempHatsPlus[nuts - 1][location] += 1
    if tempHatsMinus[nuts - 1][location] > 1:
        tempHatsMinus[nuts - 1][location] -= 1
    nuts = nuts - take
    return nuts

#function containing the player vs AI game
#utelizes playerTurn() and AI()
#the parameters are the amount of initial nuts followed by the hats list and the two copies of it that will be added and subtracted to/from
def PvCPU(initial_nuts, hats,tempHatsPlus,tempHatsMinus):
    nuts = initial_nuts
    while nuts > 0:
        print()
        print("There are ",nuts," nuts on the table.")
        print()
        nuts = playerTurn(1 , nuts)
        print()
        if nuts <= 0:
            print("Player 1, you lose!")
            return 1
        print("There are ",nuts," nuts on the table.")
        print()
        take = nuts - (AI(hats,nuts,tempHatsPlus,tempHatsMinus))
        nuts -= take
        print("The AI takes ",take," nuts")
        if nuts <= 0:
            print("Player 1, you win!")
            return 0

#fuction to train the AI
#Is essentially the same as the other games but does games of AI vs AI siletly and will return the resultant winner
#the parameters are the amount of initial nuts followed by the hats list and the four copies of it that will be added and subtracted to/from
def AItraining(initial_nuts, hats,tempHatsPlus1,tempHatsMinus1,tempHatsPlus2,tempHatsMinus2):
    nuts = initial_nuts
    while nuts > 0:
        nuts = AI(hats,nuts,tempHatsPlus1,tempHatsMinus1)
        if nuts <= 0:
            return 1
        nuts = AI(hats,nuts,tempHatsPlus2,tempHatsMinus2)
        if nuts <= 0:
            return 0
        
#the main game function. This is the only function we end up calling and it contains the entire game within it
#makes use of all functions created above in some way shape or form
def main():
    initial_nuts = welcome()
    gameMode = mainMenu()
    #game mode one is the PVP game. this will run the pvp game and at the end of it it will offer the players the ability to play again
    if gameMode == 1:
        game = 1
        while game == 1:
            nuts = initial_nuts
            PvP(nuts)
            game = anotherGame()
    elif gameMode == 2:
        #game mode two is the player vs the untrained computer. as the player plays against the cpu player it will learn and slowly get better as it wins or loses
        #at the end of each game the player is offered the ability to play against the computer again
        #if the player choses to do so then the cpu will learn from its previous move set and choose its nuts accordingly
        nuts = initial_nuts
        hats = initHats(nuts)
        game = 1
        while game == 1:
            tempHatsPlus = copy.deepcopy(hats)
            tempHatsMinus = copy.deepcopy(hats)
            nuts = initial_nuts
            aiwin = PvCPU(nuts,hats,tempHatsPlus,tempHatsMinus)
            if aiwin == 1:
                hats = tempHatsPlus
            elif aiwin == 0:
                hats = tempHatsMinus
            #print(hats)
            #uncomment this if you want to see the AI's hats after the game
            game = anotherGame()

    elif gameMode == 3:
        #game mode three first trains the AI in how to play the game and then puts the player against it
        #upon completion of the game the player can continue to play agains this AI and it will slowly learn from the moves it makes agains the player
        nuts = initial_nuts
        hats = initHats(nuts)
        print("Training the computer player, please wait...")
        for i in range(100000):
            tempHatsPlus1 = copy.deepcopy(hats)
            tempHatsMinus1 = copy.deepcopy(hats)
            tempHatsPlus2 = copy.deepcopy(hats)
            tempHatsMinus2 = copy.deepcopy(hats)
            winner = AItraining(initial_nuts, hats,tempHatsPlus1,tempHatsMinus1,tempHatsPlus2,tempHatsMinus2)
            if winner == 1:
                hats = tempHatsPlus2
            elif winner == 0:
                hats = tempHatsPlus1
        #print(hats)
        #uncomment this if you want to see the hats after the training
        game = 1
        while game == 1:
            tempHatsPlus = copy.deepcopy(hats)
            tempHatsMinus = copy.deepcopy(hats)
            aiwin = PvCPU(initial_nuts, hats,tempHatsPlus,tempHatsMinus)
            if aiwin == 1:
                hats = tempHatsPlus
            if aiwin == 0:
                hats = tempHatsMinus
            #print(hats)
            #uncomment this if you would like to see the AI's hats
            game = anotherGame()
            
#calling main()
main()
