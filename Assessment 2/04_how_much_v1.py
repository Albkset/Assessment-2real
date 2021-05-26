# Functions go here



# Main routine goes here

error = "Please enter a whole number between 1 and 10"

question = "How much are you willing to pay? "

valid = False
while not valid:
    try:
        # ask the question
        response = int(input(question))
        
        # if the amount is too low / too high give 
        if response > 0 and response <= 10:
            print("You will be spending ${}".format(response))

        #output an error

        else:
            print(error)
    except ValueError as e:
        print(e)
