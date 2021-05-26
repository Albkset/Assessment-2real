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

def instructions():
    print("*****How to play *****")
    print()
    print("The rules of the game go here")
    print()
    return ""

# Main Routine goes here
played_before = yes_no("Have you played the game before  ")
if played_before == "no":
    instructions()

print("Programs continues")
print()

having_fun = yes_no("Are you having fun? ")
if having_fun == "yes":
    print("you said {} to having fun ".format(having_fun))

else:
    print ("Thank you for your response")

