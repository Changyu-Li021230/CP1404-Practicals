"""
CP1404 Practical - UnreliableCar class tests
Test the behavior of cars with different reliability levels.
"""

from prac_09.unreliable_car import UnreliableCar

START_KM = 1
END_KM = 12


def main():
    """Test UnreliableCar by driving with increasing distance and comparing reliability."""

    # Create cars with different reliabilities
    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)

    # Attempt to drive the cars multiple times and display the distance driven
    for distance in range(START_KM, END_KM):
        print(f"Attempting to drive {distance}km:")
        print(f"{good_car.name:12} drove {good_car.drive(distance):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(distance):2}km")

    # Print the final states of the cars
    print("\nFinal states:")
    print(good_car)
    print(bad_car)


if __name__ == '__main__':
    main()
