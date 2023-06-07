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


def solve_equation(equation):
    """Solves the equation and returns the value of x."""
    # Extract the coefficients and constant from the equation
    parts = equation.split()
    a = int(parts[0][:-1])  # Remove 'x' from the coefficient
    b = int(parts[2])
    c = int(parts[4])

    # Solve the equation for x
    x = (c - b) / a

    return x


def play_game():
    """Main game loop."""
    print("Welcome to the Algebra Game!")
    print("Find the value of 'x' in the following equation:")

    equation = generate_equation()
    print(equation)

    # Get the player's guess
    guess = float(input("Enter the value of 'x': "))

    # Solve the equation
    x = solve_equation(equation)

    # Check if the player's guess is correct
    if guess == x:
        print("Congratulations! You found the correct value of 'x'.")
    else:
        print(f"Oops! The correct value of 'x' is {x}.")

    play_again = input("Do you want to play again? (yes/no): ")

    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thank you for playing!")


# Start the game
play_game()

