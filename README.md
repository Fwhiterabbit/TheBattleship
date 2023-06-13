# The game begins by displaying an intro where user can provide his nickname, after that we can go to the Main Menu.
![intro](https://github.com/Fwhiterabbit/TheBattleship/assets/122694703/6e77d5a7-84e8-415e-bda6-7c96c4ad2b92)

## New Game:
![baord](https://github.com/Fwhiterabbit/TheBattleship/assets/122694703/c7a243b9-5b24-4bc7-9708-4dbf99cc0097)
#### Upon selecting this option, the game initializes a game board and randomly places battleships on the hidden pattern board.
#### The player has 20 turns to guess the locations of the battleships by entering row and column coordinates (e.g., "4B").
#### After each guess, the game updates the board to indicate hits ("X") and misses ("-").
#### If the player hits a battleship, a congratulatory message is displayed.
#### If the player misses, a message indicating a miss is displayed.
#### The game keeps track of previous guesses and displays up to three of the most recent guesses.


## Rules:
#### Selecting this option displays the rules of the game, providing an explanation of how to play Battleship.
#### After reading the rules, the player can press Enter to return to the main menu.
![rules](https://github.com/Fwhiterabbit/TheBattleship/assets/122694703/1e063d5a-6694-4d5f-acd2-c3208d325aa9)

## End Game:
#### After 20 turns, the game ends, and the player's accuracy is calculated based on the number of hits.
#### The game displays the accuracy percentage and prompts the player to play again or return to the main menu.
![end game](https://github.com/Fwhiterabbit/TheBattleship/assets/122694703/fe796e51-79c0-4d45-83cd-7ea612366842)

## Quit Program:
#### Choosing this option terminates the game and ends the program.
#### The game incorporates various functions to handle different aspects:

#### The game board is displayed using the print_board() function.
#### User input for guessing ship locations is obtained through the get_ship_location() function.
#### Battleships are randomly placed on the hidden pattern board using the create_ships() function.
#### The count_hit_ships() function counts the number of hits (battleships) on the board.
#### The calculate_accuracy() function calculates the player's accuracy based on their hits.
#### The play_again() function prompts the player to play again or return to the main menu.
#### The welcome_screen() function displays a slowly printed welcome message before the main menu.
#### The print_previous_guesses() function prints up to three previous guesses made by the player.
#### The get_username() function prompts the player to enter their username.

## Testing:
#### The code was tested and validate usgin flake8, major issues were fixed. The ones that remain are due to strings being too long. With regard to the strings length, it has been decided that they are to remain as is for design purposes.
![PEP8](https://github.com/Fwhiterabbit/TheBattleship/assets/122694703/c10ff911-bfff-4219-8bc8-19a4810cdb39)
#### How to validate python using flake8 method:
1. Install 'flake8' by running the following command in your terminal
- pip install flake8
2. Navigate to the directory where your Python file is located
3. Run 'flake8' followed by the name of your Python file.
- flake8 run.py
4. Replace 'run.py' with the actual name of your Python file.
## Bugs:
#### No bugs have been found
## Development and App control
#### Whole app was constructed and developed using Visual Studio Code ( that is why there minght be high uploads on GitHub and lack of commits ) !
## Deplyment:
#### The application has been deployed to heroku. The steps taken were:
#### Heroku:

##### Open the "new" menu and click on "Create new app".
##### Fill form fields with app name and region (Europe or USA) depends on where are you live. Click on "Create app".
##### In the "Settings" section, click on "Add buildpack" and add Python and NodeJS, in that order.
##### In "Deployment method", select the GitHub option and provide the repository details. Click on "Connect".
##### Click on "Enable Automatic Deploys" and finally, click on "Deploy Branch" with comprahending repository.

## Credits:
- Game developed with the assistance of ChatGPT, an AI language model created by OpenAI.
- Thank you to ChatGPT for helping in the development of this app.

Overall, Python game provides a text-based Battleship experience where the player tries to sink battleships within a limited number of turns.
