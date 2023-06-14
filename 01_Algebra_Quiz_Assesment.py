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
    print("You need to answer these questions correctly in able to win more points")
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


def check_rounds():
    while True:
        response = input("How many rounds? or press <Enter> for continuous mode: ")

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


statement_generator("Welcome to The Algebra Quiz", "*")
print()

# Main Routine goes here...

played_before = yes_no("Have you played this game before? ")

if played_before == "no":
        instructions()


# List of valid response


rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

rounds = check_rounds()
if rounds == "":
    mode = "infinite"
    rounds = 5

while rounds_played < rounds:

    print()
    if mode == "infinite":
        heading = "Continuous Mode: " \
                  "Round {}".format(rounds_played + 1)
        rounds += 1

    else:
        heading = "Round {} of " \
                  "{}".format(rounds_played + 1, rounds)

    print(heading)
    rounds_played += 1

    end_game = "no"
    while end_game == "no":

        if mode == "infinite":
            heading = f"Round {rounds_played + 1} (infinite mode)"
            rounds += 1
        else:
            heading = f"Round {rounds_played + 1} of {rounds}"

        print(heading)

        rounds_played += 1

        answer = input("press enter")

        # check if we are out of rounds
        if rounds_played >= rounds:
            break
        elif answer == "xxx":
            break



