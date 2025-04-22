from os import cpu_count

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
game_images= [rock,paper,scissors]
user = int(input("what would you choose, 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user>=0 and user<=2:
    print(game_images[user])

cpu = random.randint(0,2)
print(f"Computer chose:")
print(game_images[cpu])

if user >= 3 or user<0:
    print("You lose, invalid number")
elif user ==0 and cpu ==2:
    print("You win")
elif cpu ==0 and user ==2:
    print("You lose")
elif cpu>user:
    print("You lose")
elif user>cpu:
    print("You Win!")
elif cpu == user:
    print("Its a draw")









