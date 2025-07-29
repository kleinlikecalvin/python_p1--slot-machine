import random
import re

# Slot symbols
slot_symbols = ["👻", "🦇", "🎃", "💀", "👹", "🧌"]

# Number of reels
num_of_reels = 3

# Starting balance
starting_balance = 100

# Ongoing balance
ongoing_balance = starting_balance

# Paytable
paytable = {
    ("👻", "👻", "👻"): 1000,
    ("🦇", "🦇", "🦇"): 900,
    ("🎃", "🎃", "🎃"): 800,
    ("💀", "💀", "💀"): 700,
    ("👹", "👹", "👹"): 600,
    ("👻", "👻", "*"): 500,
    ("🦇", "🦇", "*"): 400,
    ("🎃", "🎃", "*"): 300,
    ("💀", "💀", "*"): 200,
    ("👹", "👹", "*"): 100,
    ("*", "*", "*"): 0,
}


# Spin function
def spin(num_of_reels: int, slot_symbols: list[str]) -> list[str]:
    spin_result = random.choices(slot_symbols, k=num_of_reels)
    print("Here's the result of your spin: {}".format(spin_result))
    return spin_result


# Bet function
def bet(bet_amount):
    global ongoing_balance
    if bet_amount <= ongoing_balance:
        ongoing_balance -= bet_amount
        print("Bet placed! Your new balance = {}".format(ongoing_balance))
        return True
    else:
        print(
            "😭 You're running out of money! Try adding more to your balance or lower your bet"
        )
        return False


# Add to balance function
def addToBalance(amount_to_add):
    global ongoing_balance
    ongoing_balance += amount_to_add
    print(
        "Topped off your balance with {}! Your new balance = {}".format(
            amount_to_add, ongoing_balance
        )
    )


# Ensure that the spin_result matches the pattern
# 🚨 This isn't exactly right yet but close - we are returning the value of the key which first symbol matches
# I want to be checking the amount of times a value appears in the list
def getPayout(spin_result):
    global spin_symbol_matches
    global spin_symbol_to_match
    global key_symbol_matches

    spin_symbol_matches = 0
    spin_symbol_to_match = ""
    key_symbol_matches = 0
    payout = paytable.get(tuple(spin_result), 0)

    # Check for a perfect match
    if payout > 0:
        return payout

    # Check for potential matches
    for symbol in spin_result:
        matches = spin_result.count(symbol)
        if matches == 2:
            spin_symbol_matches
            spin_symbol_to_match = symbol
            break

    for key, value in paytable.items():
        for symbol in list(key):
            if symbol == spin_symbol_to_match:
                print(symbol)
                key_symbol_matches += 1
                if key_symbol_matches == 2:
                    payout = value
                    break

    return payout


# Check for a win function
def checkForWinner(spin_result):
    amount_won = getPayout(["👹", "👹", "👻"])
    if amount_won > 0:
        return (True, amount_won)
    return (False, amount_won)


# Play function
def play(bet_amount: int):
    bet_is_applied = bet(bet_amount)
    if bet_is_applied:
        spin_result = spin(num_of_reels, slot_symbols)
        isWinner, amount_won = checkForWinner(spin_result)

        if isWinner:
            print(
                "You've won: {} 🥳 Congratulations!! We are adding that amount to your balance.".format(
                    amount_won
                )
            )
            addToBalance(amount_won)
        else:
            print("Womp womp! Goose eggs... try again!")


play(50)
play(25)
play(150)
play(70)
