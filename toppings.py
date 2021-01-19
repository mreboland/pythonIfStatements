# To check for an inequality, we use ! =. The "!" stands for not, so not equal
requestedTopping = "mushrooms"

# The below reads, if the var requestedTopping does not equal anchovies, which is true, then execute the next line. reqTopping is not equal to anchovies, is true, execute code. 
if requestedTopping != "anchovies":
    print("Hold the anchovies!")
    
# Testing multiple conditions
# The issue with elif is that once a condition is true, nothing else is checked. If we need to check for multiple things we stack if statements so that we can act on every true condition

requestedTopping = ['mushrooms', 'extra cheese']

if "mushrooms" in requestedTopping:
    print("Adding mushrooms.")
if "pepperoni" in requestedTopping:
    print("Adding pepperoni")
if "extra cheese" in requestedTopping:
    print("Adding extra cheese")
    
print("\nFinished making your pizza!")

# If we had used the elif code block we wouldn't be able to act on each new topping as one true statement will break the chain

# mushrooms pass, however the extra cheese does not, so this code block doesn't work for our purposes.
if 'mushrooms' in requestedTopping:
    print("Adding mushrooms.")
elif 'pepperoni' in requestedTopping:
    print("Adding pepperoni.")
elif 'extra cheese' in requestedTopping:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
        
# In summary, if you want only one block of code to run, use an if-elifelse
# chain. If more than one block of code needs to run, use a series of
# independent if statements.

# 5-3. Alien Colors  # 1: Imagine an alien was just shot down in a game. Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

alienColour = "green"

# • Write an if statement to test whether the alien’s color is green. If it is , print
# a message that the player just earned 5 points.

if alienColour == "green":
    print("You just earned 5 points!")

# • Write one version of this program that passes the if test and another that
# fails. (The version that fails will have no output.)

if alienColour == "green":
    print("You just earned 5 points!")
if alienColour == "red":
    print("You just earned 10 points!")

# 5-4. Alien Colors  # 2: Choose a color for an alien as you did in Exercise 5-3, and
# write an if-else chain.
# • If the alien’s color is green, print a statement that the player just earned
# 5 points for shooting the alien.
# • If the alien’s color isn’t green, print a statement that the player just earned
# 10 points.
# • Write one version of this program that runs the if block and another that
# runs the else block.


if alienColour == "green":
    print("\nYou just earned 5 points!")
else:
    print("You just earned 10 points!")

alienColour = "red"

if alienColour == "green":
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")


# 5-5. Alien Colors  # 3: Turn your if-else chain from Exercise 5-4 into an if-elifelse
# chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed
# for the appropriate color alien.

alienColour = "green"

if alienColour == "green":
    print("\nYou just earned 5 points!")
elif alienColour == "yellow":
    print("You just earned 10 points!")
elif alienColour == "red":
    print("You just earned 15 points")
    
alienColour = "yellow"

if alienColour == "green":
    print("\nYou just earned 5 points!")
elif alienColour == "yellow":
    print("You just earned 10 points!")
elif alienColour == "red":
    print("You just earned 15 points")
    
alienColour = "red"

if alienColour == "green":
    print("\nYou just earned 5 points!")
elif alienColour == "yellow":
    print("You just earned 10 points!")
elif alienColour == "red":
    print("You just earned 15 points!")

# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
# stage of life. Set a value for the variable age, and then:
# • If the person is less than 2 years old, print a message that the person is
# a baby.
# • If the person is at least 2 years old but less than 4, print a message that
# the person is a toddler.
# • If the person is at least 4 years old but less than 13, print a message that
# the person is a kid.
# • If the person is at least 13 years old but less than 20, print a message that
# the person is a teenager.
# • If the person is at least 20 years old but less than 65, print a message that
# the person is an adult.
# • If the person is age 65 or older, print a message that the person is an
# elder.

age = 65

if age < 2:
    print("Get out of here baby!")
