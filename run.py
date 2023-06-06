import os
from random import randint


# change comments layout and style

BOARD_SIZE = 8

Hidden_Pattern = [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]
Guess_Pattern = [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]
Previous_Guesses = []

# Clears the console screen, is uses "os" module and thte system function to call the appropriate
# command based on the operating system
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# This function prints the game the game board with the current state of the hidden
# and guessed patterns, it displays the row and collumn labels along with the corresponding cells.
def print_board(board):
    clear_screen()
    print("    .+*^*+. The Game Board .+*^*+.")
    print('     A   B   C   D   E   F   G   H')
    print('   ┌───┬───┬───┬───┬───┬───┬───┬───┐')
    for row_num, row in enumerate(board):
        row_label = str(row_num + 1)
        print(' ' + row_label + ' │ ' + ' │ '.join(row) + ' │')
        if row_num < BOARD_SIZE - 1:
            print('   ├───┼───┼───┼───┼───┼───┼───┼───┤')
    print('   └───┴───┴───┴───┴───┴───┴───┴───┘')

# this function prompts the player to enter a guess for the location of a battleship.
# It validates the input and returns the row and column indicates of thte guess.
def get_ship_location():
    while True:
        guess = input("Enter a guess (e.g., 4B): ").upper()
        if len(guess) == 2 and guess[0] in "12345678" and guess[1] in "ABCDEFGH":
            return int(guess[0]) - 1, ord(guess[1]) - ord("A")
        print("Please enter a valid guess.")

# This function randomly places battleships on the hidden patter board, is uses "randint" function
# to determine the size, direction, and position of each battleship.


def create_ships(board):
    ship_sizes = [4, 3, 2, 1, ]
    for size in ship_sizes:
        ship_placed = False
        while not ship_placed:
            direction = randint(0, 1)  # 0 for horizontal, 1 for vertical
            if direction == 0:  # horizontal placement
                ship_r = randint(0, 7)
                ship_cl = randint(0, 8 - size)
                for i in range(size):
                    if board[ship_r][ship_cl + i] != " ":
                        break
                else:
                    for i in range(size):
                        board[ship_r][ship_cl + i] = "■"
                    ship_placed = True
            else:  # vertical placement
                ship_r = randint(0, 8 - size)
                ship_cl = randint(0, 7)
                for i in range(size):
                    if board[ship_r + i][ship_cl] != " ":
                        break
                else:
                    for i in range(size):
                        board[ship_r + i][ship_cl] = "■"
                    ship_placed = True

#  This function counts the number of hits (battleship) on the board


def count_hit_ships(board):
    hit_count = 0
    for row in board:
        hit_count += row.count("■")
    return hit_count

# This function calculate the accuracy of the players guesses


def calculate_accuracy(guesses):
    total_guesses = 15
    hits = guesses.count("X")
    accuracy = (hits / total_guesses) * 100
    return accuracy

# this fucntion ask the player if he or she wants to play again


def play_again():
    answer = input("Do you want to play again? (yes/no): ").lower()
    return answer == "yes"

# Function that prints welcome screen and main menu of the game


def print_welcome():
    clear_screen()
    print("-----------------------")
    print("|  The Battleship  |")
    print("-----------------------")
    print("       MAIN MENU          ")
    print("-----------------------")
    print("  1. New Game")
    print("  2. Rules")
    print("  3. Quit Program")
    print("-----------------------")

# This function prints the rules of the game


def print_rules():
    clear_screen()
    print("-----------------------")
    print("|       RULES       |")
    print("-----------------------")
    print(
        "  Guess the location of the hidden battleships using row and column coordinates."
    )
    print(
        "  Each battleship occupies multiple consecutive cells either horizontally or vertically."
    )
    print(" You have 4, 3, 2, 1. Ships sprad out on the board randomly")
    print("  You have 15 turns to guess the locations of the battleships.")
    print('  Enter your guess in the format "A1", "B2", etc.')
    print(
        '  After each guess, the board will be updated to show hits ("X") and misses ("-").'
    )
    print("-----------------------")
    input("Press Enter to go back to the main menu.")

#  this function prints the game over screen displaying the players accuracy


def print_outro(accuracy):
    clear_screen()
    print("-----------------------")
    print("|     GAME OVER     |")
    print("-----------------------")
    print("    Accuracy: {:.2f}%".format(accuracy))
    print("-----------------------")

# This function prints players previous guesses


def print_previous_guesses():
    if Previous_Guesses:
        print("Previous Guesses:")
        for guess in Previous_Guesses:
            print("Row:", guess[0] + 1, ", Column:", chr(guess[1] + ord("A")))
    else:
        print("No previous guesses.")


print_welcome()
while True:
    choice = input("Enter your choice (1-3): ")

    if choice == "1":  # New Game
        create_ships(Hidden_Pattern)
        turns = 15
        guesses = []
        while turns > 0:
            print_board(Guess_Pattern)
            print_previous_guesses()
            print("Turns Remaining:", turns)
            guess = get_ship_location()

            if Guess_Pattern[guess[0]][guess[1]] == "-":
                print("You already guessed that.")
            elif Hidden_Pattern[guess[0]][guess[1]] == "■":
                print("Congratulations! You hit a battleship.")
                Guess_Pattern[guess[0]][guess[1]] = "X"
                guesses.append("X")
                turns -= 1
            else:
                print("Sorry, you missed.")
                Guess_Pattern[guess[0]][guess[1]] = "-"
                guesses.append("-")
                turns -= 1

            Previous_Guesses.append(guess)

        accuracy = calculate_accuracy(guesses)
        print_outro(accuracy)

        if not play_again():
            break
        else:
            Hidden_Pattern = [[" "] * 8 for _ in range(8)]
            Guess_Pattern = [[" "] * 8 for _ in range(8)]
            Previous_Guesses = []
            print_welcome()
    elif choice == "2":  # Rules
        print_rules()
        print_welcome()
    elif choice == "3":  # Quit
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 3.")
