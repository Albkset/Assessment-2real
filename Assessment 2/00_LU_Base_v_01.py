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

def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            
            # if the amount is too low / too high give 
            if response > low and response <= high:
                return response

            #output an error

            else:
                print(error)
        except ValueError :
            print(error)

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
print()

how_much = num_check("How much are you willing to pay? ", 0, 10)
print("You will be spending ${}".format(how_much))
