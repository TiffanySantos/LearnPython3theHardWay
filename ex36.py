import random

def start():
    name = str(input("What's your name?: "))
    print("Hello " + name)
    print("Welcome to the Rainbow Runner!")
    print("This is a Crystal Maze style game.")
    print("\nYour objective is to earn a gem in each room.")
    print("Each coloured room will have a task, solving each task correctly will get you a gem.")
    print("Incorrect answers or bad decisions will result in no gem.")
    print("\nYou will be moved on from room to room, unable to go back, so make your choices wisely.")
    print("Are you ready to be a Rainbow Runner today?! Great, let's begin in the Red Room:")


def gem_count(gem):
    print (f"Your gem count is {gem}") 


def red_room():
    print('''\nYou are in a red room,
            on the blood red table there are three glasses, 
            each containing a different coloured liquid. 
            In order to obtain your first gem you must drink the liquid 
            on the opposite side of the colour wheel as the room you're in.
    Which colour do you choose?
    a) bue
    b) yellow
    c) green''')
    
    answer = input("Letter: ")
    if answer == "c":
        print("Well done, you have earned your first gem!")
        return True 
    else:
        print("Sorry, you didn't get a gem this time.")
    return False

def orange_room():
    print("\nAn isogram is a word which does not repeat letters.")
    print("Which is the longest one in the English language?")
    print("You have five attempts to guess the word")
    print("hint: it contains the word copy, has a prefix and a suffix, and is an adjective.")
    word = "uncopyrightable"
    guess = " "
    guess_count = 0
    guess_limit = 5
    guess_max = False
    while guess != word and not guess_max:
        if guess_count < guess_limit:
            guess = input("Enter a guess: ")
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
    print("\nThis is the yellow room, in this room we have a little game of hangman for you to play.")
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
    print('''Welcome to to green room.
    Green day reminds us of our need to look after our planet, on which many aninals are endagered. 
    One such animal is the Tiger. 
    In this room you will complete a very famous poem by William Blake. 
    You'll earn yourself a green gem if you guess half or more correctly. 
    \n#save_the_tiger''')
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
        print("Sorry, not this time.")
        incorrect += 1
    if input("In the forests of the ") == noun1:
        print("correct") 
        correct += 1 
    else:
        print("Sorry, not this time.")
        incorrect += 1
    if input("What immortal hand or ") == noun2:
        print("correct")
        correct += 1 
    else:
        print("Sorry, not this time.")
        incorrect += 1
    if input("Could frame thy fearful ") == noun3: 
        print("correct")
        correct += 1 
    else:
        print("Sorry, not this time.")
        incorrect += 1
    if correct >= incorrect:
        return True


def blue_room():
    print("The blue room is under water.")
    print("In it you must guess a number from 1 - 10.")
    print("If you are correct within the try limit, you get a blue gem.")
    print("If you are not, you leave empty handed.")
    number = random.randint(1, 10)
    guess_count = 0
    while guess_count < 3:
        print("Guess a number:")
        guess = input()
        i = int(guess)
        guess_count +=1
        if i < number:
            print("Too low.")
        elif i > number:
            print("Too high.")
        else:
            break
    if guess_count is 0 and i != number:
        print("\nYou have no more guesses left, you don't get a gem.")
        return False
    else:
        print("\nWell done! You get a blue gem.")
        return True

#def indigo_room():

#indigo_room()


#def violet_room():

#violet_room()


#def rainbow_room():

#rainbow_room()

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

    gem = run_rooms([red_room, orange_room, yellow_room, green_room, blue_room])
    
    print("\nYou have been a fantastic Rainbow Runner, this is the end of the game!")
    

# terminal lets python know you're running directly.
if __name__ == "__main__":
    main()


