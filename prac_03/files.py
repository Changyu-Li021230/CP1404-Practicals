# Question 1: Ask for user name, write it to "name.txt" using open and close
"""
get name
open "name.txt" as file for writing
write name to file
close file
"""
name = input("Enter your name: ")
file = open('name.txt', 'w')
file.write(name)
file.close()

# Question 2: Open "name.txt", read the name, and print a greeting using open and close
"""
open "name.txt" as file for reading
read name_from_file from file
close file

remove extra whitespace from name_from_file
print "Hi " + name_from_file + "!"
"""
file = open('name.txt', 'r')
name_from_file = file.read().strip()
file.close()
print(f"Hi {name_from_file}!")

# Question 3: Read the first two numbers from "numbers.txt", add them and print the result
# Make sure "numbers.txt" contains: 17\n42\n400\n
"""
open "numbers.txt" as file for reading
read all lines from file into numbers
close file

convert numbers[0] to integer and remove extra whitespace
convert numbers[1] to integer and remove extra whitespace
set sum_of_first_two = numbers[0] + numbers[1]

print sum_of_first_two
"""
"""Read the first two numbers from numbers.txt and print their sum."""

with open("numbers.txt", "r") as file:
    numbers = file.readlines()
    first_number = int(numbers[0].strip())
    second_number = int(numbers[1].strip())
    sum_of_first_two = first_number + second_number
    print(sum_of_first_two)


# Question 4: Print the total sum of all the numbers in "numbers.txt"
"""
open "numbers.txt" as file for reading

set total = 0

for each line in file
    convert line to integer and remove extra whitespace
    total = total + line

close file

print total
"""
with open('numbers.txt', 'r') as file:
    total = 0
    for line in file:
        total += int(line.strip())
    print(total)
