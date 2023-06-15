import random


def generate_question():
    variable = random.choice(['x'])
    coefficient = random.randint(1, 10)
    constant = random.randint(1, 10)
    operation = random.choice(['+', '-'])
    equation = f"{coefficient}{variable} {operation} {constant} = {coefficient * variable} {operation} ?"

    return equation


# Example usage
question = generate_question()
print(question)

