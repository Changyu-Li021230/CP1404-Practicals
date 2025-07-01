"""CP1404/CP5632 Practical - Car Driving Simulator"""

from prac_06.car import Car

# Constants
INITIAL_FUEL = 100
INVALID_INPUT_MESSAGE = "Value must be >= 0"
MENU = "Menu:\nd) drive\nr) refuel\nq) quit"


def main():
    """Simulate driving a car with fuel management using a menu."""
    print("Let's drive!")
    name = input("Enter your car name: ")
    car = Car(name, INITIAL_FUEL)
    print(car)

    print(MENU)
    choice = input("Enter your choice: ").lower()

    while choice != "q":
        if choice == "d":
            distance_to_drive = get_non_negative_int("How many km do you wish to drive? ")
            distance_driven = car.drive(distance_to_drive)
            print(f"The car drove {distance_driven}km", end="")
            if car.fuel == 0:
                print(" and ran out of fuel", end="")
            print(".")
        elif choice == "r":
            fuel_to_add = get_non_negative_int("How many units of fuel do you want to add to the car? ")
            car.add_fuel(fuel_to_add)
            print(f"Added {fuel_to_add} units of fuel.")
        else:
            print("Invalid choice")

        print()
        print(car)
        print(MENU)
        choice = input("Enter your choice: ").lower()

    print(f"\nGood bye {car.name}'s driver.")


def get_non_negative_int(prompt):
    """Prompt user for a non-negative integer."""
    value = int(input(prompt))
    while value < 0:
        print(INVALID_INPUT_MESSAGE)
        value = int(input(prompt))
    return value


if __name__ == "__main__":
    main()
