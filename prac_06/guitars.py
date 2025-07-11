"""CP1404 Practical - Program to record and display guitars."""

from prac_06.guitar import Guitar

# Constants
NAME_WIDTH = 20
COST_WIDTH = 10


def main():
    """Allow user to input and display guitars, including vintage status."""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added.")
        name = input("Name: ")

    # Sample data for testing
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>{NAME_WIDTH}} ({guitar.year}), "
                  f"worth ${guitar.cost:{COST_WIDTH},.2f}{vintage_string}")
    else:
        print("No guitars :( Quick, go and buy one!")


if __name__ == "__main__":
    main()
