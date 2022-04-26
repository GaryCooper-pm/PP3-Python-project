"""
Imports the various modules for the game
"""
# Imports
import time
from time import sleep
import sys
from colorama import init, Fore, Back

init()

# Adventure introduction
intro = ["You have woken up in a village square",
         "The square has 3 visible exits",
         "North, East and West",
         "To the North lies a cobbled road leading out to open fields",
         "To the East you see a small wooden bridge crossing a river",
         "To the West there is a dirt path leading to an ancient wood"]

for line in intro:
    for c in line:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.125)
    print(Fore.GREEN + '' + Fore.RESET)
time.sleep(1)
