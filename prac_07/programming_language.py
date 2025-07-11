"""
CP1404 Practical
ProgrammingLanguage class with pointer arithmetic support and filtering logic.
"""

# === Constants ===
DYNAMIC_TYPING = "Dynamic"


def main():
    """Run ProgrammingLanguage test and filtered display."""
    ruby = ProgrammingLanguage("Ruby", DYNAMIC_TYPING, True, 1995, False)
    python = ProgrammingLanguage("Python", DYNAMIC_TYPING, True, 1991, False)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)
    cpp = ProgrammingLanguage("C++", "Static", False, 1983, True)

    languages = [ruby, python, vb, cpp]

    print(python)

    print("\nDynamically typed languages:")
    display_filtered_languages(languages, lambda lang: lang.is_dynamic())

    print("\nLanguages supporting pointer arithmetic:")
    display_filtered_languages(languages, lambda lang: lang.pointer_arithmetic)


class ProgrammingLanguage:
    """Stores information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
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


def display_filtered_languages(languages, condition):
    """Print language names that match a filter condition."""
    for language in languages:
        if condition(language):
            print(f"- {language.name}")


if __name__ == "__main__":
    main()
