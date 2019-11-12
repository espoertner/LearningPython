answer = input('Rock, Paper or Scissors?')
import random

while answer != "Quit":
  comp_pick = random.choice(['Rock', 'Paper', 'Scissors'])
  if (
    (answer == "Rock" and comp_pick == "Rock")
    or (answer == "Scissors" and comp_pick == "Scissors")
    or (answer == "Paper" and comp_pick == "Paper")
  ):
    print("You picked" , answer , "and the computer picked" , comp_pick , ". So no one won. Try again.")
  elif (
    (answer == "Rock" and comp_pick == "Paper")
    or (answer == "Scissors" and comp_pick == "Rock")
    or (answer == "Paper" and comp_pick == "Scissors")
  ):
    print("You picked" , answer , "and the computer picked" , comp_pick , ". So you lost. Try again.")
  elif (
    (answer == "Rock" and comp_pick == "Scissors")
    or (answer == "Scissors" and comp_pick == "Paper")
    or (answer == "Paper" and comp_pick == "Rock")
  ):
    print("You picked" , answer , "and the computer picked" , comp_pick , ". So you won.")
  else: (
    print("That is not a valid answer.")
  )
  answer = input('Rock, Paper or Scissors?')