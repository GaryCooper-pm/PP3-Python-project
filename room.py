# Imports
""" Import the various modules for the game """
import time
from time import sleep
import sys
from colorama import init, Fore, Back

init()


delay = 1


def win():
    time.sleep(delay)
    print("Congratulations, you managed to survive the adventure!")


def kill():
    time.sleep(delay)
    print("Unfortunately " + Fore.GREEN + name + Fore.RESET
        + " you chose the wrong path!")
    time.sleep(delay)
    print("GAME OVER!")


def ancient_wood():
    location_builder([True, True]
                    , "in some ancient woods", True, ["win", "kill"])


def open_fields():
    location_builder([True, True]
                    , "in open fields filled with bright yellow flowers."
                    " The cobbled road splits,"
                    " hills to the North and an ancient wood to the West"
                    , False, ["win", "kill"])


def wooden_bridge():
    location_builder([True, True]
                    , "at a wooden bridge that crosses over a fast flowing river.",
                    True, ["win", "kill"])


# Adventure introduction
intro = ["You have woken up in a village square",
         "The square has 3 visible exits",
         "North, East and West",
         "To the West there is a dirt path leading to an ancient wood",
         "To the North lies a cobbled road leading out to open fields",
         "To the East you see a small wooden bridge crossing a river\n",
         "Your controls for this adventure are:",
         "direction 1 = West",
         "direction 2 = North",
         "direction 3 = East"]


def typewriter_text(typet):
    """Types text out like a typewriter"""
    for line in intro:
        for character in line:
            print(character, end='')
            sys.stdout.flush()
            sleep(0.105)
        print(Fore.GREEN + '' + Fore.RESET)
    time.sleep(delay)


typewriter_text(intro)

# Request Player to enter a name
name = input(Back.MAGENTA + "Please type your name: \n" + Back.RESET
).upper()
time.sleep(delay)

# Welcome player to the adventure
print(Fore.GREEN + "Welcome" + Fore.RESET, name, Fore.GREEN + "!")
time.sleep(delay)
print("Your adventure is about to begin!\n\n" + Fore.RESET)
time.sleep(delay)

# ([list of directions(T/F)], The Location Name, last location (T,F), [list of
# next locations])


def location_builder(location_list, location_name, is_end_location, next_location):
    print(f"You find yourself {location_name}.")
    time.sleep(delay)
    location_count = len(location_list)
    choices = []

# Dynamically build an input message based on my number of directions
    input_message = "Please choose a direction to travel: ("

# Add each direction name to the list and to a message |
# exp (direction 1(west), direction 2(north), direction 3(east))
    direction_message = ""
    for count in range(location_count):
        choices.append(f"direction {count + 1}")
        if count + 1 < location_count:
            direction_message += f"direction {count + 1}, "
        else:
            direction_message += f"direction {count + 1}): "
# Add the direction message onto the back of the input message
    input_message += direction_message
    time.sleep(delay)

    while True:
        command = input(input_message).lower()

        if command in choices:
            if location_list[choices.index(command)]:
                if is_end_location:
                    time.sleep(delay)
                    print("Congratulations, you have chosen wisely!")
                    win()
                    break
                else:
                    time.sleep(delay)
                    print("You travel to the next location.")
                    time.sleep(delay)
                    eval(next_location[choices.index(command)] + "()")
                    break
            else:
                kill()
                break
        else:
            time.sleep(delay)
            print(f"Sorry, you must enter a valid ({direction_message}")


location_builder([True, True, True], "in the Village Square", False,
                ["ancient_wood", "open_fields", "wooden_bridge"])