"""
<Pseudocode:>
constant DISCOUNT_THRESHOLD = 100
constant DISCOUNT_RATE = 0.9

function main()
    get number_of_items as integer
    while number_of_items < 0
        display "Invalid number of items!"
        get number_of_items as integer

    total_price = 0
    for each item from 1 to number_of_items
        get price_of_item as float
        while price_of_item < 0
            display "Invalid price! Please enter a positive value."
            get price_of_item as float
        total_price = total_price + price_of_item

    if total_price > DISCOUNT_THRESHOLD
        total_price = total_price * DISCOUNT_RATE

    display total_price formatted to 2 decimal places, with number_of_items

"""

DISCOUNT_THRESHOLD = 100  # dollars
DISCOUNT_RATE = 0.9       # 10% discount

def main():
    number_of_items = int(input("Number of items: "))
    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))

    total_price = 0
    for i in range(number_of_items):
        price_of_item = float(input(f"Price of item {i + 1}: "))
        while price_of_item < 0:
            print("Invalid price! Please enter a positive value.")
            price_of_item = float(input(f"Price of item {i + 1}: "))
        total_price += price_of_item

    if total_price > DISCOUNT_THRESHOLD:
        total_price *= DISCOUNT_RATE  # Apply discount

    print(f"Total price for {number_of_items} items is ${total_price:.2f}")


if __name__ == "__main__":
    main()
