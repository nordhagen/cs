# Looping, remember the colon at the en of for look signature
# and the indentation
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
  print(magician.title() + ', that was a great trick')

# The range function produces a range object
r = range(1,5)

# It looks like a list when printed, but needs casting to be
# a true list
l = list(r)
print r
print l
for value in r:
    print value

# The range function has start, end and step size arguments
even_numbers = range(2, 11, 2)
print even_numbers

# Double asterisks (**) represent exponents
squares = []
for val in range(1, 11):
    squares.append(val**2)

print squares

# Min and max are global functions
digits = range(1, 11)
print digits
print min(digits)
print max(digits)

# List comprehensions. Looks like a combination of square bracket
# list initialization supporting arguments rather than only values
# and reverse syntactical order
sq = [value**2 for value in range(1,11)]
print sq

# Slicing lists has a really nice syntax:
print sq[4:6]
print sq[:6]
print sq[:4]
print [val for val in sq[2:4]]

# Copying a list is simple, just use the slice operator
# without indicies
sq2 = sq[:]
print sq
print sq2

# Tuples are immutable lists. They are made using parenthesis
# instead of square brackets. They have the same operations as
# lists, apart from the ones that make modifications.
hd = (1920, 1080)
print hd
print hd[1]

# A tuple cannot be changed but the variable holding it can be
# assigned a new, different tuple
hd = (1080, 720)
print hd