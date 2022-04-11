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
play=True
while(play):
	your_chance=int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n"))
	
	if your_chance == 0:
	  print(rock)
	elif your_chance == 1:
	  print(paper)
	else:
	  print(scissors)
	 
	
	computer_choose = random.randint(0,2)
	
	if computer_choose == 0:
	  print("computer choose:\n" + rock)
	elif computer_choose == 1:
	  print("computer choose:\n" + paper)
	else:
	  print("computer choose:\n" + scissors)
	
	if your_chance >= 3 or your_chance <0:
	  print("you typed an invlid number, you loose!!")
	elif your_chance == 0 and computer_choose==2:
	  print("you won!!")
	elif computer_choose == 0 and your_chance ==2:
	  print("you loose!!")  
	elif computer_choose>your_chance:
	  print("you loose!!")
	elif your_chance>computer_choose:
	  print("you won!!")
	elif your_chance == computer_choose:
	  print("it's a draw.")

	cont = input("Do you want to continue(Y/N): ")
	if (cont=='Y'):
		play=True
	else:
		print("Thank you for playing!!!")
		play=False