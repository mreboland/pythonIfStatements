cars = ['audi', 'bmw', 'subaru', 'toyota']

# Loop through list
for car in cars:
    # Checking to see if bmw has come up through loop
    # Keep in mind that true false tests are case sensitive so you may need to alther the data (i.e using .lower()) so data can be compared properly.
    # Using below if it was "BMw" we could use car.lower() == "bmw" to do the check without altering the original list or variable (if its being used).
    if car == "bmw":
        # If so, print the name in caps
        print(car.upper())
    else:
        # otherwise use title case
        print(car.title())
        

        
