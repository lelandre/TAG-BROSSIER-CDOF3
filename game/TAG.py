def event1():
    while True:
        print("You found a bush full of berries! Do you want to pick them?")
        print("[yes] [no]")
        command = input()
        if command == "yes":
            print("You pick the berries and gain 2 food.")
            return 2  # Gain 2 food
        elif command == "no":
            print("You decided not to risk it. No food gained.")
            return 0  # No change
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")

def event2():
    while True:
        print("A human dropped a loaf of bread. Do you try to steal it?")
        print("[yes] [no]")
        command = input()
        if command == "yes":
            from random import randint
            if randint(1, 2) == 1:
                print("You successfully steal the bread! Gain 3 food.")
                return 3
            else:
                print("You got caught! Lose 1 food.")
                return -1
        elif command == "no":
            print("You decided to stay safe. No food gained.")
            return 0
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")

def event3():
    while True:
        print("You encounter a wandering trader who offers food in exchange for help.")
        print("Do you help the trader? [yes] [no]")
        command = input()
        if command == "yes":
            print("The trader is grateful and gives you 1 food.")
            return 1
        elif command == "no":
            print("You ignore the trader and move on. No food gained.")
            return 0
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")

def event4():
    while True:
        print("You find a sparkling river. The water looks drinkable but might be poisoned.")
        print("Do you drink from the river? [yes] [no]")
        command = input()
        if command == "yes":
            from random import randint
            if randint(1, 2) == 1:
                print("You feel refreshed! Gain 1 food.")
                return 1
            else:
                print("The water was poisoned! Lose 1 food.")
                return -1
        elif command == "no":
            print("You decide not to risk it and move on.")
            return 0
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")

def event5():
    while True:
        print("You find an old, rusty rabbit trap with a caught rabbit inside.")
        print("Do you take the rabbit? [yes] [no]")
        command = input()
        if command == "yes":
            print("You carefully take the rabbit. Gain 2 food.")
            return 2
        elif command == "no":
            print("You leave the rabbit trap alone. No food gained.")
            return 0
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")

def event6():
    while True:
        print("You find a bush full of strange-looking berries. They could be edible or toxic.")
        print("Do you eat the berries? [yes] [no]")
        command = input()
        if command == "yes":
            from random import randint
            outcome = randint(1, 3)
            if outcome == 1:
                print("The berries are delicious! Gain 3 food.")
                return 3
            elif outcome == 2:
                print("The berries are bitter but edible. Gain 1 food.")
                return 1
            else:
                print("The berries are poisonous! Lose 2 food.")
                return -2
        elif command == "no":
            print("You decide not to eat the berries. No food gained.")
            return 0
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")

def event7():
    while True:
        print("A human merchant offers you food in exchange for a shiny pebble.")
        print("Do you trade? [yes] [no]")
        command = input()
        if command == "yes":
            print("The merchant gives you 2 food for the pebble.")
            return 2
        elif command == "no":
            print("The merchant shrugs and moves on. No food gained.")
            return 0
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")

def event8():
    while True:
        print("A wild cat appears, guarding some scraps of food.")
        print("Do you try to scare the cat away? [yes] [no]")
        command = input()
        if command == "yes":
            from random import randint
            if randint(1, 2) == 1:
                print("You scare the cat away and take the food. Gain 2 food.")
                return 2
            else:
                print("The cat scratches you! Lose 1 food.")
                return -1
        elif command == "no":
            print("You decide to leave the cat alone. No food gained.")
            return 0
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")

def event9():
    print("A sudden storm catches you off guard. You find shelter, but it costs you time and energy.")
    print("Lose 1 food.")
    return -1

def event10():
    while True:
        print("You stumble upon the remains of a human feast.")
        print("Do you scavenge for leftovers? [yes] [no]")
        command = input()
        if command == "yes":
            print("You find some scraps. Gain 3 food.")
            return 3
        elif command == "no":
            print("You decide it's too risky to stay near humans. No food gained.")
            return 0
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")

def event11():
    while True:
        print("You come across a campfire with a pot of soup cooking. No one seems to be around.")
        print("Do you take some soup? [yes] [no]")
        command = input()
        if command == "yes":
            from random import randint
            if randint(1, 2) == 1:
                print("You enjoy a warm meal! Gain 3 food.")
                return 3
            else:
                print("The owner returns and catches you! Lose 2 food.")
                return -2
        elif command == "no":
            print("You decide not to take the risk. No food gained.")
            return 0
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")

def event12():
    while True:
        print("You discover an abandoned beehive with some honeycomb left inside.")
        print("Do you try to gather the honey? [yes] [no]")
        command = input()
        if command == "yes":
            from random import randint
            if randint(1, 2) == 1:
                print("You gather the honey safely. Gain 2 food.")
                return 2
            else:
                print("The bees sting you! Lose 1 food.")
                return -1
        elif command == "no":
            print("You leave the beehive untouched. No food gained.")
            return 0
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")
