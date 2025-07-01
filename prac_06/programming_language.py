"""CP1404Practical """

# Constants
TYPING_DYNAMIC = "Dynamic"
TYPING_STATIC = "Static"


class ProgrammingLanguage:
    """Store information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise ProgrammingLanguage with name, typing, reflection, and year."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return formatted string of language details."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return True if the language uses dynamic typing."""
        return self.typing == TYPING_DYNAMIC


def run_tests():
    """Run demonstration of ProgrammingLanguage class and methods."""
    ruby = ProgrammingLanguage("Ruby", TYPING_DYNAMIC, True, 1995)
    python = ProgrammingLanguage("Python", TYPING_DYNAMIC, True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", TYPING_STATIC, False, 1991)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
# Minor update to trigger PR diff
# No functional change — added to trigger GitHub diff
