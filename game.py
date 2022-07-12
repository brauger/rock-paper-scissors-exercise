print("Rock, Paper, Scissors, Shoot!")

print("Welcome 'Player One' to the best game you will ever play!")

user = input("Choose rock, paper or scissors: ")

if user in ["rock", "paper", "scissors"]:
    print("Player One is:" + user)
else:
    print("Invalid input")
    exit()


import random
possible = ["rock", "paper", "scissors"]
computer = random.choice(possible)

print("The computer is:" + random.choice(possible))




