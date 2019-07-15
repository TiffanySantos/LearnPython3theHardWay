
the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes",3 ,"quarters"]
 
 # this is the first kind of for-loop that goes through the list
for number in the_count:
    print(f"This is count number {number}")

# same as above
for fruit in fruits:
    print(f"This type of fruit is: {fruit} ")

# we can alsogo through mixed lists 
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we cna also build lists, starting with an empty elemet
elements = []
# then use the range function to count 0 - 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list")
    # apppend is a function that lists understand
    elements.append(i)
    
# now we can print them out too
for i in elements:
    print(f"Element was: {i}")




