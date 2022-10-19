
#rock paper scissors game
import random

def getChoices():
  player_choice = input("Enter your choice:")
  comp_options = ["rock", "paper", "scissors"]
  comp_choice = random.choice(comp_options)
  choices = {"player": player_choice ,"computer":comp_choice}
  return choices


def checkWin(player,computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win."
    else:
      return "Paper covers rock!You lose."
  elif player == "scissors":
    if computer == "paper":
      return "scissors cuts paper! You win."
    else:
      return "Rock smashes scissors!You lose."
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win."
    else:
      return "scissors cuts paper!You lose."  
  
choices = getChoices()
result = checkWin(choices["player"],choices["computer"])
print(result)


  
   
  
    