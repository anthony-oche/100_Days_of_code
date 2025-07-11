import random
from game_data import data
from art import logo, vs


#TODO 3: function to compare the followers of the randomly selected accounts
def compare(acct_a, acct_b, choice):
    """Takes 2 accounts and users choice and returns if they are correct"""
    global score
    if acct_a['follower_count'] > acct_b['follower_count'] and choice == 'a':
        score += 1
        print(f"You're right! Current score: {score}")
        return True
    elif acct_b['follower_count'] > acct_a['follower_count'] and choice == 'b':
        score += 1
        print(f"You're right! Current score: {score}")
        return True
    else:
        return False

print(logo)

score = 0
#generate a random account
account_b = random.choice(data)

should_continue = True
while should_continue:
    #TODO 1: generate random A and B to be compared from the game data
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    #put the generated random accounts in a printable format
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
    print(vs)
    print(f"Against B: {account_b['name']}, {account_b['description']}, {account_b['country']}.")


    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 5)

    should_continue = compare(account_a, account_b, user_choice)

print(f"Sorry, that's wrong. Final score: {score}")