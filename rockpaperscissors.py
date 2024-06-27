import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])  
    
def get_user_choice():
    choice = input("Enter your choice [rock, paper, scissors]: ").strip().lower()
    while choice not in ('rock', 'paper', 'scissors'):
        print("Entered option is invalid.")
        choice = input("Enter your choice [rock, paper, scissors]: ").strip().lower()
    return choice
    
def finalwinner(userchoice, computerchoice):
    if userchoice == computerchoice:
        return "tie"
    
    elif(userchoice == "rock" and computerchoice == "scissors") or \
        (userchoice == "paper" and computerchoice == "rock") or \
        (userchoice == "scissors" and computerchoice == "paper"):
            return "user"
            
    else:
        return "computer"
        

def display(userchoice, computerchoice, winner):
    print("You chose: ", userchoice)
    print("Computer chose: ", computerchoice)
    if winner == "tie":
        print("It's a tie")
    elif winner == "user":
        print("You Win!")
    else:
        print("You Lose!")
        

def game():
    userscore = 0
    computerscore = 0
    while True:
        userchoice = get_user_choice()
        computerchoice = get_computer_choice()
        winner = finalwinner(userchoice, computerchoice)
        
        display(userchoice, computerchoice, winner)
        
        if winner == "user":
            userscore += 1
        elif winner  == "computer":
            computerscore += 1
        
        x = input("Do you want to play again? (Y/N): ")
        if x not in "Yy":
            break
        
    print("Final Score: ")
    print("Your Score:", userscore, "-", "Computer Score:", computerscore)
    
    
game()
        
    

    
