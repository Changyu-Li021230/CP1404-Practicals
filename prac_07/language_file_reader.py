"""CP1404 Practical-Read programming language data from CSV, convert to objects, and display them.
"""

import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage

# === Constants ===
CSV_FILE = "languages.csv"
YES = "yes"


def main():
    """Load languages from CSV then display them."""
    languages = load_languages(CSV_FILE)
    for language in languages:
        print(language)


def load_languages(filename):
    """Return list of ProgrammingLanguage objects read from CSV."""
    languages = []
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            name, typing, reflection_str, year_str, ptr_str = row
            languages.append(
                ProgrammingLanguage(
                    name=name,
                    typing=typing,
                    reflection=reflection_str.lower() == YES,
                    year=int(year_str),
                    pointer_arithmetic=ptr_str.lower() == YES
                )
            )
    return languages


# ---------- Optional demo readers ---------- #

def using_csv():
    """Print each CSV row as raw list (demo)."""
    with open(CSV_FILE, newline='') as file:
        next(file)
        for row in csv.reader(file):
            print(row)


def using_namedtuple():
    """Print rows as named tuples (demo)."""
    Language = namedtuple("Language", "name typing reflection year pointer_arithmetic")
    with open(CSV_FILE, newline='') as file:
        next(file)
        for language in map(Language._make, csv.reader(file)):
            print(repr(language))


def using_csv_namedtuple():
    """Print name & year using csv + namedtuple (demo)."""
    Language = namedtuple("Language", "name typing reflection year pointer_arithmetic")
    with open(CSV_FILE, newline='') as file:
        next(file)
        for language in map(Language._make, csv.reader(file)):
            print(f"{language.name} was released in {language.year}")


if __name__ == "__main__":
    main()
