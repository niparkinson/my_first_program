#building a rock paper scissors game

import random

choices = ["rock", "paper", "scissors"]

computer_choice = random.choice(choices)

game = str(input("Lets play rock paper scissors. Pick Rock, Paper, or Scissors: ")).lower()

if game == computer_choice:
    print("Its a tie!", "The computer chose", computer_choice + "!")

while (game != computer_choice):
    if game == "rock" and computer_choice == "scissors":
        print("You lose!", "The computer chose", computer_choice + "!")
    elif game == "rock" and computer_choice == "paper":
        print("You Win! Congratulations", "The computer chose", computer_choice + "!")
    elif game == "paper" and computer_choice == "scissors":
        print("You Lose!", "The computer chose", computer_choice + "!")
    elif game == "paper" and computer_choice == "rock":
        print("You Win! Congratulations", "The computer chose", computer_choice + "!")
    elif game == "scissors" and computer_choice == "rock":
        print("You Lose!", "The computer chose", computer_choice + "!")
    elif game == "scissors" and computer_choice == "paper":
        print("You Win! Congratulations", "The computer chose", computer_choice + "!")
    else:
        print("Wrong input")
    break