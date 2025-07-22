"""
CP1404 - Test Taxi
Test the Taxi class by simulating two drives.
"""

from prac_09.taxi import Taxi

MAX_FUEL = 100  # Constant for maximum fuel level


def main():
    """Test the Taxi class with a sample drive and fare reset."""
    my_taxi = Taxi("Prius 1", MAX_FUEL)

    my_taxi.drive(40)
    print(my_taxi)  # Should show distance=40, fare

    my_taxi.start_fare()  # Reset fare
    my_taxi.drive(100)
    print(my_taxi)  # Should show distance=100, updated fare


if __name__ == '__main__':
    main()
