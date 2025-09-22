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
