"""2. Write a Python program to count the number of even and odd 
numbers from a series of numbers. 
Sample numbers :  numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) """

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = 0
odd = 0
for i in numbers:
    if i % 2 == 0:
        even = even + 1
    else:
        odd += 1
print(f"Total even numbers: {even}")
print(f"total odd numbers: {odd}")