from helper_functions import clear_screen
clear_screen()

# =====================
# NESTED LOOPS PRACTICE
# =====================

# 1. PRACTICE: NESTED LOOPS WITH DICTIONARIES AND LISTS
# Given the schedule dictionary below:
# print out each day of the week, and then below each day,
# print each class that occurs on that day, tabbed out from the day of the week:

# E.g.:
# Monday:
#   Math
#   Science

# after each day's classes, print an extra blank line so it looks nicer.

# remember that with a dicitonary, you can get the keys and values by
# using dictionary_variable.items()

schedule = {
    "Monday": ["Math", "Science"],
    "Tuesday": ["English", "History", "Art"],
    "Wednesday": ["Math", "Science", "PE"],
    "Thursday": ["English", "Art"],
    "Friday": ["Math", "History", "Science", "PE"]
}