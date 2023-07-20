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
    print("When asked for the amount of rounds u want to play")
    print("You can choose <enter> for infinite mode, or a number for the certain amount of rounds")
    print()
    print("You can play as many rounds as you want")
    print("And when you feel like you want to quit, just press 'xxx' and the game will end")
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
        response = input("How many questions do you want to answer? or press <Enter> for infinite mode: ")

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


# Makes sure the response to the answer is above a certain number and a whole number

def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"
    if low is not None and high is not None:
        error = f"Please enter an integer between {low} and {high}"
        situation = "both"
    else:
        error = f"Please enter a number more than {low} or 'xxx' to quit"
        situation = "low only"

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check that integer is valid (ie: not too low / too hig etc)
            if situation == "any integer":
                return response

            elif situation == "both":
                if low <= response <= high:
                    return response

            elif situation == "low only":
                if response >= low:
                    return response

            print(error)

        except ValueError:
            print(error)


# Prints the statement

statement_generator("Welcome to The Algebra Quiz", "*")
print()

# Main Routine goes here...

played_before = yes_no("Have you played this quiz before? ")

# If they say no to played_before, then show instructions
if played_before == "no":
    instructions()

# List of valid response
yes_no_list = ["yes", "no"]
equations_list = [1, 2, 3, 4]

# Setting the variables to zero
questions_answered = 0
questions_right = 0
num_wrong = 0


mode = "regular"

quiz_summary = []

# Calls check_rounds() function
questions = check_rounds()

# If response is <Enter>, set mode to infinite
if questions == "":
    mode = "infinite"
    questions = 5

while questions_answered < questions:

    # Prints the heading for Infinite mode
    print()
    if mode == "infinite":
        heading = "Infinite Mode: "
        questions += 1

    # Makes sure if they respond with a whole number, says how many questions they are answering
    else:
        heading = "Question {} of " \
                  "{}".format(questions_answered + 1, questions)

    # If mode is infinite, change heading to infinite
    if mode == "infinite":
        heading = f"Question {questions_answered + 1} (infinite mode)"
        questions += 1

    # Otherwise print a heading that compares how many questions to go
    else:
        heading = f"Question {questions_answered + 1} of {questions}"

    # Print the heading
    print(heading)

    # Generating values for the questions
    a = random.randint(-20, 10)
    b = random.randint(-20, 10)
    c = random.randint(-20, 10)
    x = random.randint(-20, 10)

    equations_list = [1, 2, 3, 4]

    equation = random.choice(equations_list)

    # Shows a question like 3x + 5 = 20
    if equation == 1:
        c = a * x + b
        question = f"{a}x + {b} = {c}"

    # Shows a question like 3x - 5 = 10
    if equation == 2:
        c = a * x - b
        question = f"{a}x - {b} = {c}"

    # Shows a question like 3 + x = 7
    if equation == 3:
        c = x + a
        question = f"{a} + x = {c}"

    # Shows a question like 3 - x = -5
    if equation == 4:
        c = a - x
        question = f"{a} - x = {c}"
    answer = ""

    if answer == "":
        # Create the equation string
        print(question)
        answer = int_check("What is 'x' in the equation above (xxx to quit)", -20, exit_code="xxx")

        # Prints the print statement if a whole number or xxx was not the response to the question
        if answer == "":
            print("please enter a whole number or 'xxx' to quit")

        # Breaks code if they respond with 'xxx'
        elif answer == "xxx":
            break

        # Saying whether their answer was right or wrong
        elif int(answer) == x:
            print("!!! Correct !!!")
            questions_right += 1

        else:
            print("That's Wrong")
            print("The answer was", x)
            num_wrong += 1

    questions_answered += 1

    # Shows the quiz summary
    questions_right = questions_answered - num_wrong
    num_wrong = questions_answered - questions_right
    quiz_summary.append(heading)
    quiz_summary.append(
        "Question: {}\tAnswer: {}\tResult: {}".format(question, answer, "Correct" if int(answer) == x else "Wrong"))

    if questions_answered >= questions:
        break

# Calculates the percentage of questions wrong and right
if questions_answered > 0:
    percent_right = questions_right / questions_answered * 100
    percent_wrong = num_wrong / questions_answered * 100

    # prints the full game history and what your answer was to the question
    print()
    print("***** Quiz History *****")
    for outcome in quiz_summary:
        print(outcome)

    print()
    # Showing the percentage of wrong and right answers
    print("****** Quiz Statistics ******")
    print("Correct: {}, ({:.0f}%)\nWrong: {}, ({:.0f}%)\n ".format(questions_right, percent_right, num_wrong,
                                                                   percent_wrong))

    # How many were right and wrong
    print()
    print('***** End Quiz Summary *****')
    print("Correct: {} \t|\t Wrong: {} \t|\t "
          .format(questions_right, num_wrong, ))

    # Exit statements
    print()
    print("Thanks for playing")
    print("Hope you enjoyed my quiz")
