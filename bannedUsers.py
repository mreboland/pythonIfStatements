# Checking whether a value is not in a list
# Let's say we want to check a list of users who are banned from commenting in a forum. We want to check if the user trying to post, is banned or not.
# Instead of using "in" to see if the user is in the list we use "not in" to check that they are not, in fact, in the list.
bannedUsers = ['andrew', 'carolina', 'david']
user = "marie"

# Evaluates to true as marie is not in bannedUsers
if user not in bannedUsers:
    print(f"{user.title()}, you can post a response if you wish.")


# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# • Create at least ten tests. Have at least five tests evaluate to True and
# another five tests evaluate to False.

age = 20

print("Is age < 20, false")
print(age < 20)
print("Is age > 20, false")
print(age > 20)
print("Is age <= 20, true")
print(age <= 20)
print("Is age >= 20, true")
print(age >= 20)
print("Is age == 20, true")
print(age == 20)

# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to ten. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:
# • Tests for equality and inequality with strings
topping = "pineapple"

print(topping == "pineapple", "true")
print(topping != "cheese", "true")
print(topping != "pineapple", "false")
print(topping == "cheese", "false")

# • Tests using the lower() method
topping = "PinEaPplE"

print(topping == "pineapple", "false")
print(topping.lower() == "pineapple", "true")

# • Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to

# already done above

# • Tests using the and keyword and the or keyword

ageOne = 30
ageTwo = 25

if ageOne >= 30 and ageTwo <= 25:
    print("You meet the requirements")

if ageOne >= 30 or ageTwo < 18:
    print("You meet the requirements")

# • Test whether an item is in a list

ages = [18, 19, 20, 50, 60, 70]

if 18 in ages:
    print("You are old enough")
    
ageCheck = 55

if ageCheck in ages:
    print("This won't print")

# • Test whether an item is not in a list
if ageCheck not in ages:
    print("This will print")
