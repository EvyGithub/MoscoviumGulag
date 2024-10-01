from time import sleep
from random import choice, randint

# variables
location = "gulag"

def update(newLocation: str) -> None:
    global location
    location = newLocation

def choice(options: list[str], prompt) -> str:
    # repeadtely ask user for an option, returns what they typed
    temp = "honestly this string is a very nice placeholder that I spent a long time writing for absolutely no reason at all" # lol idk I like to have fun with placeholder variables
    print(prompt)
    while temp not in validOptions:
        try:
            temp = input("> ").strip().lower()
        except EOFError:
            continue

    print("\n" * 69)

    return temp

def menu() -> None:
    temp = input("""
- Technetium Gulag -

/technetiumGulag/mainMenu

Please select a (VALID) option:
- 0: Quit game
- 1: New game
- 2: Load game
- 3: print 1 + 2""".strip())
    if temp == "0": exit()
    elif temp == "1": technetiumGulag()
    elif temp == "2": load() # after load run technetiumGulag()
    elif temp == "3": print(1 + 2); exit()
    else: exit()

def technetiumGulag() -> None:
    # controll of technetium Gulag
    global location
    match location:
        case "gulag": tcgGulag()

# LOCATIONs
def tcgGulag() -> None:
    update("gulag")
    print("You are in the Gulag.\nIt is currently 14:00.\nThe gulag leader has ordered you to mine some technetium (Tc).\n\nWhat do you do?\n1: Go mining for Tc\n2: Stay in bed\n")
    temp = choice(["1", "2"], "> ")
    if temp == "1": tcgTcMines()
    else: tcgGulag()

def tcgTcMines() -> None:
    update("tcmines")
    print("You are in the Tc mines. ")