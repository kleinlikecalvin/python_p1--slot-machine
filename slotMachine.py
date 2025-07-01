import random

# Slot symbols
slot_symbols = ["👻", "🦇", "🎃", "💀", "👹", "🧌"]

# Number of reels
num_of_reels = 3

# Starting balance
starting_balance = 100

# Ongoing balance
balance = 100


# Spin function
def spin(num_of_reels: int, slot_symbols: list[str]) -> list[str]:
    spin_result = random.choices(slot_symbols, k=num_of_reels)
    print(spin_result)
    return spin_result


# Bet function
def bet(balance, bet_amount):
    # if there is enough left in the balance for the bet_amount to be subtracted then
    # bet_amount should subtract amount from balance and spin()
    # If there isn't the user should be prompted that they either don't have enough and should add more to their balance or lower their bet
    pass


# Win function
def winner():
    # If winner then add to balance
    pass
