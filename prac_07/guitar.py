"""CP1404 Practical – Guitar class for storing guitar details."""

from datetime import date

# === Constants ===
VINTAGE_AGE = 50


class Guitar:
    """Represent a guitar with name, year, and cost."""

    def __init__(self, name: str = "", year: int = 0, cost: float = 0.0):
        self.name = name
        self.year = year
        self.cost = cost

    # --------------------------------------------------------------------- #
    # Display helpers
    # --------------------------------------------------------------------- #
    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self):
        return f"Guitar({self.name!r}, {self.year}, {self.cost})"

    # --------------------------------------------------------------------- #
    # Business logic
    # --------------------------------------------------------------------- #
    def get_age(self) -> int:
        """Return guitar age in years."""
        return date.today().year - self.year

    def is_vintage(self) -> bool:
        """Return True if guitar is at least VINTAGE_AGE years old."""
        return self.get_age() >= VINTAGE_AGE

    # --------------------------------------------------------------------- #
    # Sorting support
    # --------------------------------------------------------------------- #
    def __lt__(self, other):
        """Compare guitars by year (older = less)."""
        return self.year < other.year
