
def statement_generator(statement, deco):
    sides = deco * 3
    statement = "{} {} {}".format(sides, statement,sides)
    top_bottom = deco * len(statement)
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

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
    statement_generator("How to Play", "*")
    print()
    print("The rules of the game go here")
    print()
    print("Choose a starting amount minium $1, maximum $10.")
    print()
    print("Then press <enter> to play. You will get either a horse, a zebra, a donkey or a unicorn.")
    print()
    print("It costs a $1 per round. Depending on your prize you might win some of the money back. Here's thee payout accounts...")
    print("Unicorn: $5.00 (balance increase by $4)")
    print("Donkey: $1 (balance decreases by $1)")
    print("Horse: $0.50 (balance decreases by $0.50) " )
    print("Zebra: $0.50 (balance decreases by $0.50)")
    print()
    print("Can you avoid tthe donkeys, gett the unicorns and walk home with the money??")
    print()
    print("Hint: to quit while you are ahead, type 'xxx' instead of pressing <enter>")    

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
print()
statement_generator("Welcome to Lucky Unicorn Game", "*")
print()

played_before = yes_no("Have you played the game before  ")
print()
if played_before == "no":
    instructions()

print()
statement_generator("Let's get Started", "-")
print()


how_much = num_check("How much are you willing to pay? $", 0, 10)
print()
print("You will be spending ${}".format(how_much))
print()

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
    print()
    statement_generator("Round #{}".format(rounds_played), "*")
    print()

    chosen_num = random.randint(1,100)
    
    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add $ 4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
        statement_generator("You got a Unicorn. Your balance is ${:.2f}".format(balance), "$")

    # if the random # is between 6 and 36   
    # user gets a donkey (subtract $1 from the balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
        statement_generator("You got a Donkey. Your balance is ${:.2f}".format(balance), "D")
        
    # if the number is even, set the chosen 
    # item to a horse
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
            balance -= 0.5
            statement_generator("You got a Horse. Your balance is ${:.2f}".format(balance), "H")
         # otherwise set it to zebra
        else:
            chosen = "zebra"
            balance -= 0.5
            statement_generator("You got a Zebra. Your balance is ${:.2f}".format(balance), "Z")
            
            # output
    

    print()
    
    

    if balance < 1:
        play_again = "xxx"
        print ("Sorry you have run out of money")
    else:
        play_again = input("Please Enter to play again ""or 'xxx' to quit ")    


print()
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: {:.2f}".format(balance))
print()

having_fun = yes_no("Are you having fun? ")
if having_fun == "yes":
    print()
    statement_generator("Thank you for enjoying our game, We hope you play with us again ", "*")
else:
    print()
    statement_generator("Thank you for your response", "#")
print()

