import random

def get_choices():
 player_choice=input("enter a choice(rock,paper,scissor):")
 options=["rock","paper","scissor"]
 
 computer_choice=random.choice(options)
 choices={"player":player_choice,"computer":computer_choice}
 return choices

def check_win(player,computer):
    print("you chose "+player +" computer chose "+computer)
    if player==computer:
        return("it's a tie")
    elif player=="rock":
        if computer=="scissors":
            return("rock samshes scissors!you win!")
        else:
            return("paper covers the rock!you lose!")
    elif player=="paper":
        if computer=="rock":
            return("paper covers the rock!you win!")
        else:
            return("scissors cuts the paper!you lose!")
    elif player=="scissors":
        if computer=="paper":
            return("scissors cuts the papaer!you win!")
        else:
            return("rock samashes the scissors!you lose!")

choices=get_choices()
result=check_win(choices["player"],choices["computer"])
print(result)
