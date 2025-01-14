from TAG import *

separator = "******************************************************************"
hours = 6
food = 3
day = 0
events = [event1(), event2(), event3(), event4(), event5(), event6(), event7(), event8(), event9(), event10()]

def intro():
    hours = 6
    food = 3
    print("you are a little goblin named kobok,")
    print("you are trying to make a living in a town full a human")
    print("times are harsh but you make with what you have")
    print("as a good little goblin, you wake up at 10AM and go to sleep at 12AM")
    print("try to eat enough to survive the night !")
    print("you need at least 3 food to survive the night")

def exitgame():
    print(separator)
    print("see you next time")
    quit()

def givetime():
    print(separator)
    if (hours + 10) < 13:
        print("it's " + str(hours) + " AM")
    else:
        print("it's " + str(hours) + " PM")

def givefood():
    print(food)