# TAG-BROSSIER-CDOF3
Welcome to my open source project !

This repository is a small school project done in 3 hours in python using pyCharm.

Kobok Adventures is a text-based adventure game where you play as a little goblin named Kobok trying to survive in a human town. Every decision you make matters, and your survival depends on your ability to gather enough food to last the night.

Features
Interactive Gameplay: Choose from multiple options to influence the story and progress.
Random Events: Each day, experience unique random events that challenge your survival skills.
Time Management: Balance exploration and rest to make the most of your day.
Replayability: Each playthrough offers new challenges with randomized events.
How to Play
Clone the repository to your local machine:
bash
Copier
Modifier
git clone https://github.com/lelandre/kobok-adventures.git
Navigate to the project folder:
bash
Copier
Modifier
cd kobok-adventures
Run the game using Python:
bash
Copier
Modifier
python main.py
Gameplay Mechanics
Daily Routine:
Kobok wakes up at 10 AM and must survive until 12 AM. You need at least 3 units of food to survive the night.

Commands:

sleep: Skip time and consume 1 food.
explore: Trigger a random event, which may result in gaining or losing food.
Random Events:
Events include encountering wild animals, finding food, or facing dangerous situations. Choose wisely!

End of the Day:

If Kobok has at least 3 food, the day ends successfully, and you can choose to play another day.
If not, the game ends with Kobok starving.
File Structure
main.py:
The main game logic, including the introduction, game loop, and daily mechanics.

utils.py:
Contains utility functions such as time tracking, food management, and game-ending sequences.

TAG.py:
Defines all random events that occur during the game. Each event includes a description, choices, and outcomes.

Example of Random Events
The River:
You find a sparkling river. Do you drink the water? It might be poisoned...

[Yes] Risk gaining food or losing it due to poisoning.
[No] Safely avoid the risk but gain nothing.
The Merchant:
A human merchant offers food in exchange for a shiny pebble.

[Yes] Gain 2 food.
[No] The merchant leaves, and you get nothing.
Planned Features
Add more complex events with branching paths.
Introduce a health system for additional survival mechanics.
Implement an inventory system to store items and resources.
Contributing
Contributions are welcome!

Fork the repository.
Create a feature branch:
bash
Copier
Modifier
git checkout -b feature-name
Commit your changes:
bash
Copier
Modifier
git commit -m "Add a brief description of your changes"
Push to the branch:
bash
Copier
Modifier
git push origin feature-name
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.


This project is licensed under the MIT license
