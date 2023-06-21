import random


# checks users enter yes / no for a given question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes / no")


# Shows the instructions


def instructions():
    print()
    print("**** How to Play ****")
    print()
    print("You are going to get asked a series of algebra questions")
    print("You need to find the value of x:")
    print("You need to answer these questions correctly in able to have a higher winning percentage")
    print()
    print("Answer these questions carefully")
    print("The value of x will on almost every occasion be less than the answer in the question")
    print("And make sure you put down the right numbers")
    print()
    print("When asked for the amount of rounds u want to play")
    print("You can choose <enter> for infinite mode, or a number for the certain amount of rounds")
    print("Make sure to answer these questions carefully and get as many questions right as possible")
    print("Good luck and have fun")
    print()


# Generates a decoration for the welcoming statement

def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Asks how many rounds or press <enter> for infinite mode


def check_rounds():
    while True:
        response = input("How many rounds? or press <Enter> for infinite mode: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0\n"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


def num_check(question, low, high):
    error = "PLease enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


statement_generator("Welcome to The Algebra Quiz", "*")
print()

# Main Routine goes here...

played_before = yes_no("Have you played this game before? ")

# If they say no to played_before, then show instructions
if played_before == "no":
    instructions()

# List of valid response
yes_no_list = ["yes", "no"]
equations_list = ["{a}x + {b} = {c}",
                  "{a}x - {b} = {c}",
                  "{a} + x = {c}"]

rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

mode = "regular"

rounds = check_rounds()
if rounds == "":
    mode = "infinite"
    rounds = 5

while rounds_played < rounds:

    print()
    if mode == "infinite":
        heading = "Infinite Mode: "
        rounds += 1

    else:
        heading = "Round {} of " \
                  "{}".format(rounds_played + 1, rounds)

    if mode == "infinite":
        heading = f"Round {rounds_played + 1} (infinite mode)"
        rounds += 1
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)

    rounds_played += 1

    # Generate random coefficients and constants
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)

    # Create the equation string
    equation = random.choice(equations_list)
    print(equation)
    answer = input("What is 'x' in the equation above (xxx to quit): ")

    # check if we are out of rounds
    if rounds_played >= rounds:
        break
    elif answer == "xxx":
        break
