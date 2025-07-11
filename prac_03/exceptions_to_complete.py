"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task.
This program keeps asking the user for a valid integer
until the input is correct.
"""
"""
set is_finished = false
while not is_finished
    try
        get result as integer
        set is_finished = true
    catch value error
        print "Please enter a valid integer."

print "Valid result is:", result

"""


is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
