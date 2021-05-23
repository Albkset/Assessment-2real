# Functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        # If they say yes, output 'program continues'
        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response


        # If they say no, output 'display instructions'
        else:
            print("Please answer yes / no")

# Main Routine goes here
show_instructions = yes_no("Have you played the game before  ")
print("You chose {}". format(show_instructions))
print()
having_fun = yes_no("Are you having fun? ")
print("you said {} to having fun ".format(having_fun))