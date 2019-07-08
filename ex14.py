from sys import argv

script, user_name = argv
prompt = ' # ' # we make a variable promt that is set tot he prompt we wnat so that instead of typing the input over and over again we can just change it in one spot.

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like {user_name}")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print (f""" 
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer, nice!
""")