"""
CP1404 Practical - Read programming languages from file and convert to objects.
Demonstrates: file reading, class use, pointer arithmetic field, constants.
"""

import csv
from programming_language import ProgrammingLanguage

# === Constants ===
CSV_FILENAME = "languages.csv"
YES = "yes"
HEADER_LINE_INDEX = 0


def main():
    """Read programming language data from a CSV file and display it as objects."""
    languages = read_languages(CSV_FILENAME)
    print("Programming Languages:")
    for language in languages:
        print(language)


def read_languages(filename):
    """Read data from CSV and return a list of ProgrammingLanguage objects."""
    languages = []
    with open(filename, mode='r', newline='') as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip header
        for row in reader:
            name = row[0]
            typing = row[1]
            reflection = row[2].strip().lower() == YES
            year = int(row[3])
            pointer_arithmetic = row[4].strip().lower() == YES
            language = ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic)
            languages.append(language)
    return languages


# Uncomment the following line to run main if this file is run directly
# main()
