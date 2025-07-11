"""
CP1404 Practical
ProgrammingLanguage class with pointer arithmetic support and demo.
"""

# === Constants ===
DYNAMIC_TYPING = "Dynamic"


def main():
    """Demonstrate filtering with ProgrammingLanguage objects."""
    languages = [
        ProgrammingLanguage("Ruby",  DYNAMIC_TYPING, True, 1995, False),
        ProgrammingLanguage("Python", DYNAMIC_TYPING, True, 1991, False),
        ProgrammingLanguage("Visual Basic", "Static", False, 1991, False),
        ProgrammingLanguage("C++", "Static", False, 1983, True),
    ]

    print("All languages:")
    display_filtered(languages, lambda _: True)

    print("\nDynamically typed languages:")
    display_filtered(languages, ProgrammingLanguage.is_dynamic)

    print("\nLanguages supporting pointer arithmetic:")
    display_filtered(languages, lambda lang: lang.pointer_arithmetic)


class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"Pointer Arithmetic={self.pointer_arithmetic}, "
                f"First appeared in {self.year}")

    def is_dynamic(self):
        """Return True if language uses dynamic typing."""
        return self.typing == DYNAMIC_TYPING


def display_filtered(languages, condition):
    """Print names of languages satisfying *condition*."""
    for lang in languages:
        if condition(lang):
            print(f"- {lang.name}")


if __name__ == "__main__":
    main()
# Code review request: please check logic and structure
