# Vegas-Style Slot Machine

A simple Vegas-style electronic slot machine built with Python. This project is perfect for beginners learning Python and simulates a slot machine with spinning reels, betting, and payouts.

## Features

- Simulates spinning reels with random symbols.
- Allows the player to place bets and tracks their balance.
- Calculates winnings based on matching symbols.
- Simple text-based interface.

## How It Works

1. The player starts with a balance of $100.
2. The player places a bet for each spin.
3. The slot machine spins three reels with random symbols.
4. Winnings are calculated based on the symbols:
   - **Jackpot**: All three symbols match (10x payout).
   - **Small Win**: Two symbols match (2x payout).
   - **No Win**: No matching symbols.
5. The game ends when the player runs out of balance or chooses to quit.

## Setup Instructions

1. Install Python (version 3.6 or later).
2. Clone this repository or copy the code into a file named `slot_machine.py`.
3. Run the script in your terminal:
   ```bash
   python slot_machine.py
   ```
