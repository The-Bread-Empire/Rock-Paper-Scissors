import random
from time import sleep
#start of starter variables
again = 1
selection_dict = {
  1:"rock",
  2:"paper",
  3:"scissors"
}
winners_dict = {
  "rock":"scissors",
  "paper":"rock",
  "scissors":"paper"
}
#End of starter variables
print("Lets play some rock, paper, scissors")
while again == 1:
  shoot = input("Rock, paper, or scissors?: ")
  selection_map = ["rock", "paper", "scissors"]
  if shoot in selection_map:
    computer_selection = random.randint(1, 3)
    print(f"Computer selected {selection_dict[computer_selection]}")
    computer = selection_dict[computer_selection]
    if shoot.lower() == computer:
      print("You win!")
      again = 2
    elif shoot.lower() == computer:
      print("tie\nTry again\n")
    else:
      print("You lose\nTry again\n")
  else:
    print("Something went wrong please try again\n")
    