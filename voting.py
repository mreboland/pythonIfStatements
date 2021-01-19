age = 19

if age >= 18:
    print("You are old enough to vote!")
    # If statements aren't limited to one line of code after the condition
    # Condition is true so both lines will be printed
    print("Have you registered to vote yet?")
    
# if-else statements
# When we want a condition to do something when it's true, however do something else if it's false, we use an if-else statementdatetime A combination of a date and a time. Attributes: ()
# Using the above example again:
age = 17

if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote")
    
# if-elif-else chain
# If we need to test multiple situations we use elif to do so.
# With elif, if one test passes the others are not tested. They are skipped.
# Example:
# Admission for anyone under age 4 is free.
# Admission for anyone between the ages of 4 and 18 is $25.
# Admission for anyone age 18 or older is $40.

age = 12

if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")
    
# We can expand on the above code block by instead of having print statements under each if block, we set the price to a variable in each conditional statement and have 1 print statement. 

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
    
# By setting the price in the brackets we can customize our message regardless of what price changes we make.
print(f"Your admission price is ${price}")

# We are not restricted to how many elif blocks we use
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
    
print(f"Your admission cost is ${price}.")

# The else block isn't required. Sometimes an else block is useful, othertimes it is clearer to use an additional elif statement that catches the condition of interest
# The advantage to not using the else is that it makes sure that your testing has to pass without a catch that the else would provide. It provides better testing conditions
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20