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
        heading = "Continuous Mode: "
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

        answer = input("press enter")

        # check if we are out of rounds
        if rounds_played >= rounds:
            break
        elif answer == "xxx":
            break
