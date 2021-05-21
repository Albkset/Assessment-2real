play = ""
while play.lower() != "xxx":
    # Ask the user if they have have played before
    play = input("Have you played this game before? ").lower()

    # If they say yes, output 'program continues'
    if play == "yes" or play == "y":
        play = "yes"
        print("program continues")

    elif play == "no" or play == "n":
        play = "no"
        print("Display instructions")
    # If they say no, output 'display instructions'
    else:
        print("Please answer yes / no")

