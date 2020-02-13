# ask user for number
# Loop question so that it repeats until valid number is entered
# make code recyclable

valid = False
while not valid:
    error = "Whoops! Please enter an integer"

    try:
        response = int(input("Enter an integer bewteen 1 and 10:"))

        if 1 <= response <= 10:
            valid = True
        else:
            print(error)
            print()

    except ValueError:
        print(error)

print(response)

