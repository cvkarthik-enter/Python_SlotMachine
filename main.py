# Based on the video by Tech with Tim

# we are writing a simple text based slot machine program
# this will allow us to be come familiar with python

import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

COLS = 3
ROWS = 3
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def get_slotmachine_spin(cols, rows, symbols):

    # creating a list of symbols as per the count in symbol_count dictionary
    all_symbols = []
    for symbol, symboly_count in symbols.items():
        for _ in range(symboly_count):
            all_symbols.append(symbol)

    # generating the columns. This depends on rows, symbol_count and number of columns
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


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
            winning_lines.append(line + 1)

    return winnings, winning_lines


def print_slotmachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("Enter your deposit amount? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Kindly enter value > 0")
        else:
            print("Kindly enter a number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1 - " + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines between 1 - ", str(MAX_LINES))
        else:
            print("Kindly enter a number.")
    return lines


def get_bet():
    while True:
        bets = input(f"Enter the bet amount on each line (${MIN_BET} - ${MAX_BET}): ")
        if bets.isdigit():
            bets = int(bets)
            if MIN_BET <= bets <= MAX_BET:
                break
            else:
                print(f"Enter a valid bet amount between ${MIN_BET} - $", str(MAX_BET))
        else:
            print("Kindly enter a number.")
    return bets


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Your total bet ${total_bet} is greater than the available current balance of ${balance} ")
        else:
            break
    print(f"Total bet is : ${total_bet}, where you bet ${bet} on each of the {lines}.")

    slots = get_slotmachine_spin(ROWS, COLS, symbol_count)
    print_slotmachine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print("You won on lines: ", *winning_lines)

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        ans = input("Press enter to spin or Q/q to quit: ")
        if ans.lower() == 'q':
            break
        balance += spin(balance)
        print(f"You are left with ${balance}.")




if __name__ == "__main__":
    main()