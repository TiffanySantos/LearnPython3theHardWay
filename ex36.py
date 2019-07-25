import random
import time

def start():
    name = str(input("What's your name?: "))
    print("Hello " + name)
    print("Welcome to the Rainbow Runner!")
    print("This is a Crystal Maze style game.")
    print("\nYour objective is to earn a gem in each room.")
    time.sleep(3)
    print("Each coloured room will have a task, solving each task correctly will get you a gem.")
    print("Incorrect answers or bad decisions will result in no gem.")
    time.sleep(5)
    print()
    print("You will be moved on from room to room, unable to go back, so make your choices wisely.")
    print("Are you ready to be a Rainbow Runner today?! Great, let's begin in the Red Room:")


def gem_count(gem):
    print (f"Your gem count is {gem}") 


def red_room():
    time.sleep(5)
    print()
    print("\nYou are in a red room, on the blood red table there are three glasses, each containing a different coloured liquid.") 
    print()       
    print("In order to obtain your first gem you must drink the liquid on the opposite side of the colour wheel as the room you're in.")
    print("Which colour do you choose?")
    print()
    print ("a) bue")
    print("b) yellow")
    print("c) green")
    
    answer = input("Letter: ")
    if answer == "c" or "green" or "c)green":
        print("Well done, you have earned your first gem!")
        return True 
    else:
        print("Sorry, you didn't get a gem this time.")
    return False

def orange_room():
    time.sleep(5)
    print()
    print("\nWelcome to the second room, the Orange room!")
    print("An isogram is a word which does not repeat letters.")
    print()
    print("Which is the longest one in the English language?")
    print()
    print("You have five attempts to guess the word")
    print("hint: it contains the word copy, has a prefix and a suffix, and is an adjective.")
    print("The word is FIFTEEN letters long!")
    time.sleep(1)
    word = "uncopyrightable"
    guess = " "
    guess_count = 0
    guess_limit = 5
    guess_max = False
    while guess != word and not guess_max:
        if guess_count < guess_limit:
            guess = input("\nEnter a guess: ")
            guess_count += 1
        else:
            guess_max = True
    if guess_max:
        print("\nYou have no more guesses left, you don't get a gem.")
        return False
    else:
        print("\nWell done! You get an orange gem.")
        return True

   
def yellow_room():
    time.sleep(5)
    print()
    print("\nThis is the Yellow room, in this room we have a little game of hangman for you to play.")
    word = "rainbow" # secret word
    display = [] # create an empty list
    used = [] # creating a list of used letters
    display.extend(word)# pass the chars from word into a list , "r", "a", etc.
    used.extend(word)# pass the chars from word into a list  of used letters, "r", "a", etc.
    for i in range (len(display)):
        display[i] = "_" # swaps out each letter for a dash
    print (' '.join(display)) # rejoins the split list to form a line of dashes 
    print() # prints the dashes
    #while loop to keep going until all dashed have been changed to letters or all wrong answers have been used
    count = 0
    wrong = 9
    while count < len(word) and wrong > 0:
        guess = input("Guess a letter: ")
        guess = guess.lower()
    # iterate guess though letters in word
        for i in range(len(word)):
            if word[i] == guess and guess in used:
                display[i] = guess
                count +=1
                used.remove(guess) #removes the used letter from the used letters list thereby NOT increasing the counter
                print("\nYou have guessed a correct letter.")
        if guess not in display:
            print("\nSorry, wrong guess. You've got", wrong, "guesses left.")
            wrong -= 1
        print (' '.join(display)) # print the new string with the guessed letters in it
        print()
    if count == len(word):
            print("Well done, you've got a yellow gem")
            return True
    else:
            print("Unfortunatly you didn't get a gem this time.")
            return False


def green_room():
    time.sleep(5)
    print()
    print('''\nWelcome to to Green room.
    Green day reminds us of our need to look after our planet, 
    on which many aninals are endagered. 
    One such animal is the Tiger.''')
    time.sleep(1)
    print()
    print("In this room you will complete a very famous poem by William Blake.")
    print("You'll earn yourself a green gem if you guess more than half correctly.")
    print()
    adj = "bright"
    noun1 = "night"
    noun2 = "eye"
    noun3 = "symetry"
    correct = 0
    incorrect = 0
    if input("Tyger Tyger burning ") == adj:
        print("correct") 
        correct += 1  
    else:
        print("incorrect")
        incorrect += 1
    if input("In the forests of the ") == noun1:
        print("correct") 
        correct += 1 
    else:
        print("incorrect")
        incorrect += 1
    if input("What immortal hand or ") == noun2:
        print("correct")
        correct += 1 
    else:
        print("incorrect")
        incorrect += 1
    if input("Could frame thy fearful ") == noun3: 
        print("correct")
        correct += 1 
    else:
        print("incorrect")
        incorrect += 1
    if correct > incorrect:
        return True


