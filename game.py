# Imports
""" Import the various modules for the game """
import os
import time
from time import sleep
import sys
from colorama import init, Fore, Back

init()


COLORS = {
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "white": "\u001b[37m",
}


def colorText(text):
    """Defines changing the text color"""
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text


# Printing out the ASCII file
f = open("virtual_house.txt", "r")
ascii = "".join(f.readlines())
print(colorText(ascii))
time.sleep(3.0)
os.system('clear')


def win():
    """Defines the winning message of the game"""
    time.sleep(1.0)
    print(
        Fore.GREEN
        + "Congratulations, "
        + name
        + " you managed to reach the safe room and",
        "survive the Virtual House!" + Fore.RESET
        )


def kill():
    """Defines the losing message of the game"""
    time.sleep(1.0)
    print(
        Fore.RED
        + "Unfortunately "
        + name
        + " you chose the wrong door!"
    )
    time.sleep(1.0)
    print("GAME OVER!" + Fore.RESET)


def bathroom():
    """Defines the bathroom"""
    f = open("bathroom.txt", "r")
    ascii = "".join(f.readlines())
    print(colorText(ascii))
    time.sleep(3.0)
    room_builder([True, False], "the bathroom", True, ["win", "kill"])


def nook():
    """Defines the nook"""
    f = open("nook.txt", "r")
    ascii = "".join(f.readlines())
    print(colorText(ascii))
    time.sleep(3.0)
    room_builder([False, True], "the nook", True, ["kill", "win"])


def dining_room():
    """Defines the dining_room"""
    f = open("dining_room.txt", "r")
    ascii = "".join(f.readlines())
    print(colorText(ascii))
    time.sleep(3.0)
    room_builder([False, True], "the dining room", True, ["kill", "win"])


def kitchen():
    """Defines the kitchen"""
    f = open("kitchen.txt", "r")
    ascii = "".join(f.readlines())
    print(colorText(ascii))
    time.sleep(3.0)
    room_builder([False, True], "the kitchen", False, ["kill", "dining_room"])


def bedroom():
    """Defines the bedroom"""
    f = open("bedroom.txt", "r")
    ascii = "".join(f.readlines())
    print(colorText(ascii))
    time.sleep(3.0)
    room_builder([True, False], "the bedroom", False, ["bathroom", "kill"])


def office():
    """Defines the office"""
    room_builder([False, True], "the office", False, ["kill", "nook"])


# Prints a little house
print("       `'::::. ")
time.sleep(1.0)
print("         _____A_ ")
time.sleep(1.0)
print("        /       /\ ")
time.sleep(1.0)
print("     __/___/\__/  \___")
time.sleep(1.0)
print("---/___|'  '' '| /___/\----")
time.sleep(1.0)
print("   |' '|'' ||''| |' '|| ")
time.sleep(1.0)
print(Back.GREEN + "   `' '`'' ))''`'`''''`  \n" + Back.RESET)
time.sleep(2.0)


# Request Player to enter a name
name = input(Back.MAGENTA + "Please type your name: \n" + Back.RESET).upper()
time.sleep(2.0)

# Welcome player to the adventure
print()
print(Fore.GREEN + "Welcome" + Fore.RESET, name, Fore.GREEN + "!")
time.sleep(1.0)
print("Your adventure is about to begin!\n" + Fore.RESET)
time.sleep(2.0)
os.system('clear')


# Adventure introduction
intro = [
    "You have woken up in a strange virtual house.\n"
    "Your challenge is to make it to the safe room.\n",
]


def typewriter_text(self):
    """Types text out like a typewriter"""
    for line in intro:
        for character in line:
            print(character, end="")
            sys.stdout.flush()
            sleep(0.105)
        print(Fore.GREEN + "" + Fore.RESET)
    time.sleep(1.0)


typewriter_text(intro)


# ([list of doors(T/F)], The Room Name, last room (T,F), [list of next room])


def room_builder(room_list, room_name, is_end_room, next_rooms):
    """Defines the room builder"""
    print(f"You find yourself in {room_name}.")
    time.sleep(1.0)
    room_count = len(room_list)
    choices = []

    # Dynamically build an input message based on my number of doors
    input_message = "Please choose a door to enter: ("

    # Add each ddoor name to the list and to a message |
    # exp (door 1, door 2, door 3)
    door_message = ""
    for count in range(room_count):
        choices.append(f"door {count + 1}")
        if count + 1 < room_count:
            door_message += f"door {count + 1}, "
        else:
            door_message += f"door {count + 1}): "
    # Add the door message onto the back of the input message
    input_message += door_message
    time.sleep(1.0)

    while True:
        command = input(input_message).lower()

        if command in choices:
            if room_list[choices.index(command)]:
                if is_end_room:
                    time.sleep(1.0)
                    print("Congratulations, you have chosen wisely!")
                    win()
                    break
                else:
                    time.sleep(1.0)
                    print(
                        Fore.BLUE
                        + "You travel to the next room."
                        + Fore.RESET
                        )
                    time.sleep(1.0)
                    os.system('clear')
                    eval(next_rooms[choices.index(command)] + "()")
                    break
            else:
                kill()
                break
        else:
            time.sleep(1.0)
            print(f"Sorry, you must enter a valid response ({door_message}")


room_builder(
    [True, True, True],
    "the entrance hall",
    False,
    ["kitchen", "bedroom", "office"],
)