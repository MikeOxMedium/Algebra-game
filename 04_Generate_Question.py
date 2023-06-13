import random


def generate_equation():
    """Generates a random equation for the game."""
    # Generate random coefficients and constants
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)

    # Create the equation string
    equation = f"{a}x + {b} = {c}"

    return equation