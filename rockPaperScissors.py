import random 

def user_Input(condition, computer_move): 

    print() 
    print("In this game")
    print("R - Rock")
    print("P - Paper")
    print("S - Scissor")
    print() 

    user_move = input("Please Input your Move ( R, P, S ) : ") 

    if condition == True: 
        return user_move

    else:

        for x in range(0, len(computer_move)): 

            if computer_move[x] == user_move.lower(): 
                to_pop = x 

        computer_move.pop(x) 
        
    return user_move 

        
def gameChoice():

    game_Choice = input("D0 you want there to be a possibility of a draw ? (Y/N) : ")

    if game_Choice.lower() == "y" or game_Choice.lower() == "yes": 
        return True  

    elif game_Choice.lower() == "n" or game_Choice.lower() == "no": 
        return False 

    else: 
        print("The input was not recognized, please try again.")
        gameChoice()


def game():
    user_move = user_Input(gameChoice(), computer_move)

    computer_choice = random.choice(computer_move)

    print("The computer move was : ",str(computer_choice))

    if user_move.lower() == "r": 
    
        if computer_choice == "p": 
            print("User lost. Computer Wins.")

        elif computer_choice == "s": 
            print("User Wins!! Computer Loses.")

        elif computer_choice == user_move.lower(): 
            print("Draw")

    elif user_move.lower() == "p": 

        if computer_choice == "r": 
            print("User wins")

        elif computer_choice == "s": 
            print("Computer wins.") 

        elif computer_choice == user_move.lower(): 
            print("Draw")

    elif user_move.lower()=="s": 

        if computer_choice == "p": 
            print("Computer loses.")

        elif computer_choice == "r": 
            print("User Wins. ")

        elif computer_choice == user_move.lower(): 
            print("Draw") 

    else: 

        print("Input not recognized, please try again.")
        game() 

    gameCondition() 

def gameCondition():

    game_Condition = input("Do you want to play again? (Y/N): ") 

    if game_Condition.lower() == 'y': 
        game() 

    elif game_Condition.lower() == 'n': 
        pass

    else: 
        print("Please input a valid answer.")

        gameCondition()  



computer_move = ["r", "p", "s"]

game() 





    
    