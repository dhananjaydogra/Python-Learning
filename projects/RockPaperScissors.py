#Rock Paper Scissors Game
import random

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

options=[rock,paper,scissors]
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
entered_index= input()
rand_index=random.randint(0,2)
if entered_index == '0' or entered_index == '1' or entered_index =='2' :
    entered_index=int(entered_index)
    print(options[entered_index])
    print("\nComputer chose:\n")
    print(options[rand_index])
    if entered_index==rand_index:
         print("It's a draw")
    elif (entered_index==0 and rand_index==2) or (entered_index==1 and rand_index==0) or (entered_index==2 and rand_index==1) :
        print("You win!")
    else:
         print("You lose")
else:
    print("You typed an invalid input, you lose!")