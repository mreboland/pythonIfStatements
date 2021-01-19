#Testing numbers

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")
    
# We can use any comparisions in our conditional statements as needed
if answer < 42:
    print("That is not the correct answer. Please try again!")

# Checking multiple conditions
# On occasion you may need two conditions to be true in order to execute a block of code. Key words "and" and "or" facilitate that
age0 = 22
age1 = 18

# The below won't print because age1 is set to 18 which is less than the condition set of 21 or greater
if age0 >= 21 and age1 >= 21:
    print("You are of age!")
    
# If we update age1 to 22 it'll work
age0 = 22
age1 = 22

# You can use parenthesis to make the code more readable, though it's not necessary
if (age0 >= 21) and (age1 >= 21):
    print("You are of age!")
    
# Using "and" requires both statements to be true. If we only need one of the checks to be true we use "or".
age0 = 22
age1 = 18

if age0 >= 21 or age1>= 21:
    print("This is true, because one of the checks is true")
    # If we were to change age0 to 18, the print statement wouldn't run as both statements would be false.
    
# Checking whether a value is in a list
# When we want to check to see if a list contains a certain value before taking action, we use the keyword "in".
requestedToppings = ['mushrooms', 'onions', 'pineapple']

if "mushrooms" in requestedToppings:
    print("It is!")

if "pepperoni" in requestedToppings:
    print("This won't print!")


