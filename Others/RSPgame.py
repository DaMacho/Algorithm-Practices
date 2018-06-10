from random import random

userChoice = input("Do you choose rock, paper or scissors?: ")

computerChoice = random()
if computerChoice < 0.34:
    computerChoice = "rock"
elif computerChoice <= 0.67:
    computerChoice = "paper"
else:
    computerChoice = "scissors"

print ("user: " + userChoice)
print ("Computer: " + computerChoice)

def compare(choice1, choice2):
    if (choice1 == choice2):
        print ("The result is a tie!")
    elif (choice1 == "rock"):
        if (choice2 == "scissors"):
            print ("rock wins")
        else:
            print ("paper wins")
    elif (choice1 == "paper"):
        if (choice2 == "rock"):
            print ("paper wins")
        else:
            print ("scissors wins")
    elif (choice1 == "scissors"):
        if (choice2 == "paper"):
            print ("scissors wins")
        else:
            print ("rock wins")


compare (userChoice, computerChoice)
