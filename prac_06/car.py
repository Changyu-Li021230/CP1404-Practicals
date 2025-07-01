"""CP1404/CP5632 Practical - Car class"""

# Constant to define what qualifies as a vintage car (used elsewhere in prac)
VINTAGE_AGE = 50


class Car:
    """Represent a car with name, fuel amount, and odometer reading."""

    def __init__(self, name="", fuel=0):
        """Initialise a car with a name, amount of fuel, and odometer set to 0."""
        self.name = name
        self.fuel = fuel
        self._odometer = 0  # Start odometer at 0

    def __str__(self):
        """Return a formatted string showing car status."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"

    def add_fuel(self, amount):
        """Add given amount of fuel to the car."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance if enough fuel; update odometer.

        Return the actual distance driven.
        """
        actual_distance = min(distance, self.fuel)
        self.fuel -= actual_distance
        self._odometer += actual_distance
        return actual_distance
