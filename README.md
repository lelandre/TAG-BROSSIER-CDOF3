Welcome to my open source project !

this is a school project done in python in 3 hours using pyCharm

Kobok Adventures is a text-based adventure game where you play as a goblin named Kobok, striving to survive in a human town. Make strategic choices to gather enough food and survive each day. Explore, sleep, or take risks to manage your time and resources wisely.

Features
Dynamic day-night cycle starting at 10 AM and ending at midnight.
A variety of randomized events with consequences for your food levels.
Multiple choices at each step that affect the gameplay.
Simple text-based interface.

File Structure
main.py:
The main entry point of the game, handles game flow, introduction, and day progression.

utils.py:
Contains utility functions for managing the game state (time, food, days).
Defines the list of randomized events.
Provides helper functions like exitgame, givetime, and givefood.

TAG.py:
Defines 12 unique randomized events triggered during exploration.
Each event affects food levels positively or negatively based on the player's choices.

How to Play:
Run main.py to start the game.
Follow the on-screen instructions to make choices:
Type [kobok] to begin a new game.
Type [quit] to exit the game.
During the game:
Choose [sleep] to rest for 3 hours at the cost of 1 food.
Choose [explore] to trigger a random event, potentially gaining or losing food.
Survive until the end of the day by having at least 3 food.
At the end of the day, decide to continue surviving another day or quit the game.
Random Events
Events are defined in TAG.py. Each event offers unique scenarios where the player can:
Gain food (e.g., stealing bread, finding berries).
Lose food (e.g., being caught by humans, drinking poisoned water).
Choose wisely to maximize survival.

Game Rules
Each game day starts at 10 AM and ends at midnight.
Manage your time (hours) and food carefully:
Sleep spends 3 hours and costs 1 food.
Explore spends 1 hour and may affect food levels positively or negatively.
If you have less than 3 food at the end of the day, the game ends.

Game Flow
Introduction: The game introduces Kobok and the survival challenge.

Gameplay:
Choose actions (sleep or explore) until the day ends.
Random events occur during exploration.

End of Day:
If food is ≥ 3, proceed to the next day.
If food is < 3, the game ends.
Game Over: Decide to restart or quit.

Installation & Execution
Clone the repository or download the project files.
Ensure Python 3.6+ is installed.

Run the game:
bash
Copier
Modifier
python main.py
Dependencies
Python Standard Library:
random for event randomization.
input for user interaction.
Contribution
Contributions are welcome! To add new events:

Define the event function in TAG.py following the format of existing events.
Append the new event to the events list in utils.py.
License
This project is licensed under the MIT License.
