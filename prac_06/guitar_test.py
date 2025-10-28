"""CP1404-Practical  Manual tests for Guitar class methods."""

from prac_06.guitar import Guitar


def run_tests():
    """Test Guitar methods get_age() and is_vintage()."""
    test_guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    test_guitar_2 = Guitar("Another Guitar", 2013, 1512.9)

    # Testing get_age
    print(f"{test_guitar_1.name} get_age() - Expected ~100. Got {test_guitar_1.get_age()}")
    print(f"{test_guitar_2.name} get_age() - Expected ~{2025 - 2013}. Got {test_guitar_2.get_age()}")

    # Testing is_vintage
    print(f"{test_guitar_1.name} is_vintage() - Ex_
