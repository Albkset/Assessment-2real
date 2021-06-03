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



how_much = num_check("How much are you willing to pay? ", 0, 10)
print("You will be spending ${}".format(how_much))

import random
    # set balance for testing purpose

balance = how_much
STARTING_BALANCE = how_much

rounds_played = 0

play_again = input("Press <Enter> to play... ").lower()
while play_again == "":

    # increase # of the round played
    rounds_played += 1

    # Print round number
    print ("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1,100)
    
    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add $ 4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

    # if the random # is between 6 and 36   
    # user gets a donkey (subtract $1 from the balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
        
    # if the number is even, set the chosen 
    # item to a horse
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
         # otherwise set it to zebra
        else:
            chosen = "zebra"
            balance -= 0.5

            # output
    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))

    print()
    
    

    if balance < 1:
        play_again = "xxx"
        print ("Sorry you have run out of money")
    else:
        play_again = input("Please Enter to play again ""or 'xxx' to quit ")    


         
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: {:.2f}".format(balance))
    
having_fun = yes_no("Are you having fun? ")
if having_fun == "yes":
    print("you said {} to having fun ".format(having_fun))

else:
    print ("Thank you for your response")
print()