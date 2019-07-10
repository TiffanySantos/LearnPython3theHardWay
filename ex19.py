#def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #print(f"You have {cheese_count} cheeses!")
    #print(f"You have {boxes_of_crackers} boxes of crackers!")
    #print("Man that's enough for a party!")
    #print("Get a blanket.\n")
## the above def and the below print are connected. Line 1 defines the function, line 7 passes in values
#print("We can just give the functions numbers directly:")
#cheese_and_crackers(20, 30)
#
##these are vars with values
#print("OR, we can use variables form  our script:")
#amount_of_cheese = 10
#amount_of_crackers = 50
#
#cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#
##operators in use
#print("We can even do math inside too:")
#cheese_and_crackers(10 + 20, 5 * 6)
## vars with operators
#print("And we can combine the two variables and do math.")
#cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# 1st method, passes values into arguments
def outgoings(bills, rent):
    print(f"Bills: {bills}")
    print(f"Rent: {rent}")
#call the function
outgoings(50 , 250)


# 2nd method, assigns a value to the arguments
bills = 51
rent = 251
#call the function
outgoings(bills, rent)


# 3rd method, uses an operator within the argument
bills = (50 + 2)
rent = (250 + 25)
outgoings(bills, rent)


# 4th method, like CSS uses the last var in sight with the new operator
outgoings (bills + 50, rent + 50)


# 5th method, add the two variables together, first delare the int so that the two ints can be added
bills = 20
rent = 300
this_month = (bills + rent)   
print(f"Outgoings this month were €{this_month}")


# 6th method, takes user input and prints it out in a string
print("How much did you spend on bills this month? ") 
bills = input()
print("How much did you spend on rent this month? ") 
rent = input()
print(f" So your spend on bills this month was {bills} and your spend on rent was {rent}.")


# 7th method, takes user input (with cleaner code) and adds it for the user
bills = int(input("Bills: "))
rent = int(input("Rent: "))
total_spend = (bills + rent)
print(f"Your total spend this month was €{total_spend}")
# oh dear! this just put my two valuesnext to each other!!! input() and input () side by side
# solution = int(input()), now working correctly. As expected, inputting a string breaks it


# 8th method credit for the idea to www.josharcher.uk, try a function into a function
def daily_life_spend(): 
    food = int(input("Food: "))
    drink = int(input("Drink: "))
    return food + drink
daily_spend = daily_life_spend()
print(f" Your total daily spend was €{daily_spend}")

# 9th method, adding the two dinctions together as ints with an operation
print("Now let's see how much you've spent this month then:")
monthly_total = this_month + (daily_spend * 30)
print(f"In total across a 30 day month you spent €{monthly_total}")

#Oh my! I've learnt loads with this one!!! Looks like a return statement will allow me to re-use the variables. 

