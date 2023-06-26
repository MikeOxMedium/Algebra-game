import random


while True:
    # Generate random coefficients and constants
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)

    equations_list = [1, 2, 3, 4]

    equation = random.choice(equations_list)
    equation = 1

    if equation == 1:
        a = random.randint(-10, 10)
        x = random.randint(-10, 10)
        b = random.randint(-10, 10)

    c = a * x + b
    question = f"{a}x + {b} = {c}"

    print(question)
    print("answer", x)

    equation = random.choice(equations_list)
    equation = 2

    if equation == 2:
        a = random.randint(-10, 10)
        x = random.randint(-10, 10)
        b = random.randint(-10, 10)

    c = a * x - b
    question = f"{a}x - {b} = {c}"

    print(question)
    print("answer", x)

    equation = random.choice(equations_list)
    equation = 3

    if equation == 3:
        a = random.randint(-10, 10)
        x = random.randint(-10, 10)
        b = random.randint(-10, 10)

    c = x + a
    question = f"{a} + x = {c}"

    print(question)
    print("answer", x)

    equation = random.choice(equations_list)
    equation = 4

    if equation == 4:
        a = random.randint(-10, 10)
        x = random.randint(-10, 10)
        b = random.randint(-10, 10)

    c = x - a
    question = f"{a} - x = {c}"

    print(question)
    print("answer", x)

    input()