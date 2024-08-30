
    # '=' operator used for assignment not comparing, for comparing must be used '=='
    # error in 'else'  it doesn't take condition must be used 'elif' instead
place = input ("choose a place: forest or cave? ")
if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("Invalid action.")
elif place == "cave":
    print("You find a hidden treasure!")
else:
    print("Invalid place.")

    place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("Invalid action.")
elif place == "cave":
    sub_action = input("light a torch or proceed in the dark? ")
    if sub_action == "light a torch":
        print("You see a hidden passage and find a treasure chest!")
    elif sub_action == "proceed in the dark":
        print("You stumble upon a sleeping dragon and narrowly escape!")
    else:
        print("Invalid action.")
else:
    print("Invalid place.")


    # code gives you found hidden treasure
    # lighting a torch gives back this:-"You see a hidden passage and find a treasure chest!
    #for proceed in the dark code comes back withcave:-You stumble upon a sleeping dragon and narrowly escape
    
    place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("Invalid action.")
        pass  # Placeholder for handling invalid actions in the forest
elif place == "cave":
    sub_action = input("light a torch or proceed in the dark? ")
    if sub_action == "light a torch":
        print("You see a hidden passage and find a treasure chest!")
    elif sub_action == "proceed in the dark":
        print("You stumble upon a sleeping dragon and narrowly escape!")
    else:
        print("Invalid action.")
        pass  # Placeholder for handling invalid actions in the cave
else:
    print("Invalid place.")
    pass  # Placeholder for handling invalid places

#added 'pass' after printing "invalid action" in the forest branch
#added 'pass' in the cave branch after invalid action print






