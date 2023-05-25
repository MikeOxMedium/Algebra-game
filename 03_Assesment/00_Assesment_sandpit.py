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
    print("You are going to get asked a series of questions")
    print("You have to answer those questions correctly or you will lose the game" )
    return ""


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