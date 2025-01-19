import game.utils as utils
from random import randint


def intro():
    """
    Introduces the game, providing context and rules to the player.
    Waits for user input to proceed through the introduction.
    """
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
    game()  # Starts the main game loop


def game():
    """
    Main game loop where the player makes choices each hour.
    Updates game state based on player actions until the day ends.
    """
    while utils.hours < 24:  # The day ends after 24 hours
        print(utils.separator)
        utils.givetime()  # Displays the current time
        utils.givefood()  # Displays the current food level
        print(f"Days survived: {utils.days}")
        print("What do you want to do?")
        print("[sleep] [explore]")
        command = input()  # Waits for the player's choice

        if command == "sleep":
            # Player chooses to sleep, which costs time and food
            print("You find a spot to rest and sleep for 3 hours.")
            utils.hours += 3
            utils.food -= 1
        elif command == "explore":
            # Player chooses to explore, triggering a random event
            chosenevent = randint(0, len(utils.events) - 1)  # Randomly selects an event
            food_change = utils.events[chosenevent]()  # Executes the event and returns food changes
            utils.food += food_change
            utils.hours += 1  # Exploring takes 1 hour
            input()
        else:
            # Handles invalid inputs
            print("Invalid choice. Type one of the options in brackets!")

    endday()  # Ends the day and checks survival conditions


def endday():
    """
    Ends the current day. Checks if the player has enough food to survive.
    If they do, the game can continue to a new day. Otherwise, it ends.
    """
    print("You start to feel sleepy.")
    if utils.food >= 3:
        # Player has enough food to survive
        print("Thankfully, you have enough food to have a good sleep.")
        print("Tomorrow will be a new day in a goblin's life.")
        print(utils.separator)
        print("Want to play a new day?")
        print("[yes] [no]")
        command = input()  # Asks the player if they want to continue

        if command == "yes":
            # Prepares the game for the next day
            utils.food -= 3  # Deducts food needed to survive
            if utils.food < 0:
                utils.food = 0  # Ensures food doesn't drop below zero
            utils.days += 1
            utils.hours = 10  # Resets time to the start of the day
            game()  # Starts a new day
        elif command == "no":
            # Ends the game if the player chooses not to continue
            print("See you next time!")
            quit()
        else:
            # Handles invalid inputs
            print("You need to write one of the words written inside brackets!")
    else:
        # Player does not have enough food to survive
        gameover()


def gameover():
    """
    Handles the game-over scenario when the player runs out of food.
    Asks if they want to restart the game or quit.
    """
    print("Sadly, you do not have enough food,")
    print("You cuddle up in a corner and join the goblin afterlife.")
    print("\n")
    print(utils.separator)
    print("Would you like to play again?")
    print("[yes] [no]")
    command = input()  # Asks the player if they want to restart

    if command == "yes":
        # Restarts the game
        intro()
    elif command == "no":
        # Ends the game
        print("See you next time!")
        quit()
    else:
        # Handles invalid inputs
        print("You need to write one of the words written inside brackets!")


# Main menu
while True:
    """
    Displays the main menu where the player can start the game or quit.
    Loops until the player makes a valid choice.
    """
    print(utils.separator)
    print("Welcome to Kobok Adventures!")
    print("This is a text-based adventure game.")
    print("To progress, type one of the [options] given to you.")
    print("Play: [kobok], Quit: [quit]")
    command = input()  # Waits for the player's choice

    if command == "kobok":
        # Starts the game
        print(utils.separator)
        print("Welcome to the game! You can quit anytime by typing quit.")
        input("*press any key to continue*")
        intro()
    elif command == "quit":
        # Exits the game
        utils.exitgame()
    else:
        # Handles invalid inputs
        print("You need to write one of the words written inside brackets!")
        input("*press any key to continue*")
