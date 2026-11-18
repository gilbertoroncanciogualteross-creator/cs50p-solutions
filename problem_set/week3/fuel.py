# In a file called fuel.py, implement a program  that prompts the user for a fraction,
# formatted as X/Y, wherein x is a non-negative integer and Y is a positive integer,
# and then outputs, as a percentage rounded to the nearest integer, how wuch fuel is in the tank.

# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance
# 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full.

while True:
    try:
        fraction = input("Fraction: ").split("/")
        x = float(fraction[0])
        z = float(fraction[1])

        result = x / z
        result = round(result * 100)

        if result <= 1:
            print("E")

        elif result >= 99:
            print("F")

        else:
            print(f"{result}%")

        break

    except (ValueError, ZeroDivisionError, IndexError):
        pass
