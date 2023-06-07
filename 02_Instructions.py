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


def instructions():
    print()
    print("**** How to Play ****")
    print()
    print("You are going to get asked a series of algebra questions")
    print("You need to find the value of x:")
    print("You need to answer these questions correctly in able to win more points")
    print()
    print("Answer these questions carefully")
    print("The value of x will on almost every occasion be less than the answer in the question")
    print("And make sure you put down the right numbers")
    print()
    print("Good luck and have fun")
    print("And make sure to answer as many questions correctly as possible")
    print()


def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


statement_generator("Welcome to The Algebra Quiz", "*")
print()

# Main Routine goes here...
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()