elif age >= 2 and age < 4:
    print("Ah! a toddler!")
elif age >= 4 and age < 13:
    print("You're a kid!")
elif age >= 13 and age < 20:
    print("You're a teenager")
elif age >= 20 and age < 65:
    print("adult")
elif age >= 65:
    print("elder")
    
# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
# independent if statements that check for certain fruits in your list.
# • Make a list of your three favorite fruits and call it favorite_fruits.
# • Write five if statements. Each should check whether a certain kind of fruit
# is in your list. If the fruit is in your list, the if block should print a statement,
# such as You really like bananas!

favouriteFruits = ["mango", "banana", "pineapple"]

if "mango" in favouriteFruits:
    print("Delicious!")
if "banana" in favouriteFruits:
    print("Delicious!")
if "pineapple" in favouriteFruits:
    print("Delicious!")
if "apple" in favouriteFruits:
    print("Delicious!")
if "pear" in favouriteFruits:
    print("Delicious!")
    
    
# Checking for special items
requestedToppings = ['mushrooms', 'green peppers', 'extra cheese']

# The below is a simple loop to print out the requested toppings
for requestedTopping in requestedToppings:
    print(f"Adding {requestedTopping}.")

print("\nFinished making your pizza!\n")

# What happens if we run out of green peppers?
for requestedTopping in requestedToppings:
    # Here we added a check to see if we had a topping before printed out that we are adding the topping.
    # Because we are out of green peppers, we print we don't have any.
    if requestedTopping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requestedTopping}.")

print("\nFinished making your pizza!")

# Checking that a list is not empty
requestedToppings = []

# Instead of jumping right into a for loop, we do a quick check below. If the list is empty the if requestedToppings will be false which will trigger the else block. If there was something in the list, it'd continue like normal.
if requestedToppings:
    for requestedTopping in requestedToppings:
        print(f"Adding {requestedTopping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza")

# Using multiple lists
# For this example we want to check each item in requestedToppings against the list of available toppings before it's added to the pizza.
availableToppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requestedToppings = ['mushrooms', 'french fries', 'extra cheese']

# We loop through the request toppings so we have access to each topping individually
for requestedTopping in requestedToppings:
    # We check if that individual topping is within the list of avail toppings
    if requestedTopping in availableToppings:
        # If it is, print the below
        print(f"Adding {requestedTopping}.")
    else:
        # If not, print below
        print(f"Sorry, we don't have {requestedTopping}.")
        
print("\nFinished making your pizza!")

# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user:

names = ["billy", "bob", "celine", "eddy", "john", "admin"]

# • If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Jaden, thank you for
# logging in again.

for name in names:
    if name == "admin":
        print(f"Hello {name.title()}, would you like to see a status report?")
    else:
        print(f"Hello {name.title()}, thank you for logging in again.")

# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct
# message is printed.

names = []

if names:
    for name in names:
        if name == "admin":
            print(f"Hello {name.title()}, would you like to see a status report?")
        else:
            print(f"Hello {name.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")



# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
# current_users containing the lowercase versions of all existing users.)

currentUsers = ["billy", "bob", "celine", "eddy", "john"]
newUsers = ["shane", "shawn", "Bob", "scooter", "Celine"]

for newUser in newUsers:
    if newUser.lower() in currentUsers:
        print("That username is already taken, please enter a new username")
    else:
        print("That user name is available")

# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
# as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# • Store the numbers 1 through 9 in a list.
# • Loop through the list.
# • Use an if-elif-else chain inside the loop to print the proper ordinal ending
# for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
# 7th 8th 9th", and each result should be on a separate line.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print("1st")
    if number == 2:
        print("2nd")
    if number == 3:
        print("3rd")
    if number == 4:
        print("4th")
    if number == 5:
        print("5th")
    if number == 6:
        print("6th")
    if number == 7:
        print("7th")
    if number == 8:
        print("8th")
    if number == 9:
        print("9th")