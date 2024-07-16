from functools import reduce

# Using map to double each number
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]

# Using filter to keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4]

# Using reduce to sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 15