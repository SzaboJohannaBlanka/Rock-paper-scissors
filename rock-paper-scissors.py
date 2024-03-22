import random

player_actions = input("Enter a choice (rock, paper, or scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer = random.choice(possible_actions)
print(f"\nYou chose {player_actions}, computer chose {computer}.\n")

if player_actions == computer:
    print(f"It's a tie")

elif player_actions == "rock":

    if computer == "scissors":
        print("Rock smashes scissors, you win")
    else:
        print("Paper covers rock, you lose")

elif player_actions == "paper":

    if computer == "rock":
        print("Paper covers rock, you win")
    else:
        print("Scissors cuts paper, you lose.")

elif player_actions == "scissors":

    if computer == "paper":
        print("Scissors cuts paper, you win")
    else:
        print("Rock smashes scissors, you lose")