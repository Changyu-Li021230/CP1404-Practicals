# Display all odd numbers between 1 and 20, each separated by a space
"""
<Pseudocode:>
for i from 1 to 20 step 2
    print i on the same line
print newline
"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()  # print newline


# a. Count in 10s from 0 to 100
"""
<Pseudocode:>
for i from 0 to 100 step 10
    print i on the same line
print newline
"""
for i in range(0, 101, 10):
    print(i, end=' ')
print()  # print newline


# b. Count down from 20 to 1
"""
<Pseudocode:>
for i from 20 to 1 step -1
    print i on the same line
print newline
"""
for i in range(20, 0, -1):
    print(i, end=' ')
print()  # print newline


# c. Print n stars on one line
"""
<Pseudocode:>
get n as integer
for i from 0 to n - 1
    print "*" on the same line
print newline
"""
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print('*', end='')
print()  # move to new line after printing all stars


# d. Print n lines of increasing stars
"""
<Pseudocode:>
for i from 1 to n
    print "*" repeated i times
"""
for i in range(1, number_of_stars + 1):
    print('*' * i)
