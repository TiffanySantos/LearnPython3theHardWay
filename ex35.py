import sys # import the library here

def gold_room():
    print("This room is full of gold. How much do you take?")
    
    while True:
        try:
            how_much = int(input("Enter an amount: "))
            break
        except ValueError: # letting the user know they messed up!
            print("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        sys.exit(0) # now it's clear where and when you're using it
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved form the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "open door":
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or stare back?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif choice == "stare back":
        print("You are driven to hallucination")
        print("...so much so that you imagine you are in a different room.")
        gold_room()
    else:
        print("I got no idea what that means.")

def dead(why):
    print(why, "\nThat's the end of the game!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around in the room until you starve!")

start()

        
