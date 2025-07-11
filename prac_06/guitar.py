"""CP1404Practical - Guitar class for storing guitar details."""

from datetime import date

# Constant to define vintage age threshold
VINTAGE_AGE = 50


class Guitar:
    """Represent a guitar with name, year, and cost."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance with name, year and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return formatted string of guitar details."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar based on the current year."""
        current_year = date.today().year
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage based on age threshold."""
        return self.get_age() >= VINTAGE_AGE


