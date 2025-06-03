"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?

A ValueError occurs when the user enters something that cannot be converted to an integer.
For example, entering a non-numeric string like "abc" will cause int("abc") to raise a ValueError.


2. When will a ZeroDivisionError occur?

A ZeroDivisionError happens when the user attempts to divide by zero.
This occurs if the denominator entered is 0, since dividing by zero is not allowed in mathematics or Python.


3. Could you change the code to avoid the possibility of a ZeroDivisionError?

Yes. To avoid a ZeroDivisionError, we can add an if statement to check whether the denominator is zero
before performing the division. If it is zero, we can display a message instead of trying to divide.

"""
"""
define zero = 0

try
    get numerator as integer
    get denominator as integer

    if denominator == zero
        print "Cannot divide by zero!"
    else
        set fraction = numerator / denominator
        print fraction

catch value error
    print "Numerator and denominator must be valid numbers!"

print "Finished."

"""


# Constants
ZERO = 0

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == ZERO:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
