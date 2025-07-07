import art

# TODO-4: Compare bids in dictionary
def find_highest_bid(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

print(art.logo)
all_bids = {}
should_continue_bid = True
while should_continue_bid:
    # TODO-1: Ask the user for input
    user_bid = input("What is your name?: ").title()
    bid_price = int(input("How much do you want to bid?: $"))

    # TODO-2: Save data into dictionary {name: price}
    all_bids[user_bid] = bid_price

    # TODO-3: Whether if new bids need to be added
    new_bid = input("Are there any other bidders? ").lower()
    if new_bid == "no":
        should_continue_bid = False
        find_highest_bid(all_bids)
    else:
        print("\n" * 5)



