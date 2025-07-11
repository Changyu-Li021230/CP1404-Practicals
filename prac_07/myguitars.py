"""
CP1404 Practical – More Guitars
Load existing guitars, display them, let user add more, then save back to CSV.
"""

import csv
from pathlib import Path
from guitar import Guitar

# === Constants ===
CSV_FILE = Path("guitars.csv")
QUIT_SENTINEL = ""           # 空名称表示结束输入


def main():
    """Drive the guitar program workflow."""
    guitars = load_guitars(CSV_FILE)
    print("These are the guitars loaded from file:")
    display_guitars(guitars)

    print("\nEnter your new guitars (blank name to stop):")
    guitars.extend(collect_user_guitars())

    guitars.sort()  # Guitar.__lt__ sorts by year
    print("\nAll guitars (sorted by year):")
    display_guitars(guitars)

    save_guitars(CSV_FILE, guitars)
    print(f"\nGuitars saved to {CSV_FILE.resolve()}")


# --------------------------------------------------------------------------- #
# Helper functions
# --------------------------------------------------------------------------- #
def load_guitars(filename: Path) -> list[Guitar]:
    """Return a list of Guitar objects read from CSV."""
    guitars = []
    if filename.exists():
        with filename.open(newline="") as file:
            reader = csv.reader(file)
            for name, year, cost in reader:
                guitars.append(Guitar(name, int(year), float(cost)))
    else:
        filename.touch()
    return guitars


def save_guitars(filename: Path, guitars: list[Guitar]):
    """Write all guitars to CSV: name,year,cost."""
    with filename.open("w", newline="") as file:
        writer = csv.writer(file)
        for g in guitars:
            writer.writerow([g.name, g.year, f"{g.cost:.2f}"])


def collect_user_guitars() -> list[Guitar]:
    """Prompt user to enter new guitars until a blank name is given."""
    new_guitars = []
    while True:
        name = input("Name: ")
        if name == QUIT_SENTINEL:
            break
        year = _prompt_int("Year: ")
        cost = _prompt_float("Cost: $")
        new_guitars.append(Guitar(name, year, cost))
    return new_guitars


def _prompt_int(prompt: str) -> int:
    """Return a valid integer from user input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer; please try again.")


def _prompt_float(prompt: str) -> float:
    """Return a valid float from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number; please try again.")


def display_guitars(guitars: list[Guitar]):
    """Display guitars in a numbered list."""
    for i, guitar in enumerate(guitars, start=1):
        print(f"{i}. {guitar}")


if __name__ == "__main__":
    main()
# Code review request: please check logic and structure
