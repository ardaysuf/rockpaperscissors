import random

print("Welcome to the RPS game...")

wannaStart = input("Do you want to start? (yes/no): ")

if wannaStart == "no":
    quit()
elif wannaStart == "yes":
    print("Try to beat.")
    print("Let's start!")

    card = input("Your Card: ")
   
    cards = ["rock","paper","scissors"]
    
    result = random.choice(cards)
    
    if card == result:
        print("Draw!!")
        print("Computer's card was " + result)
        quit()
    elif card == "rock" and result == "paper":
        print("You lost...")
        print("Computer's card was " + result)
        quit()
    elif card == "rock" and result == "scissors":
        print("You win!!")
        print("Computer's card was " + result)
        quit()
    elif card == "paper" and result == "rock":
        print("You win!!") 
        print("Computer's card was " + result)
        quit()   
    elif card == "paper" and result == "scissors":
        print("You lost...")
        print("Computer's card was " + result)
        quit()  
    elif card == "scissors" and result == "paper":    
        print("You win!!") 
        print("Computer's card was " + result)
        quit()   
    elif card == "scissors" and result == "rock":   
        print("You lost...")
        print("Computer's card was " + result)
        quit()           
