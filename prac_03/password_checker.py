
"""
CP1404/CP5632 - Practical
Password checker skeleton code
"""
"""
Define min_length = 2
Define max_length = 6
Define is_special_character_required = false
Define special_characters = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

function main()
    print "Please enter a valid password"
    print "Your password must be between " + min_length + " and " + max_length + " characters, and contain:"
    print "    1 or more uppercase characters"
    print "    1 or more lowercase characters"
    print "    1 or more numbers"

    if is_special_character_required
        print "    and 1 or more special characters: " + special_characters

    get password
    while not is_valid_password(password)
        print "Invalid password!"
        get password

    print "Your " + length of password + " character password is valid: " + password

function is_valid_password(password)
    if length of password < min_length or length of password > max_length
        return false

    set number_of_lower = 0
    set number_of_upper = 0
    set number_of_digit = 0
    set number_of_special = 0

    for each character in password
        if character is lowercase
            number_of_lower = number_of_lower + 1
        else if character is uppercase
            number_of_upper = number_of_upper + 1
        else if character is digit
            number_of_digit = number_of_digit + 1
        else if character is in special_characters
            number_of_special = number_of_special + 1

    if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0
        return false

    if is_special_character_required and number_of_special == 0
        return false

    return true

"""
"""Password checker: validate length and required character classes."""

MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main() -> None:
    """Run the interactive password checker."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print(f"\tand 1 or more special characters: {SPECIAL_CHARACTERS}")

    password = input("> ").strip()
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ").strip()

    print(f"Your {len(password)} character password is valid: {password}")

def is_valid_password(password: str) -> bool:
    """Return True if password meets length and character-class requirements."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0

    for character in password:
        if character.islower():
            number_of_lower += 1
        elif character.isupper():
            number_of_upper += 1
        elif character.isdigit():
            number_of_digit += 1
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1

    if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0:
        return False
    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special == 0:
        return False
    return True

if __name__ == "__main__":
    main()
