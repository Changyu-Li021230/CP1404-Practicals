"""
CP1404/CP5632 Practical - Final Solution
State names in a dictionary.
File has been reformatted, uses EAFP, and prints all states.
"""

INPUT_PROMPT = "Enter short state: "
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

state = input(INPUT_PROMPT).upper()
while state != "":
    try:
        print(f"{state} is {CODE_TO_NAME[state]}")
    except KeyError:
        print("Invalid short state")
    state = input(INPUT_PROMPT).upper()

print("\nAll states:")
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")
