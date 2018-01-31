bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print bicycles

# Python has string operation functions like .title() for title casing.
print bicycles[0].title()

# Negative array access will count from the end
print bicycles[-1]

message = 'My first bicycle was a '+ bicycles[0].title() + '.'
print message

motorcycles = ['honda', 'yamaha', 'suzuki']
print motorcycles

# Array elements can be edited in place, just like JS
motorcycles[0] = 'ducati'
print motorcycles

# append() is like push() in JS
motorcycles.append('honda')
print motorcycles

# Unlike JS, Python has an dedicated insert method
motorcycles.insert(1, 'bmw')
print motorcycles

# Deleting items in an array uses the del keyword
del motorcycles[2]
print motorcycles

# pop() just like JS
print motorcycles.pop()
print motorcycles

# Almost, in Python you can pop at any index
print motorcycles.pop(1)
print motorcycles

# Remove by value (stops searching after first match)
motorcycles.remove('ducati')
print motorcycles

cars = ['bmw', 'audi', 'toyota', 'subaru']

# Sorting in-place
cars.sort()
print cars

# Sorting in reverse order
cars.sort(reverse=True)
print cars

# Use sorted() to return a copy instead of sorting in-place like sort()
print sorted(cars)

# Reversing
print cars
cars.reverse()
print cars

# Counting array length
print str(len(cars)) + ' cars in list'