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

#Write your code below this line 👇
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input > 2:
    print("something is wrong! Please enter valid number")
else:
    rps = [rock, paper, scissors]
    print(rps[user_input])
    ci = random.choice(rps)
    print(f"Computer chose:\n {ci}")

    if ci == rock:
        computer_input = 0
    elif ci == paper:
        computer_input = 1
    else:
        computer_input = 2


    if user_input == computer_input:
        print("it's a draw")
    elif (user_input == 0 and computer_input == 2) or (user_input == 1 and computer_input == 0) or (user_input == 2 and computer_input == 1):
        print("You win!")
    elif (user_input == 0 and computer_input == 1) or (user_input == 1 and computer_input == 2) or (user_input == 2 and computer_input == 0):
        print("You lose!")
    else:
        print("something is wrong! Please enter valid number")
