"""
CP1404
UnreliableCar class, derived from Car
"""

from random import randint
from prac_09.car import Car

MIN_RANDOM = 1
MAX_RANDOM = 100


class UnreliableCar(Car):
    """An unreliable version of a car, which sometimes fails to drive."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar with reliability percentage (0–100)."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Attempt to drive the car a given distance.
        The car only drives if a randomly generated number is less than reliability.
        """
        random_number = randint(MIN_RANDOM, MAX_RANDOM)
        if random_number >= self.reliability:
            distance = 0  # Car failed to drive
        return super().drive(distance)
