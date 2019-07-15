people = 20
cats = 30
dogs = 15

if people < cats:
    print("There are too many cats in the world.")

if people > cats:
    print("There aren't too many cats, the world is safe.")

if people < dogs:
    print("There are too many dogs.")

if people > dogs:
    print("Dogs are no longer a problem.")

dogs += 5

if people >= dogs:
    print("People are greater or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")