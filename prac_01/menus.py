"""
constant MENU = "(H)ello\n(G)oodbye\n(Q)uit"

function main()
    get name
    display MENU
    get choice as uppercase input

    while choice is not "Q"
        if choice is "H"
            display "Hello" followed by name
        else if choice is "G"
            display "Goodbye" followed by name
        else
            display "Invalid choice"
        display MENU
        get choice as uppercase input

    display "Finished"

"""


MENU = "(H)ello\n(G)oodbye\n(Q)uit"  # constant for menu text

def main():
    name = input("Enter name: ")
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "H":
            print(f"Hello {name}")
        elif choice == "G":
            print(f"Goodbye {name}")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()

    print("Finished.")


if __name__ == "__main__":
    main()
