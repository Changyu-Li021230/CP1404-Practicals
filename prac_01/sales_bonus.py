"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

"""
Pseudocode:
get sales
while sales >= 0
    if sales < 1000
        bonus = sales * 0.10
    else
        bonus = sales * 0.15
    print bonus formatted to 2 decimal places
    get sales

"""

# === Constants ===
BONUS_THRESHOLD = 1000
LOW_BONUS_RATE = 0.10
HIGH_BONUS_RATE = 0.15


def main():
    sales = float(input("Enter sales: $"))  # priming read

    while sales >= 0:
        # choose rate based on threshold
        if sales < BONUS_THRESHOLD:
            bonus = sales * LOW_BONUS_RATE
        else:
            bonus = sales * HIGH_BONUS_RATE

        print(f"Bonus: ${bonus:.2f}")

        # get next input
        sales = float(input("Enter sales: $"))

    print("Finished")


main()