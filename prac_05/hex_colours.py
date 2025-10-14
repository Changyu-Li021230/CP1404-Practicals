"""Hexadecimal Colour Lookup：
Estimate: 10 minutes
Actual: 9 minutes
This program allows users to input colour names (case-insensitive)
and returns the corresponding hexadecimal colour code if found.
"""

# Constant dictionary of colour names mapped to their hex codes
COLOUR_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "antiquewhite1": "#ffefdb",
    "antiquewhite2": "#eedfcc",
    "antiquewhite3": "#cdc0b0",
    "antiquewhite4": "#8b8378",
    "aquamarine1": "#7fffd4",
    "aquamarine2": "#76eec6",
    "aquamarine4": "#458b74",
    "azure1": "#f0ffff"
}

PROMPT = "Enter a colour name (blank to quit): "


def main():
    """Prompt for colour names and display corresponding hexadecimal codes."""
    colour_name = input(PROMPT)
    while colour_name != "":
        hex_code = get_colour_code(colour_name)
        if hex_code:
            print(f'The code for "{colour_name}" is {hex_code}')
        else:
            print(f'"{colour_name}" is not a valid colour name.')
        colour_name = input(PROMPT)


def get_colour_code(colour_name: str) -> str | None:
    """Return hexadecimal code for a given colour name, or None if not found."""
    return COLOUR_CODES.get(colour_name.lower())


if __name__ == "__main__":
    main()
