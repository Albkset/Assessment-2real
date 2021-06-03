
def statement_generator(statement, deco):
    sides = deco * 3
    statement = "{} {} {}".format(sides, statement,sides)
    top_bottom = deco * len(statement)
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# Main routine goes here

statement_generator ("Welcome to Lucky Unicorn Game", "*")
print()
statement_generator("Congratulations you got a Unicorn", "$")
print()