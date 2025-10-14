"""
Wimbledon Champions Summary

Reads Wimbledon men's singles champions data from CSV,
counts how many times each player has won,
and displays a summary of winners and countries.
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Load, process and display Wimbledon data."""
    records = load_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_champions(champion_to_count)
    display_countries(countries)


def load_records(filename):
    """Read CSV file and return list of records (each a list of fields)."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header row
        return [line.strip().split(",") for line in in_file]


def process_records(records):
    """Return champion-to-count dict and country set from records."""
    champion_to_count = {}
    countries = set()
    for record in records:
        country = record[INDEX_COUNTRY]
        champion = record[INDEX_CHAMPION]
        countries.add(country)
        # Use .get() to count wins (avoid try/except)
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
    return champion_to_count, countries


def display_champions(champion_to_count):
    """Display each champion and their win count, sorted by name."""
    print("Wimbledon Champions:")
    for champion, count in sorted(champion_to_count.items()):
        print(f"{champion:20} {count}")


def display_countries(countries):
    """Display sorted list of countries that have won Wimbledon."""
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


if __name__ == "__main__":
    main()
