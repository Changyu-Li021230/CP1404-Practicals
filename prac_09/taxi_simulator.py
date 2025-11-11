"""
CP1404
Taxi Simulator

Provides an interactive simulator that lets the user choose between
regular and silver-service taxis, drive them, and track total cost.
"""

from prac_06.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
QUIT, CHOOSE, DRIVE = "q", "c", "d"
INITIAL_TAXIS = [
    ("Prius", 100, None),        # regular Taxi(name, fuel)
    ("Limo", 100, 2),            # SilverServiceTaxi(name, fuel, fanciness)
    ("Hummer", 200, 4),
]


def main():
    """Run the taxi simulator until the user quits."""
    total_bill = 0.0
    taxis = _build_taxis(INITIAL_TAXIS)
    current = None

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower().strip()

    while choice != QUIT:
        if choice == CHOOSE:
            current = _choose_taxi(taxis)
        elif choice == DRIVE:
            total_bill = _drive_and_bill(current, total_bill)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower().strip()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    _display_taxis(taxis)


def _build_taxis(config):
    """
    Given a list of tuples (name, fuel, fanciness or None),
    return a list of Taxi or SilverServiceTaxi instances.
    """
    taxis = []
    for name, fuel, fanciness in config:
        if fanciness is None:
            taxis.append(Taxi(name, fuel))
        else:
            taxis.append(SilverServiceTaxi(name, fuel, fanciness))
    return taxis


def _choose_taxi(taxis):
    """
    Display taxis and prompt user to choose one by index.
    Returns the chosen taxi or None on invalid input.
    """
    _display_taxis(taxis)
    try:
        index = int(input("Choose taxi: "))
        return taxis[index]
    except (ValueError, IndexError):
        print("Invalid taxi choice")
        return None


def _drive_and_bill(taxi, bill):
    """
    Prompt for distance, drive the selected taxi, show trip cost,
    and return updated bill. If taxi is None or input invalid, no change.
    """
    if taxi is None:
        print("You need to choose a taxi before you can drive")
        return bill

    taxi.start_fare()
    try:
        dist = float(input("Drive how far? "))
        driven = taxi.drive(dist)
        cost = taxi.get_fare()
        print(f"Your {taxi.name} drove {driven:.2f}km and cost ${cost:.2f}")
        return bill + cost
    except ValueError:
        print("Invalid distance")
        return bill


def _display_taxis(taxis):
    """Print a numbered list of taxis and their current states."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()
