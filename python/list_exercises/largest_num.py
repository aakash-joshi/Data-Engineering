# Write a Python program to get the largest number from a list.
def largest_number(items):
    number = items[0]

    for i in items:
        if i > number:
            number = i
    return number

print(largest_number([1, 3, 5, 7, 9]))