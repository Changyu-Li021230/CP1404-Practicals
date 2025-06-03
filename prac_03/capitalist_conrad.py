"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 17.5%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $100 or falls below $1, the program should end.
Prices are displayed to 2 decimal places and written to a file.
"""
"""
DEFINE MAX_INCREASE = 0.175 
DEFINE MAX_DECREASE = 0.05   
DEFINE MIN_PRICE = 1.00      
DEFINE MAX_PRICE = 100.00   
DEFINE INITIAL_PRICE = 10.00
DEFINE FILENAME = "stock_price_simulation.txt"

SET price = INITIAL_PRICE
SET number_of_days = 0


open filename as out_file for writing
print "Starting price: $" + format price to 2 decimal places to out_file

while min_price <= price <= max_price
    number_of_days = number_of_days + 1

    if random integer between 1 and 2 is 1
        set price_change = random float between 0 and max_increase
    else
        set price_change = random float between -max_decrease and 0

    price = price * (1 + price_change)
    print "On day " + number_of_days + " price is: $" + format price to 2 decimal places to out_file

close out_file

"""
import random

MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MIN_PRICE = 1.00
MAX_PRICE = 100.00
INITIAL_PRICE = 10.00
FILENAME = "stock_price_simulation.txt"

price = INITIAL_PRICE
number_of_days = 0

out_file = open(FILENAME, "w")
print("Starting price: ${:.2f}".format(price), file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days = number_of_days + 1

    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price = price * (1 + price_change)
    print("On day {} price is: ${:.2f}".format(number_of_days, price), file=out_file)

out_file.close()