def blue_room():
    time.sleep(5)
    print()
    print("\nThe Blue room is under water.")
    print("In it you must guess a number from 1 - 10.")
    time.sleep(3)
    print("If you are correct within the try limit of 3, you get a blue gem.")
    print("If you are not, you leave empty handed.")
    time.sleep(1)
    number = random.randint(1, 10)
    guess_count = 0
    guess = int
    while guess_count < 3:   
        try:
            guess = int(input("Guess a number: "))
            i = int(guess)
        except ValueError:
            print("You MUST enter a number: sta")   
        else:
            if i < number:
                print("Too low.")
            elif i > number:
                print("Too high.")
        guess_count +=1
    if guess != number:
        print("\nYou have no more guesses left, you don't get a gem." )
        return False
    else:
        print("\nWell done! You get a blue gem."  )
        return True


def indigo_room():
    time.sleep(5)
    print()
    print("In you go into the Indigo room!")
    print("Where a riddle is waiting for you.")
    time.sleep(3)
    print()
    print("What 8 letter word can have a letter taken away and it still makes a word.")
    time.sleep(3)
    print("Take another letter away and it still makes a word.")
    time.sleep(3)
    print("Keep on doing that until you have one letter left.")
    print()
    print("What is the word?")
    time.sleep(2)
    print("You have three tries, so THINK before you type")
    print("hint: that 8 letter word starts with an 's' and ends in a 'g'")
    word = "starting"
    guess = " "
    guess_count = 0
    while guess_count < 3: 
        guess = input("Your guess: ")
        if guess != word:    
            print("Try again.")
            guess_count +=1       
        else:
            print("Good job! You get an indigo gem this time.")
            print("Starting")
            time.sleep(1)
            print("Staring")
            time.sleep(1)
            print("String")
            time.sleep(1)
            print("Sing")
            time.sleep(1)
            print("Sin")
            time.sleep(1)
            print("In")
            time.sleep(1)
            print("I")
            return True 
             

def violet_room():
    time.sleep(3)
    print()
    print("\nYou have made your way to the Violet room.")
    print("In this room you you find two doors, one to the left and the other to the right.")
    print("Which one do you take, left or right?")
    choice = input(">")
    if choice == "left":
        rainbow_room ()
    else:
        print("\nSo, you decided to go right...there are six doors in a row before you.")
        time.sleep(2)    
        print("Each of a different colour...red, orange, yellow, green, blue and indigo")  
        time.sleep(2)  
        print("They look familiar, don't they?")   
        time.sleep(2) 
        print("Which of them would you like to return to?") 
        room = input("\nType a colour: ")  
        if room == "red": 
            red_room() 
        elif room == "orange":
            orange_room()
        elif room == "yellow":
            yellow_room()
        elif room == "green":
            green_room()
        elif room == "blue":
            blue_room()
        elif room == "indigo":
            indigo_room()
        else:
            violet_room ()


def rainbow_room():
    print()
    print()
    print("Congratulations on reaching the Rainbow room at last!")
    print("You have been a fantastic Rainbow Runner, you may take your gems with you and the small pot of gold, this is the end of the game!")
    return True
# counting gems function. each room returns a bool to this function. 
def run_rooms(rooms):
    gem = 0
    for room in rooms:
#each room returns a bool to this variable 
        success = room()
# the bools that return a true get assigned the variable success
        if success:
#the variable value acts on the if loop to add one for each true
            gem +=1
        gem_count(gem)
# this returns gem total to function in main
    return gem

#function main, top level stuff goes here
def main():
    start()
    gem = run_rooms([red_room, orange_room, yellow_room, green_room, blue_room, indigo_room, violet_room, rainbow_room])
    
# terminal lets python know you're running directly.
if __name__ == "__main__":
    main()


