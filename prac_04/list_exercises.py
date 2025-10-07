"""
PseudoCode：
function main()
numbers = call get_numbers with 5 as argument
call display_number_stats with numbers
initialize list usernames with authorized usernames
call check_access with usernames

function get_numbers(count)
initialize empty list numbers
for i from 1 to count
    loop until valid number entered
        try to get number from user
        if input is valid
            break loop
        else
            print error message
    add number to numbers list
return numbers

function display_number_stats(numbers)
 print the first number in numbers
 print the last number in numbers
 print the smallest number in numbers
 print the largest number in numbers
 print the average of the numbers

function check_access(usernames)
 get username from user
 if username is in usernames
    print "Access granted"
 else
    print "Access denied"
"""

def main():
    """Main function to execute number input and username check."""
    numbers = get_numbers(5)
    display_number_stats(numbers)
    usernames = [
        'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
        'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
        'Command', 'ExecState', 'InteractiveConsole',
        'InterpreterInterface', 'StartServer', 'bob'
    ]
    check_access(usernames)


def get_numbers(count):
    """Prompt the user for a certain number of valid float inputs."""
    numbers = []
    for _ in range(count):
        while True:
            try:
                number_text = input("Number: ")
                number = float(number_text)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        numbers.append(number)
    return numbers


def display_number_stats(numbers):
    """Display the first, last, min, max, and average values of the number list."""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


def check_access(usernames):
    """Prompt for a username and check if it's authorized."""
    username = input("Enter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


if __name__ == "__main__":
    main()
