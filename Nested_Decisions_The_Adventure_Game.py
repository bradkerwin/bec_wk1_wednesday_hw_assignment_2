# Task 1: Code Correction
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == ("cross a river"):
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

# Task 2: Setting the Scene
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == ("cross a river"):
        print("You found a boat!")
elif place == "cave":
    new_action = input("Do you want to light a torch or proceed in the dark?")
    if new_action == "light a torch":
        print("Let there be light!")
    else:
        print("We're walking through the dark")

# Task 3: Default Path
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == ("cross a river"):
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    new_action = input("Do you want to light a torch or proceed in the dark?")
    if new_action == "light a torch":
        print("Let there be light!")
    elif new_action == ("proceed in the dark"):
        print("We're walking through the dark")
    else:
        pass
else:
    pass