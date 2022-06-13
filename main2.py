import random

comp_wins=0
player_wins=0

def choose_option():
    user_choice =("choose rock, paper or scissors")
    if user_choice in ["Rock", "rock","r", "R"]:
      user_choice = "r"

    elif user_choice in ["Paper","paper","p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors","scissors","s", "S"]:
        user_choice="s"
        
    else:
        print("Invalid Entry, try again:")
        choose_option()
    return user_choice

def computer_options ():
    comp_choice=random.randint(1,3)
    if comp_choice == 1:
       comp_choice = "r"

    elif comp_choice == 2:
         comp_choice = "p"

    else:
         comp_choice = "s"
    return comp_choice()

while True:
    print("")
    user_choice=choose_option()
    comp_choice=computer_options()
    print("")
    
    if user_choice=="r":
       if comp_choice=="r":
        print("tie: you and the computer choose the same move.")

       elif comp_choice=="p":
        print("you lose.")
        comp_wins+=1

       elif comp_choice=="s":
        print("you win.")
        player_wins+=1
    
    elif user_choice=="p":
       if comp_choice=="r":
        print("you win.")
        player_wins+=1

       elif comp_choice=="p":
        print("tie: you and the computer choose the same move.")

       elif comp_choice=="s":
        print("you lose.")
        comp_wins+=1

    elif user_choice=="s":
       if comp_choice=="r":
        print("you lose.")
        comp_wins+=1

       elif comp_choice=="p":
        print("you win.")
        player_wins+=1

       elif comp_choice=="s":
        print("tie: you and the computer choose the same move.")

    print("")
    print("player wins:" + str(player_wins))
    print("computer wins:" +str(comp_wins))
    print("")
    user_choice=input("do you want to play again? (y/n)")

    if user_choice in ["Y", "y", "yes", "Yes"]:
     pass
    elif user_choice in ["N", "n", "no", "No"]:
     break
    else:
      break