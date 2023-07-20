import random


def check_rounds():
    while True:
        response = input("How many Questions? or press <Enter> for infinite mode: ")

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


# Setting the variables to zero
questions_answered = 0
questions_right = 0
num_wrong = 0

mode = "regular"

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

    print(question)

    answer = input("press enter")

    questions_answered += 1

    # check if we are out of rounds
    if questions_answered >= questions:
        break
    elif answer == "xxx":
        break