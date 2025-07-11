import random
import art
EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(user_answer, actual_answer, live):
    """Checks answer against guess, returns the number of lives"""
    # TODO 4: check if the guess is to high or low
    if user_answer == actual_answer:
        print(f"You got it! The answer was {user_answer}")
        return None
    elif user_answer > actual_answer:
        print("Too high.")
        return live - 1
    else:
        print("Too low.")
        return live - 1

#TODO 2: set difficulty for the game
def set_difficulty():
    """This sets the difficulty of the game"""
    attempts = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if attempts == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print(art.logo)
    #TODO: Welcome the user to the game
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    #TODO 1: randomly select a number between 1 and 100
    random_number = random.randint(1, 100)

    lives = set_difficulty()

    guess = 0

    #TODO 5: user should guess again
    while guess != random_number:
        print(f"You have {lives} attempts remaining to guess the number.")
        # TODO 3: let the user make a guess
        guess = int(input("Make a guess: "))

        lives = check_answer(guess, random_number, lives)

        # TODO 6: let user how many attempts are left
        if lives == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            return
        elif guess != random_number:
            print("Guess again.")

game()



