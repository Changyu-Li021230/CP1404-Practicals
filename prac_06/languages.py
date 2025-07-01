"""CP1404 Practical """

from prac_06.programming_language import ProgrammingLanguage

# Constants to represent typing styles
TYPING_DYNAMIC = "Dynamic"
TYPING_STATIC = "Static"


def main():
    """Print names of dynamically typed programming languages."""
    ruby = ProgrammingLanguage("Ruby", TYPING_DYNAMIC, True, 1995)
    python = ProgrammingLanguage("Python", TYPING_DYNAMIC, True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", TYPING_STATIC, False, 1991)

    languages = [ruby, python, visual_basic]

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    main()
# Minor update to trigger PR diff
