from random import randint
from game.utils import *



def game():
    while hours <12:
        print(separator)
        givetime()
        givefood()
        print("day survived : " + day)
        print("what do you want to do ?")
        print("[sleep]  [explore]")
        command = input()
        if command == "sleep":
            hours += 1
            food -= 1
        elif command == "explore":
            chosenevent = randint(1,10)
            events(chosenevent)
            hours += 1

    endday()

def endday():
    hours = 0
    print("you start to feel sleepy")
    if food >= 3:
        print("thankfully, you have enough food to have a good sleep")
        print("tomorrow will be a new day in a goblin's life")
        print(separator)
        print("want to play a new day ?")
        print("[yes]  [no]")
        command = input()
        if command == "yes":
            game()
            day += 1
        elif command == "no":
            print("see you next time !")
            quit()
    else:
        print("sadly, you do not have enough food,")
        print("you cuddle up in a corner and join the goblin afterlife")
        print("\n")
        print(separator)
        print("would you like to play again ?")
        print("[yes]  [no]")
        command = input()
        if command == "yes":
            intro()
        elif command == "no":
            print("see you next time !")
            quit()


#main menu
print(separator)
print("welcome to kobok adventures")
print("this is a text based adventure game")
print("to go ahead, you will need to write one of the [options] given to you")
print("play: [kobok], quit: [quit]")
command = input()
if command == "kobok":
    print(separator)
    print("welcome to this game, you can quit any time by typing quit")
    intro()
elif command == "quit":
    exitgame()
else:
    print("you need to write one of the words written inside brackets !")
