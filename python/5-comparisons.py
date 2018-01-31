# Capitalization matters in equality testing. This prints False:
print 'Audi' == 'audi'

# This prints True
print 'Audi'.lower() == 'audi'

# Multiple contitions are chained with and/or
print 36 == 37 and 36 == 36
print 36 == 37 or 36 == 36

# Checking for value in list
my_age = 36
print my_age in range(30,40)

# Checking for value not in list
print my_age not in range(20,30)

# If statements also use the colon. Remember it:
if my_age < 30:
    print 'A few more years to go'
# elif is a funny word
elif my_age > 40:
    print 'You had your fun'
else:
    print 'You are in yor best age'
