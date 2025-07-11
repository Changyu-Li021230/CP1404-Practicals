"""
min_length = 8

password = input("Enter your password: ")
while len(password) < min_length:
    print(f"Password must be at least {min_length} characters long.")
    password = input("Enter your password: ")
print("*" * len(password))

"""


"""
(Pseudocode:)

CONSTANT MIN_LENGTH = 8

function main()
    password = get_password(MIN_LENGTH)
    print_asterisks(password)

function get_password(min_length)
    get password from user
    while length of password < min_length
        print "Password must be at least {min_length} characters long."
        get password from user
    return password

function print_asterisks(password)
    print "*" repeated for length of password


"""

"""Password checker and asterisk printer program."""

MIN_LENGTH = 8  # Constant value, should be defined at top in ALL_CAPS


def main():
    """Main function to run password check and print asterisks
    ."""
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(min_length):
    """Get a valid password from the user that meets minimum length."""
    password = input("Enter your password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter your password: ")
    return password


def print_asterisks(password):
    """Print asterisks equal to the password length."""
    print("*" * len(password))


if __name__ == "__main__":
    main()
