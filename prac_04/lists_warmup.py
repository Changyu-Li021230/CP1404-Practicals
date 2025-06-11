
# Given list
numbers = [3, 1, 4, 1, 5, 9, 2]

# Expected answers to the questions:
# numbers[0] --> This is the first element of the list, and the value is 3.
# numbers[-1] --> This is the last element of the list, and the value is 2.
# numbers[3] --> This is the fourth element of the list, and the value is 1.
# numbers[:-1] --> This is all the elements of the list, except for the last one, the result is [3, 1, 4, 1, 5, 9]
# numbers[3:4] --> This is a subset of the fourth element of the list, and the result is [1]
# 5 in numbers --> Check whether 5 is in the list, and the result is True.
# 7 in numbers --> Check whether 7 is in the list, and the result is False.
# "3" in numbers --> Check whether the string "3" is in the list, and the result is False, because the number 3 is different from the string "3"
# numbers + [6, 5, 3] --> The splicing of the list, the results are [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Changing elements as instructed
numbers[0] = "ten"  # Change first element to "ten"
numbers[-1] = 1  # Change last element to 1

# Print all elements except the first two
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)
