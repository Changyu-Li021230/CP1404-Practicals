"""(Pseudocode:)

function get_valid_score()
    get score as float
    while score < 0 or score > 100
        print "Invalid score. Please enter a score between 0 and 100."
        get score as float
    return score

function get_score_result(score)
    if score < 0 or score > 100
        return "Invalid score"
    else if score >= 90
        return "Excellent"
    else if score >= 50
        return "Passable"
    else
        return "Bad"

function show_stars(score)
    print "*" repeated score times

function main()
    score = get_valid_score()
    print "Your initial score:", score, "->", get_score_result(score)

    CONSTANT MENU =
        "1. (G)et a valid score
         2. (P)rint result
         3. (S)how stars
         4. (Q)uit"

    print MENU
    get choice
    choice = choice in uppercase

    while choice is not "Q"
        if choice is "G"
            score = get_valid_score()
            print "Your score:", score, "->", get_score_result(score)
        else if choice is "P"
            print "Score result:", get_score_result(score)
        else if choice is "S"
            show_stars(score)
        else
            print "Invalid choice, please try again."

        print MENU
        get choice
        choice = choice in uppercase

    print "Farewell! Your final score was:", score
"""
"""Score menu program: validate score, classify it, and print stars."""

def main():
    """Main menu to manage score input, evaluation, and display."""
    score = get_valid_score()
    print(f"Your initial score: {score:.2f} -> {get_score_result(score)}")

    MENU = "1. (G)et a valid score\n2. (P)rint result\n3. (S)how stars\n4. (Q)uit"
    print(MENU)
    choice = input("Get choice: ").upper()

    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
            print(f"Your score: {score:.2f} -> {get_score_result(score)}")
        elif choice == 'P':
            print(f"Score result: {get_score_result(score)}")
        elif choice == 'S':
            show_stars(score)
        else:
            print("Invalid choice, please try again.")
        print(MENU)
        choice = input("Get choice: ").upper()

    print(f"Farewell! Your final score was: {score:.2f}")


def get_valid_score():
    """Prompt for a valid score between 0 and 100 inclusive."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


def get_score_result(score):
    """Return textual result for a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Display a number of asterisks equal to the integer score."""
    print('*' * int(score))


if __name__ == "__main__":
    main()
