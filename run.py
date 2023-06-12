import os
import random
import time


BOARD_SIZE = 8
Hidden_Pattern = [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]
Guess_Pattern = [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]
Previous_Guesses = []

"""
Clears the console screen, is uses "os" module
and thte system function to call the appropriate
command based on the operating system
"""
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

"""
This function prints the game the game board
with the current state of the hidden
and guessed patterns, it displays the row and
collumn labels along with the corresponding cells.
"""
def print_board(board):
    clear_screen()
    print("    .+*^*+. The Game Board .+*^*+.")
    print("     A   B   C   D   E   F   G   H")
    print("   ┌───┬───┬───┬───┬───┬───┬───┬───┐")
    for row_num, row in enumerate(board):
        row_label = str(row_num + 1)
        print(" " + row_label + " │ " + " │ ".join(row) + " │")
        if row_num < BOARD_SIZE - 1:
            print("   ├───┼───┼───┼───┼───┼───┼───┼───┤")
    print("   └───┴───┴───┴───┴───┴───┴───┴───┘")

"""
This function prompts the player to enter a 
guess for the location of a battleship.
It validates the input and returns the row 
and column indicates of thte guess.
"""
def get_ship_location():
    while True:
        guess = input("Enter a guess (e.g., 4B): ").upper()
        if len(guess) == 2 and guess[0] in "12345678" and guess[1] in "ABCDEFGH":
            return int(guess[0]) - 1, ord(guess[1]) - ord("A")
        print("Please enter a valid guess.")

"""
This function randomly places battleships on the
hidden patter board, is uses "randint" function
to determine the size, direction, and position of 
each battleship.
"""
def create_ships(board):
    ship_sizes = [4, 3, 2, 1]
    for size in ship_sizes:
        ship_placed = False
        while not ship_placed:
            # 0 for horizontal, 1 for vertical
            direction = random.randint(0, 1)
            if direction == 0:  # horizontal placement
                ship_r = random.randint(0, 7)
                ship_cl = random.randint(0, 8 - size)
                if all(board[ship_r][ship_cl + i] == " " for i in range(size)):
                    for i in range(size):
                        board[ship_r][ship_cl + i] = "■"
                    ship_placed = True
            else:  # vertical placement
                ship_r = random.randint(0, 8 - size)
                ship_cl = random.randint(0, 7)
                if all(board[ship_r + i][ship_cl] == " " for i in range(size)):
                    for i in range(size):
                        board[ship_r + i][ship_cl] = "■"
                    ship_placed = True

"""
This function counts the number
of hits (battleship) on the board
"""
def count_hit_ships(board):
    hit_count = 0
    for row in board:
        hit_count += row.count("■")
    return hit_count

"""
This function calculate the accuracy of the players guesses
"""
def calculate_accuracy(guesses):
    total_guesses = 20
    hits = guesses.count("X")
    accuracy = (hits / total_guesses) * 100
    return accuracy

"""
This functio allow player to return to the main menu
and start again
"""
def play_again():
    print(f"Thank you for playing Battleship, {username}")
    answer = input("To go back to the main menu just hit Enter").lower()
    return answer == "yes" or "y"

"""
This funcion prinst slowly welcome message
to the player before main menu
"""
def welcome_screen():
    welcome_message = "Welcome to the Battleship Game!"
    for char in welcome_message:
        print(char, end="", flush=True)
        time.sleep(0.1)
    print("\nLet's get ready to sink some battleships!\n")

"""
This function prints main menu
"""
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
    print(f"  -->   {username}   <--")
    print("-----------------------")

"""
This function prints rules of the game
"""
def print_rules():
    clear_screen()
    print("-----------------------")
    print("|       RULES       |")
    print("-----------------------")
    print(
        "Guess the location of the hidden battleships\n using row and column coordinates."
    )
    print(
        "Each battleship occupies multiple consecutive\n cells either horizontally or vertically."
    )
    print("You have 4, 3, 2, 1. Ships spread out on the board randomly")
    print("You have 20 turns to guess the locations of the battleships.")
    print('Enter your guess in the format "A1", "B2", etc.')
    print(
        'After each guess, the board will be updated to\n show hits ("X") and misses ("-").'
    )
    print("-----------------------")
    input("Press Enter to go back to the main menu.")

"""
This function check accuracy of players hit
"""
def print_outro(accuracy):
    clear_screen()
    print("-----------------------")
    print("|     GAME OVER     |")
    print("-----------------------")
    print("    Accuracy: {:.2f}%".format(accuracy))
    print("-----------------------")

"""
This dunction printing out up to 3
previous guesses 
"""
def print_previous_guesses():
    if Previous_Guesses:
        print("Previous Guesses:")
        num_guesses = min(len(Previous_Guesses), 3)
        for guess in Previous_Guesses[-num_guesses:]:
            print("Row:", guess[0] + 1, ", Column:", chr(guess[1] + ord("A")))
    else:
        print("No previous guesses.")

"""
This fucntion taking user username
"""
def get_username():
    welcome_screen()
    time.sleep(2)
    username = input("Enter your username: ")
    return username


username = ""
while not username:
    username = get_username()

print_welcome()
while True:
    choice = input("Enter your choice (1-3): ")

    if choice == "1":  # New Game
        create_ships(Hidden_Pattern)
        turns = 20
        guesses = []
        while turns > 0:
            print_board(Guess_Pattern)
            print_previous_guesses()
            print("Turns Remaining:", turns)
            guess = get_ship_location()

            if Guess_Pattern[guess[0]][guess[1]] == "-":
                print("You already guessed that.")
            elif Hidden_Pattern[guess[0]][guess[1]] == "■":
                print(
                    f"Congratulations, {username}! You hit a battleship.".format(
                        username
                    )
                )
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
            Hidden_Pattern = [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]
            Guess_Pattern = [[" "] * BOARD_SIZE for _ in range(BOARD_SIZE)]
            Previous_Guesses = []
            print_welcome()
    elif choice == "2":  # Rules
        print_rules()
        print_welcome()
    elif choice == "3":  # Quit
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 3.")
        print_welcome()

print("Thanks for playing Battleship!")
