"""
PseudoCode：
CONSTANT NUMERIC_TYPE = float
CONSTANT MONTH_PROMPT = "Enter income for month {}: "
CONSTANT HEADER = "\nIncome Report\n-------------"

function main()
    initialize empty list incomes
    get number of months from user, store in num_months
    for month from 1 to num_months
        get income from user using formatted MONTH_PROMPT
        convert income to NUMERIC_TYPE
        add income to incomes
    call print_income_report with num_months and incomes

function print_income_report(num_months, incomes)
    print HEADER
    set total to 0
    for month from 1 to num_months
        set income to incomes[month - 1]
        add income to total
        print formatted month, income, and total
"""
"""
CP1404/CP5632 Practical
Display income report for incomes over a given number of months.
"""

NUMERIC_TYPE = float  # For clarity and easier changes
MONTH_PROMPT = "Enter income for month {}: "
HEADER = "\nIncome Report\n-------------"

def main():
    """Get incomes and display a formatted report."""
    incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = NUMERIC_TYPE(input(MONTH_PROMPT.format(month)))
        incomes.append(income)

    print_income_report(num_months, incomes)


def print_income_report(num_months, incomes):
    """Print income report with cumulative totals."""
    print(HEADER)
    total = 0
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f}           Total: ${total:10.2f}")


main()
