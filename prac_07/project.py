"""
CP1404 Practical 07 - Project class module
Estimated time: 1.5 hours
"""

from datetime import datetime

# Constants
DEFAULT_PRIORITY = 1
COMPLETED_PERCENTAGE = 100
DATE_FORMAT = "%d/%m/%Y"


class Project:
    """Represent a project with its key attributes."""

    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        """Initialise a project."""
        self.name = name
        self.start_date = datetime.strptime(start_date, DATE_FORMAT).date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.percent_complete = int(percent_complete)

    def __repr__(self):
        """Return string representation of the Project object."""
        return (f"{self.name}, start: {self.start_date.strftime(DATE_FORMAT)}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.percent_complete}%")

    def is_complete(self):
        """Return True if the project is 100% complete."""
        return self.percent_complete == COMPLETED_PERCENTAGE

    def update(self, percent_complete=None, priority=None):
        """Update project's percent_complete and/or priority."""
        if percent_complete != "":
            self.percent_complete = int(percent_complete)
        if priority != "":
            self.priority = int(priority)

    def __lt__(self, other):
        """Enable sorting by priority."""
        return self.priority < other.priority

    def to_save_format(self):
        """Return tab-separated string format for saving to file."""
        return (f"{self.name}\t{self.start_date.strftime(DATE_FORMAT)}\t"
                f"{self.priority}\t{self.cost_estimate:.2f}\t{self.percent_complete}")

# Dummy line for code review trigger
