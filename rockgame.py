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
choose=int(input("What do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choose >= 3 or choose < 0:
    print("You typed an invalid number, you lose!")
    exit()

if choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
elif choose == 2:
    print(scissors)

random=random.randint(0,2)
print("Computer chose:")
if random == 0:
    print(scissors)
if random==1:
    print(paper)
if random==2:
    print(rock)

if choose==0 and random==0:
    print("You win")
elif choose==0 and random==1:
    print("You lose")
elif choose==0 and random==2:
    print("Throw again")
elif choose==1 and random==0:
    print("You lose")
elif choose==1 and random==1:
    print("Throw again")
elif choose==1 and random==2:
    print("You win")
elif choose==2 and random==0:
    print("throw again")
elif choose==2 and random==1:
    print("You win")
elif choose==2 and random==2:
    print("You lose")
