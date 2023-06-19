import random


def generate_equation():

    # Generate random coefficients and constants
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)

    # Create the equation string
    equation = f"{a}x + {b} = {c}"
    equation = f"{a}x = {c}"
    equation = f"{a}x - {b} = {c}"
    equation = f"{a} + x = {c}"
    return equation
