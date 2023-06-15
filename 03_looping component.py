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