"""
CP1404
SilverServiceTaxi class, derived from Taxi
"""

from prac_09.taxi import Taxi

DEFAULT_FLAGFALL = 4.5


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi with fanciness multiplier and flagfall fee."""

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness
        self.flagfall = DEFAULT_FLAGFALL

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the fare including flagfall."""
        return self.flagfall + super().get_fare()
