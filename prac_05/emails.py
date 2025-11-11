"""
Emails
This program prompts users to enter emails,
guesses names from the addresses, allows confirmation or correction,
stores the results in a dictionary, and displays them formatted.
"""

AT_SYMBOL = "@"
DOT = "."
DEFAULT_CONFIRM = "y"

def main():
    """Prompt user for emails, extract/confirm names, and store in a dictionary."""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ("", DEFAULT_CONFIRM):
            name = input("Name: ").strip()
        email_to_name[email] = name
        email = input("Email: ")

    print("\nResults:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract expected name from email address."""
    username = email.split(AT_SYMBOL)[0]
    name_parts = username.split(DOT)
    return " ".join(name_parts).title()


if __name__ == "__main__":
    main()
