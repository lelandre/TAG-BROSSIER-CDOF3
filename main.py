import game.utils as utils
from random import randint


def intro():
    input()
    print(utils.separator)
    print("You are a little goblin named Kobok,")
    print("trying to make a living in a town full of humans.")
    print("Times are harsh, but you make do with what you have.")
    input("*press any key to continue*")
    print(utils.separator)
    print("As a good little goblin, you wake up at 10 AM and go to sleep at midnight.")
    print("Try to eat enough to survive the night!")
    print("You need at least 3 food to survive.")
    input("*press any key to continue*")
    game()


def game():
    while utils.hours < 24:
        print(utils.separator)
        utils.givetime()
        utils.givefood()
        print(f"Days survived: {utils.days}")
        print("What do you want to do?")
        print("[sleep] [explore]")
        command = input()
        if command == "sleep":
            print("You find a spot to rest and sleep for 3 hours.")
            utils.hours += 3
            utils.food -= 1
        elif command == "explore":
            chosenevent = randint(0, len(utils.events) - 1)
            food_change = utils.events[chosenevent]()  # Execute the event
            utils.food += food_change
            utils.hours += 1
            input()
        else:
            print("Invalid choice. Type one of the options in brackets!")

    endday()


def endday():
    print("You start to feel sleepy.")
    if utils.food >= 3:
        print("Thankfully, you have enough food to have a good sleep.")
        print("Tomorrow will be a new day in a goblin's life.")
        print(utils.separator)
        print("Want to play a new day?")
        print("[yes] [no]")
        command = input()
        if command == "yes":
            utils.food -= 3
            if utils.food < 0:
                utils.food = 0
            utils.days += 1
            utils.hours = 10
            game()
        elif command == "no":
            print("See you next time!")
            quit()
        else:
            print("You need to write one of the words written inside brackets!")
    else:
        gameover()

def gameover():
    print("Sadly, you do not have enough food,")
    print("You cuddle up in a corner and join the goblin afterlife.")
    print("\n")
    print(utils.separator)
    print("Would you like to play again?")
    print("[yes] [no]")
    command = input()
    if command == "yes":
        intro()
    elif command == "no":
        print("See you next time!")
        quit()
    else:
        print("You need to write one of the words written inside brackets!")


# Main menu
while True:
    print(utils.separator)
    print("Welcome to Kobok Adventures!")
    print("This is a text-based adventure game.")
    print("To progress, type one of the [options] given to you.")
    print("Play: [kobok], Quit: [quit]")
    command = input()
    if command == "kobok":
        print(utils.separator)
        print("Welcome to the game! You can quit anytime by typing quit.")
        input("*press any key to continue*")
        intro()
    elif command == "quit":
        utils.exitgame()
    else:
        print("You need to write one of the words written inside brackets!")
        input("*press any key to continue*")
