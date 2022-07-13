print("Rock, Paper, Scissors, Shoot!")

print("Welcome 'Player One' to the best game you will ever play!")


user = input("Choose rock, paper or scissors: ")


if user.lower() in ["rock", "paper", "scissors"]:
    print("Player One is:" + user) 
else:
    print("Invalid input")
    exit()


import random
possible = ["rock", "paper", "scissors"]
computer = random.choice(possible)

print("The computer is: " + computer)



if user == computer:
    print("It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("Rock crushes scissors. You win!")
    else:
        print("Paper covers rock. You lose.")
elif user == "paper":
    if computer == "rock":
        print("Paper covers rock. You win!")
    else:
        print("Scissors cuts paper. You lose.")
elif user == "scissors":
    if computer == "paper":
        print("Scissors cuts paper. You win!")
    else:
        print("Rock crushes scissors. You lose.")




print("Thank you for playing. Hope you had fun!")
