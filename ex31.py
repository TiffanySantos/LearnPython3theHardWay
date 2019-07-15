print (''' You enter a dark room with two doors.
Do you go through door #1, door #2 or door #3?''')

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?\n 1. Take the cake. \n 2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off, now you can't see!")
    elif bear == "2":
        print("The bear eats your legs off, now you can't walk!")
    else:
        print("Well, doing {bear} is probably a good choice, the bear might walk away.")

elif door == "2":
    print("You stare into the distance at the endless abyss.")    
    print ("Directly in front of you there is a table with three bowls.")
    print(" 1. Peaches")
    print(" 2. Pears")
    print(" 3. Strawberries")
    print(" Which do you choose, 1, 2 or 3?")
    

    food = input ("> ")

    if food == "1" or "2":
        print("Oh no, P is for poison, you start hallucinating and vomiting. Not the best choice to make! ")
    else:
        print("Good choice, strawberries are full of Vit C and antioxidants. You power up your health status!")

else: #This prevuoisly unnused result is now in use, it is door #3
    print ("You trip on a knife an accidentally stab yourself to death!")


