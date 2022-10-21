rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random


player = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

bot = random.randint(0, 2)

#PLAYER CHOSE SOMETHING ELSE
if player != "0" and player != "1" and player != "2":
  print("You need to choose: 0, 1 or 2! Don't type something else!") 
#PLAYER CHOSE ROCK
if player == "0":
  print(rock)
  if bot == 0:
    print(f"Computer chose: {rock}")
    print("You draw")
  elif bot == 1:
    print(f"Computer chose: {paper}")
    print("You lose")
  else:
    print(f"Computer chose: {scissors}")
    print("You win")
#PLAYER CHOSE PAPER
if player == "1":
  print(paper)
  if bot == 0:
    print(f"Computer chose: {rock}")
    print("You win")
  elif bot == 1:
    print(f"Computer chose: {paper}")
    print("You draw")
  else:
    print(f"Computer chose: {scissors}")
    print("You lose")
#PLAYER CHOSE SCISSORS
if player == "2":
  print(scissors)
  if bot == 0:
    print(f"Computer chose: {rock}")
    print("You lose")
  elif bot == 1:
    print(f"Computer chose: {paper}")
    print("You win")
  else:
    print(f"Computer chose: {scissors}")
    print("You draw")

