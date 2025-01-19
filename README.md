# TAG-BROSSIER-CDOF3
Welcome to my open source project !

This repository is a small school project done in 3 hours in python using pyCharm.

It is a simple python script to play a text-based adventure game that works as follow:
you are a little goblin trying to survive in a city full of human, each day you must collect enough food to spend the night.
There is a loop for each hour where you can choose to sleep (skip time but lose food) or go explore to try and gather food.
When you go to explore, a random event is chosen from the TAG.py file to be your adventure for this hour.
At the end of an event, time goes up by an hour.

You are free to edit this project to fix bugs or contribute by adding new events

If you want to add a new event:
go to TAG.py and create a new event function
an event does not necessarily need to add or remove food from the player, you are free to do whatever you want !
time is updated in main.py so no need to update hours in your event.
Once you've created an event function in TAG.py add the name of your function to the event list in utils.py

have fun !

This project is licensed under the MIT license
