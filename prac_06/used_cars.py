"""CP1404/CP5632 Practical - Client code to use the Car class."""

from prac_06.car import Car

# Constants
STARTING_FUEL = 100
ADDITIONAL_FUEL = 20
DRIVE_DISTANCE = 115


def main():
    """Demonstrate using the Car class to create and drive cars."""
    my_car = Car("My car", 180)
    my_car.drive(30)
    print(f"fuel: {my_car.fuel}")
    print(my_car)

    limo = Car("Limo", STARTING_FUEL)
    limo.add_fuel(ADDITIONAL_FUEL)
    print(f"Fuel after refueling: {limo.fuel}")
    limo.drive(DRIVE_DISTANCE)
    print(limo)


if __name__ == "__main__":
    main()