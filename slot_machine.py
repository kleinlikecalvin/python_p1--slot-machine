import random
from art import tprint

# Break String
break_string = "- " * 45

# Slot symbols
slot_symbols = ["👻", "🦇", "🎃", "💀", "👹"]

# Number of reels
num_of_reels = 3

# Starting balance
starting_balance = 100

# Ongoing balance
ongoing_balance = starting_balance

# Bet Table
bet_table = [5, 10, 20, 50, 100]

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
    if bet_amount in bet_table:
        global ongoing_balance
        if bet_amount <= ongoing_balance:
            ongoing_balance -= bet_amount
            return True
        else:
            print(
                "😭 Try adding more to your balance or lower your bet, you're only working with {} left in the tank.".format(
                    ongoing_balance
                )
            )
            return False
    else:
        print(
            "Could not place bet, please choose a valid bet amount: 5, 10, 20, 50, or 100."
        )
        return False


# Add to balance function
def add_to_balance(amount_to_add):
    global ongoing_balance
    ongoing_balance += amount_to_add
    print(
        "Topped off your balance with {}! Your new balance = {}".format(
            amount_to_add, ongoing_balance
        )
    )


# Ensure that the spin_result matches the pattern
def get_payout(spin_result):
    payout = paytable.get(tuple(spin_result), 0)

    # Check for a perfect match
    if payout > 0:
        return payout
    else:
        # Check for potential matches
        for i, symbol in enumerate(spin_result):
            if symbol == spin_result[0] and symbol == spin_result[1]:
                # find that in the paytable by replacing the third with '*'
                first_two_match = [symbol, symbol, "*"]
                payout = paytable.get(tuple(first_two_match), 0)

            return payout


# Check for a win function
def check_for_winner(spin_result):
    amount_won = get_payout(spin_result)
    if amount_won > 0:
        return (True, amount_won)
    return (False, amount_won)


# Play function
def play(bet_amount: int):
    print(break_string)
    tprint("Checking balance", font="tarty2")
    print(break_string)
    bet_is_applied = bet(bet_amount)
    if bet_is_applied:
        print(
            "Bet placed! We've subtracted {} from your balance. Your new balance is {}!".format(
                bet_amount, ongoing_balance
            )
        )
        tprint("Spinning", font="isometric1")
        spin_result = spin(num_of_reels, slot_symbols)
        isWinner, amount_won = check_for_winner(spin_result)

        if isWinner:
            tprint("Wahoo", font="isometric2")
            print("🥳 You've won!! We're adding {} to your balance.".format(amount_won))
            add_to_balance(amount_won)
        else:
            tprint("Womp womp", font="isometric3")
            print("Goose eggs... try again!")


# 🎰 Call play() or add_to_balance()
# You can only bet in increments of 5, 10, 20, 50, and 100
# Then run the file in terminal (ex: python slot_machine.py)

# Example
play(2)  # Invalid amount
play(5)
play(10)
play(20)
play(25)  # Invalid amount
play(50)
play(100)
