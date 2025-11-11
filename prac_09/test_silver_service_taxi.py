"""
CP1404
SilverServiceTaxi class test
"""

from prac_09.silver_service_taxi import SilverServiceTaxi

DRIVE_DISTANCE = 18


def main():
    """Test SilverServiceTaxi with sample drive and fare output."""
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(DRIVE_DISTANCE)
    print(taxi)
    print(f"Fare: ${taxi.get_fare():.2f}")


if __name__ == '__main__':
    main()
