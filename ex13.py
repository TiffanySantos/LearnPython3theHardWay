from sys import argv
# this passes variables into a script. You must run it in the command line with a four variables
script, first, second, third = argv

print("The script is called: ", script)
print("your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ",third)

print("What's your favourite food? ", end=' ')
favouriteFood = input()
print(f"So you like {favouriteFood}, do you?")