"""
CP1404 Practical - Programming Language class with pointer arithmetic support.
"""

DYNAMIC_TYPING = "Dynamic"  # Constant for dynamic typing check


class ProgrammingLanguage:
    """Represent a programming language with core features."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """
        Initialize a programming language.
        :param name: Name of the language
        :param typing: Typing style ("Dynamic"/"Static")
        :param reflection: Boolean indicating reflection support
        :param year: Year introduced
        :param pointer_arithmetic: Boolean indicating pointer arithmetic support
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
    """Run the demonstration of ProgrammingLanguage features."""
    languages = [
        ProgrammingLanguage("Ruby", DYNAMIC_TYPING, True, 1995, False),
        ProgrammingLanguage("Python", DYNAMIC_TYPING, True, 1991, False),
        ProgrammingLanguage("Visual Basic", "Static", False, 1991, False),
        ProgrammingLanguage("C++", "Static", False, 1983, True),
        ProgrammingLanguage("C#", "Static", True, 2000, True)
    ]

    print("All Languages:")
    display_languages(languages)

    print("\nDynamically typed languages:")
    display_filtered_languages(languages, lambda lang: lang.is_dynamic())

    print("\nLanguages that support pointer arithmetic:")
    display_filtered_languages(languages, lambda lang: lang.pointer_arithmetic)


def display_languages(languages):
    """Display all language details."""
    for language in languages:
        print(language)


def display_filtered_languages(languages, condition):
    """Display languages matching a specific condition."""
    for language in languages:
        if condition(language):
            print(language.name)


if __name__ == "__main__":
    main()
