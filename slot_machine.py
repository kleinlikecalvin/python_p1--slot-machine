import random

# Slot symbols
slot_symbols = ["👻", "🦇", "🎃", "💀", "👹", "🧌"]

# Number of reels
num_of_reels = 3

# Starting balance
starting_balance = 100

# Ongoing balance
balance = 100

# Paytable
paytable = {
    ("👻", "👻", "👻"): 1000,
    ("🦇", "🦇", "🦇"): 900,
    ("🎃","🎃","🎃"): 800,
    ("💀", "💀", "💀"): 700,
    ("👹","👹","👹"): 600,
    ("👻", "👻", '*'): 500,
    ("🦇", "🦇", '*'): 400,
    ("🎃", "🎃", '*'): 300,
    ("💀", "💀", '*'): 200,
    ("👹", "👹", '*'): 100,
    ('*', '*', '*'): 0
}


# Spin function
def spin(num_of_reels: int, slot_symbols: list[str]) -> list[str]:
    spin_result = random.choices(slot_symbols, k=num_of_reels)
    print(spin_result)
    return spin_result


# Bet function
def bet(balance, bet_amount):
    if bet_amount <= balance:
        balance -= bet_amount
        print('Bet placed! Your new balance = {}'.format(balance))
        return
    else:
        print('😭 You\'re running out of money! Try adding more to your balance or lower your bet')

# Add to balance function
def addToBalance(amount_to_add):
    global balance
    balance += amount_to_add
    print('Topped off your balance with {}! Your new balance = {}'.format(amount_to_add, balance))


# Check for a win function
# 🚨 TODO update
def checkForWinner(spin_result):
    amount_won = paytable.get(tuple(spin_result), 0)
    print('payout?: {}'.format(amount_won))
    return (False, amount_won)

# Play function
def play(bet_amount: int):
    global balance
    bet(balance, bet_amount)
    spin_result = spin(num_of_reels, slot_symbols)
    isWinner, amount_won = checkForWinner(spin_result)

    if isWinner:
        print('You\'ve won: {} 🥳 Congratulations!! We are adding that amount to your balance.'.format(amount_won))
        balance += amount_won
    else:
        print('Womp womp! Goose eggs... try again!')


play(50)