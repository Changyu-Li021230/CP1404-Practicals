"""
CP1404/CP5632 Practical
Band class to represent a band that has multiple musicians.
"""

DELIMITER = ", "  # Constant for joining musician names


class Band:
    """A musical band composed of multiple musician objects."""

    def __init__(self, name: str):
        """
        Initialise a Band.

        :param name: The band's name.
        """
        self.name = name
        self.musicians = []

    def add_musician(self, musician):
        """
        Add a musician to the band.

        :param musician: An object with a callable play() method.
        :raises TypeError: If musician.play is not callable.
        """
        if not hasattr(musician, "play") or not callable(musician.play):
            raise TypeError("Musician must have a callable play() method")
        self.musicians.append(musician)

    def remove_musician(self, musician):
        """
        Remove a musician from the band.

        :param musician: The musician to remove.
        :raises ValueError: If musician is not in the band.
        """
        self.musicians.remove(musician)

    def play(self):
        """
        Make each musician in the band play their instrument.

        If there are no musicians, does nothing.
        """
        for musician in self.musicians:
            musician.play()

    def __str__(self):
        """
        Return a string representation of the Band and its members.
        """
        member_list = DELIMITER.join(str(m) for m in self.musicians)
        return f"{self.name} ({member_list})"
