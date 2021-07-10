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
list_of_array = [rock,paper,scissors]
user_choice = int(input("Which option do you choose? 0(Rock) 1(Paper) 2(scissors) : "))
computer_choice = random.randint(0,2)

print("Computer_choice:")
print(list_of_array[computer_choice])

print("User choice:")
print(list_of_array[user_choice])


if user_choice == computer_choice:
  print("OPPS! Its a tie")
elif user_choice== 0 and computer_choice == 1:
  print("You Lost")
elif user_choice == 0 and computer_choice == 2:
  print("You win") 
elif user_choice == 1 and computer_choice == 0:
  print("You win")
elif user_choice == 1 and computer_choice == 2:
  print("You lost")
elif user_choice == 2 and computer_choice == 0:
  print("You lost")
elif user_choice == 2 and computer_choice == 1:
  print("You win")
else:
  print("You win")
