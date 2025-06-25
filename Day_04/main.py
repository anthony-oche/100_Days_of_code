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

game_is_on = True
while game_is_on:
    img_list = [rock, paper, scissors]
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. type 911 stop game. "))
    computer_choice = random.randint(0, 2)
    print(img_list[user_choice])
    print(f"Computer chose: {img_list[computer_choice]}")

    #check for when the user wins or lose
    if user_choice == 911:
        game_is_on = False
    elif user_choice >=3 or user_choice < 0:
        print("Invalid Number. Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    elif user_choice == computer_choice:
        print("It's a draw")
    elif user_choice == 2 and computer_choice == 1:
        print("You win")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose")
    elif user_choice == 1 and computer_choice == 0:
        print("You win")
    elif user_choice == 0 and computer_choice == 1:
        print("You lose")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose")

    print("\n")