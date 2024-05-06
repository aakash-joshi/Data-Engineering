# Write a Python program to multiply all the items in a list.

def multiply_list(items):
    total = 1 

    for i in items:
        total *= i
    return total

print(multiply_list([2, 3, 3]))
