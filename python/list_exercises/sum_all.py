# Write a  Python program to sum all the items in a list.

def sum_list(items):
    sum = 0

    for i in items:
        sum += i
    return sum

print(sum_list([1, 2, 3, 4, 5]))