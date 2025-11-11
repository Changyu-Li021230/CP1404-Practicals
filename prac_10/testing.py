"""
CP1404/CP5632 Practical - Suggested Solution
Test functions and the Car class using assert and doctest.
"""

import doctest
from prac_06.car import Carzzzzzzzzzzz


# Constants for testing
DEFAULT_FUEL = 0
TEST_FUEL = 10
DEFAULT_ODOMETER = 0


def repeat_string(s, n):
    """
    Repeat string s, n times, with spaces in between.

    >>> repeat_string("Python", 1)
    'Python'
    >>> repeat_string("hi", 2)
    'hi hi'
    >>> repeat_string("yes", 0)
    ''
    """
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the given length.

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def phrase_to_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a period.

    >>> phrase_to_sentence("hello")
    'Hello.'
    >>> phrase_to_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> phrase_to_sentence("this subject rocks")
    'This subject rocks.'
    >>> phrase_to_sentence("  already ends. ")
    'Already ends.'
    >>> phrase_to_sentence("")
    ''
    """
    phrase = phrase.strip()
    if not phrase:
        return ""
    sentence = phrase.capitalize()
    if not sentence.endswith('.'):
        sentence += '.'
    return sentence


def run_tests():
    """Run the tests on the functions and Car class."""
    # Function tests
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    assert is_long_word("Python")
    assert not is_long_word("hi", 3)

    assert phrase_to_sentence("hi") == "Hi."
    assert phrase_to_sentence("Hi.") == "Hi."
    assert phrase_to_sentence("   ") == ""

    # Car class tests
    car = Car()
    assert car._odometer == DEFAULT_ODOMETER, "Car does not set odometer correctly"
    assert car.fuel == DEFAULT_FUEL, "Car default fuel should be 0"

    car_with_fuel = Car(fuel=TEST_FUEL)
    assert car_with_fuel.fuel == TEST_FUEL, "Car did not set fuel correctly"


if __name__ == "__main__":
    run_tests()
    doctest.testmod()
