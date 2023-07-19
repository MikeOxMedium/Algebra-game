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

    answer = input("press enter")

    # check if we are out of rounds
    if questions_answered >= questions:
        break
    elif answer == "xxx":
        break
