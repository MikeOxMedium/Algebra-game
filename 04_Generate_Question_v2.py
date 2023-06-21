import random


def generate_equation():
    # Generate random coefficients and constants
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)

    equations_list = [f"{a}x + {b} = {c}",
                      f"{a}x - {b} = {c}",
                      f"{a} + x = {c}",
                      f"{a} - x = {c}"]

    equation = random.choice(equations_list)

    return equation


for item in range(1, 21):
    question = generate_equation()
    print(question)
