# This is not a program as such, it is a Boolean truth tables test
# correct_guess = lower_case, incorrect_guess = UPPER_CASE
True and True # true
False and True # false
1 == 1 and 2 == 1 # false
"test" == "test" # true
1 == 1 or 2 != 1 # true
True and 1 == 1 # true
False and 0 != 0 # false
True or 1 == 1 # true
"test" == "testing" # false
1 != 0 and 2 == 1 # false
"test" != "testing" # true
"test" == 1 # false
not (True and False) # true
not (1 ==1 and 0 != 1) # FALSE
not (10 == 1 or 1000 == 1000) # FALSE
not (1 != 10 or 3 == 4) # false
not ("testing" == "testing" and "Zed" == "Cool Guy") # TRUE
1 == 1 and (not ("Testing" == 1 or 1 == 0)) # true
"chunky" == "bacon" and (not (3 == 4 or 3 == 3)) # false
3 == 3 and (not("testing" == "testing" or "Python" == "Fun")) # FALSE


# Clearly must revise not and/or on the truth tables again!!!