"""
PseudoCode：
function main
initialize names as ["Bob", "Angel", "Jimi", "Alan", "Ada"]
initialize full_names as ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]
initialize empty list first_initials
for each name in names
add first character of name to first_initials
display first_initials
create list first_initials using list comprehension: first character of each name in names
display first_initials
create list full_initials using list comprehension:
for each name in full_names
split name into two parts
get first character of first part and first character of second part
concatenate and add to full_initials
display full_initials
create list a_names using list comprehension:
include name from names if name starts with 'A'
display a_names
sort names alphabetically
join sorted names with spaces into a single string
display the joined string
create list lowercase_full_names using list comprehension:
convert each name in full_names to lowercase
display lowercase_full_names
initialize almost_numbers as ['0', '10', '21', '3', '-7', '88', '9']
create list numbers by converting each string in almost_numbers to an integer using list comprehension
display numbers
create list greater_than_nine using list comprehension:
include number from numbers if number > 9
display greater_than_nine
create string last_names by joining with comma:
for each name in full_names
if length of name > 11
split name and take the second part (last name)
display last_names
"""

"""CP1404/CP5632 Practical - List comprehensions"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# For loop version
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# List comprehension version
first_initials = [name[0] for name in names]
print(first_initials)

# Full initials (first letter of first name + last name)
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

# Filter names starting with 'A'
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# Sorted, joined names
print(" ".join(sorted(names)))

# Full names in lowercase
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

# Convert strings to integers
almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
numbers = [int(number) for number in almost_numbers]
print(numbers)

# Filter numbers greater than 9
greater_than_nine = [number for number in numbers if number > 9]
print(greater_than_nine)

# Last names from full names longer than 11 characters
last_names = ", ".join([name.split()[1] for name in full_names if len(name) > 11])
print(last_names)
