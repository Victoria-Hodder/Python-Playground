import random
import time

def wrong_input(valid):
    print(f"Sorry but the only valid options are: {valid}. You cannot play if you do not follow the rules!!!")

def dead(means_of_death):
    print(f"Oops you died of {means_of_death}. Hope you had a nice life!")

    print("You are falling for...")
    for i in range(11):
        print(i)
        time.sleep(0.3)
    
    print("...meters")
    print("The game is finished")

friends = ["Frieda", "Nannie", "Michael", "Alan"]
door_greetings = {"1": "Welcome to the coffin room", "2": "Welcome to the treasure house", "3": "Welcome to the fun place!"}

print("Welcome to the dungeon!")
print("What is your name?")

name = input("> ")

print(f"Do you go through door 1, door 2 or door 3, {name}?")

door = input("> ")

if door == "1":
    print(f"{door_greetings[door]}") 
    print("There is a nice vampire asking you if you enjoy life.")
    print("What do you do?")
    print("1. Smile and nod")
    print("2. Scream and run")

    vampire = input("> ")

    if vampire == "1":
        print(f"Congratulations {name}, you found a new friend!")
        print("What is your favorite color?")
        favorite_color = input("> ")
        print(f"Amazing {name}, {favorite_color} is my best color too!")

    elif vampire == "2":
        print(f"Oh no {name}! The vampire is faster than you")
        dead("vampire bite")
    else:
        wrong_input("1, 2")

elif door == "2":
    print(f"{door_greetings[door]}") 
    print("On the table, there is a golden chalice with a red liquid inside")

    print("What do you do?")
    print("1. Drink it")
    print("2. Throw it on the floor")

    chalice = input("> ")

    if chalice == "1":
        dead("poison")    
    elif chalice == "2":
        print("Excellent idea, you have avoided death")
    else:
        wrong_input("1, 2")

elif door == "3":
    print(f"{door_greetings[door]}") 
    rand_int = random.randint(0,3)
    print(f"And look, your friend {friends[rand_int]} is here.")
    print("They want to rescue you from this place")

    print("Is that OK? Please answer Y or N")

    is_OK = input("> ")

    if is_OK == "Y":
        print("Supi! Let's go")
    elif is_OK == "N":
        print("Too bad, you will die alone")
        dead("loneliness")
    else:
        wrong_input("Y, N")

else:
    wrong_input("1, 2, 3")

print()
bye = input("Say 'Good bye' in a language other than English: ")
print(f"{bye}, {name}!")