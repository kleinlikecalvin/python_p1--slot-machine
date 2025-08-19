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

# Valid Bets
valid_bets = [5, 10, 20, 50, 100]

# Paytable
paytable = {
    ("👻", "👻", "👻"): 100,
    ("🦇", "🦇", "🦇"): 90,
    ("🎃", "🎃", "🎃"): 80,
    ("💀", "💀", "💀"): 70,
    ("👹", "👹", "👹"): 60,
    ("👻", "👻", "*"): 50,
    ("🦇", "🦇", "*"): 40,
    ("🎃", "🎃", "*"): 30,
    ("💀", "💀", "*"): 20,
    ("👹", "👹", "*"): 10,
    ("*", "*", "*"): 0,
}


# Play
def play():
    bet_amount = get_bet_amount()
    valid_bet_amount = check_for_valid_bet_amount(bet_amount)
    if valid_bet_amount:
        place_bet(valid_bet_amount)
    else:
        new_bet = unable_to_place_bet()
        valid_bet_amount = check_for_valid_bet_amount(new_bet)
        while not valid_bet_amount:
            new_bet = unable_to_place_bet()
            valid_bet_amount = check_for_valid_bet_amount(new_bet)
        place_bet(valid_bet_amount)


# Get user bet
def get_bet_amount():
    bet_amount = input("Enter a bet amount of 5, 10, 20, 50, or 100 >>> ")
    return bet_amount


# Check for valid bet
def check_for_valid_bet_amount(bet_amount):
    try:
        amount = int(bet_amount)
    except ValueError:
        return False

    if amount in valid_bets:
        return amount
    else:
        return False


# Could not place bet
def unable_to_place_bet():
    new_bet = input(
        "Could not place bet, please choose a valid bet amount: 5, 10, 20, 50, or 100 >>> "
    )
    return new_bet


# Handle bet
def place_bet(bet_amount: int):
    global ongoing_balance
    print(break_string)
    tprint("Checking balance", font="tarty2")
    print(break_string)
    if bet_amount <= ongoing_balance:
        ongoing_balance -= bet_amount
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
            play_again()
        else:
            tprint("Womp womp", font="isometric3")
            print("Goose eggs...!")
            play_again()
    else:
        print(
            "😭 Try adding more to your balance or lower your bet, you're only working with {} left in the tank.".format(
                ongoing_balance
            )
        )
        is_re_upping = input(
            "Would you like to add more to your balance? Type Y or N >>> "
        )
        if is_re_upping == "Y":
            re_up()
        else:
            play_again()


# Spin
def spin(num_of_reels: int, slot_symbols: list[str]) -> list[str]:
    spin_result = random.choices(slot_symbols, k=num_of_reels)
    formatted_result = " | ".join(spin_result)
    print("Here's the result of your spin: {}".format(formatted_result))
    return spin_result


# Play again
def play_again():
    next_bet = input("Place another bet of 5, 10, 20, 50, or 100 >>> ")
    valid_bet_amount = check_for_valid_bet_amount(next_bet)
    if valid_bet_amount:
        place_bet(valid_bet_amount)
    else:
        new_bet = unable_to_place_bet()
        valid_bet_amount = check_for_valid_bet_amount(new_bet)
        if valid_bet_amount:
            place_bet(valid_bet_amount)


# Re-Up
def re_up():
    deposit_amount = input("Add a non-decimal value to your balance (ex: 500) >>> ")
    try:
        amount = int(deposit_amount)
        add_to_balance(amount)
        play_again()
    except ValueError:
        print("Incorrect input.")
        re_up()


# Add to balance
def add_to_balance(amount_to_add: int):
    global ongoing_balance
    ongoing_balance += amount_to_add
    tprint("cha ching", font="isometric4")
    print(
        "Topped off your balance with {}! Your new balance = {}".format(
            amount_to_add, ongoing_balance
        )
    )


# Get payout
def get_payout(spin_result):
    payout = paytable.get(tuple(spin_result), 0)

    # Check for a perfect match
    if payout > 0:
        return payout
    else:
        # Check for potential matches
        if spin_result[0] == spin_result[1]:
            # find pattern in the paytable by replacing the third index with '*'
            first_two_match = [spin_result[0], spin_result[1], "*"]
            payout = paytable.get(tuple(first_two_match), 0)

        return payout


# Check for a win
def check_for_winner(spin_result):
    amount_won = get_payout(spin_result)
    if amount_won > 0:
        return (True, amount_won)
    return (False, amount_won)


# Run the file in terminal (ex: python slot_machine.py)
play()
