import random 

user_wins = 0 
computer_wins = 0
options = ["rock" ,"paper", "scissors"]


while True: 
    user_input = input("type rock/paper/scissors or Q to Quit: ").lower()
    if user_input == "q": 
        break

    if user_input not in options:
        continue 

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print ("Computer picked: ", computer_pick + ".")
    print ("You picked: ", user_input, "." )
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!") 
        user_wins += 1
        

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!") 
        user_wins += 1
        
   
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!") 
        user_wins += 1

    elif user_input == "scissor" and computer_pick == "rock":
        print("Computer won!") 
        computer_wins += 1
        
    elif user_input == "rock" and computer_pick == "paper":
        print("Computer won!") 
        computer_wins += 1
        
   
    elif user_input == "paper" and computer_pick == "scissors":
        print("Computer won!") 
        computer_wins += 1
        
    else: 
        print("Tie!")
        

print("You won", user_wins, "times")
print("computer" , computer_wins, "times" )

    
