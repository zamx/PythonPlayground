import sys

def is_even(number):
    return number % 2 ==0

def highest_even(list):
    current_max = -sys.maxsize
    for number in list:
        if is_even(number):
            current_max = max(number, current_max)
    
    if current_max == -sys.maxsize:
        return None

    return current_max

print(highest_even([10, 5, 11, 6]))
print(highest_even([]))
print(highest_even([13, 5, 11, 9]))