# Imports
""" Import the various modules for the game """
import time
from time import sleep
import sys
from colorama import init, Fore, Back

init()


delay = 0.5


def win():
    time.sleep(delay)
    print("Congratulations, you managed to survive the adventure!")


def kill():
    time.sleep(delay)
    print("Unfortunately you chose the wrong path!")
    time.sleep(delay)
    print("GAME OVER!")


