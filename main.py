import random

MAX_LINES = 5
MAX_BET = 1000
MIN_BET = 1

ROWS = 5
COLS = 3

symbol_count = {
    "🍒": 8,
    "🍋": 6, 
    "🔔": 4,
    "⭐": 3, 
    "💎": 2, 
}

symbol_values = {
    "🍒": 5,
    "🍋": 4, 
    "🔔": 3,
    "⭐": 2, 
    "💎": 1, 
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines

def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

def print_slot_machine(columns, lines):
    for row in range(lines):  
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")  
            else:
                print(column[row]) 
        
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than $0.")
        else:
            print("Please enter a number.")
        
    return amount

def get_line_number():
    while True:
        lines = input("How many lines would you like to bet on (1 - " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
        
    return amount

def spin(balance):
    lines = get_line_number()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough money to bet. Your current balance is ${balance}.")
        else:
            break
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")

    slots = get_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots, lines) 
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won {winnings}!")

    if len(winning_lines) > 0:
        print(f"You won on lines:", *winning_lines)
    else:
        print("Sorry, you didn't win on any lines :(")

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}!")

main()