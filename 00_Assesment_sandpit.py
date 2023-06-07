def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer Yes / No")


while True:
    print("Im looping")

    played_before = yes_no("Have you played this game before? ")

    again = input("Press <enter> to loop...")

    if again != "":
        break

    print()
