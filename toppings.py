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
