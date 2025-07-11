"""
CP1404/CP5632 Practical - Programming Language class with pointer arithmetic support.
"""

DYNAMIC_TYPING = "Dynamic"  # constant for comparison

class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """
        Initialize a programming language with name, typing, reflection support,
        year introduced, and pointer arithmetic support.
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"Pointer Arithmetic={self.pointer_arithmetic}, First appeared in {self.year}")

    def is_dynamic(self):
        return self.typing == DYNAMIC_TYPING


def main():
    """Demonstrate the use of the ProgrammingLanguage class."""
    languages = [
        ProgrammingLanguage("Ruby", DYNAMIC_TYPING, True, 1995, False),
        ProgrammingLanguage("Python", DYNAMIC_TYPING, True, 1991, False),
        ProgrammingLanguage("Visual Basic", "Static", False, 1991, False),
        ProgrammingLanguage("C++", "Static", False, 1983, True),
        ProgrammingLanguage("C#", "Static", True, 2000, True),
    ]

    print("All Languages:")
    display_languages(languages)

    print("\nDynamically typed languages:")
    display_filtered_languages(languages, lambda lang: lang.is_dynamic())

    print("\nLanguages that support pointer arithmetic:")
    display_filtered_languages(languages, lambda lang: lang.pointer_arithmetic)


def display_languages(language_list):
    """Print details of all languages."""
    for language in language_list:
        print(language)


def display_filtered_languages(language_list, condition):
    """Print language names that match a given condition."""
    for language in language_list:
        if condition(language):
            print(language.name)


if __name__ == "__main__":
    main()
