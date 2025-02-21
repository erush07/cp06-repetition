import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# =========
# ENUMERATE
# =========

'''
OVERVIEW
--------
Sometimes you might want to loop through something like a list, and also have
access to the index of the element in the list. Or, list out then number of
the thing in the list. enumerate() is a function that makes that easy to do
with for loops.

EXAMPLE
-------  
iterable_variable = ["example_1", "example_2", "example_3"]

for index, looping_variable in enumerate(iterable_variable):
    print(index, looping_variable)

'''

example_list = ["Harry", "Hermione", "Ronald", "Luna"]

# 1. SHOW ELEMENTS AND THEIR INDEX TOGETHER
# Use a for loop, along with enumerate to print out the index of each
# element in the list, along with the element itself

for index, name in enumerate(example_list):
    print(f"{index}: {name}")


# 2. SHOW ELEMENTS WITH A DIFFERENT STARTING NUMBER
# Use a for loop, along with enumerate to print out the index of each
# element in the list, along with the element itself, but this time, change
# the starting number in enumerate(start=1) to start counting at 1 instead of 0.

print() # just to add an extra space
for starting_num, name in enumerate(example_list, start=1):
    print(f"{starting_num}: {name}")
