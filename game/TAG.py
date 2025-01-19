def event1():
    print("You found a bush full of berries! Do you want to pick them?")
    print("[yes] [no]")
    command = input()
    if command == "yes":
        print("You pick the berries and gain 2 food.")
        return 2  # Gain 2 food
    else:
        print("You decided not to risk it. No food gained.")
        return 0  # No change

def event2():
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
    else:
        print("You decided to stay safe. No food gained.")
        return 0

def event3():
    print("You encounter a wandering trader who offers food in exchange for help.")
    print("Do you help the trader? [yes] [no]")
    command = input()
    if command == "yes":
        print("The trader is grateful and gives you 1 food.")
        return 1
    else:
        print("You ignore the trader and move on. No food gained.")
        return 0

def event4():
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
    else:
        print("You decide not to risk it and move on.")
        return 0

def event5():
    print("You find an old, rusty rabbit trap with a caught rabbit inside.")
    print("Do you take the rabbit? [yes] [no]")
    command = input()
    if command == "yes":
        print("You carefully take the rabbit. Gain 2 food.")
        return 2
    else:
        print("You leave the rabbit trap alone. No food gained.")
        return 0

def event6():
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
    else:
        print("You decide not to eat the berries. No food gained.")
        return 0

def event7():
    print("A human merchant offers you food in exchange for a shiny pebble.")
    print("Do you trade? [yes] [no]")
    command = input()
    if command == "yes":
        print("The merchant gives you 2 food for the pebble.")
        return 2
    else:
        print("The merchant shrugs and moves on. No food gained.")
        return 0

def event8():
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
    else:
        print("You decide to leave the cat alone. No food gained.")
        return 0

def event9():
    print("A sudden storm catches you off guard. You find shelter, but it costs you time and energy.")
    print("Lose 1 food.")
    return -1

def event10():
    print("You stumble upon the remains of a human feast.")
    print("Do you scavenge for leftovers? [yes] [no]")
    command = input()
    if command == "yes":
        print("You find some scraps. Gain 3 food.")
        return 3
    else:
        print("You decide it's too risky to stay near humans. No food gained.")
        return 0
