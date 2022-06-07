"""A number-guessing game."""

# Pseudocode

# greet player
# get player name
# choose random num 1-100
# repeat:
#   get guess
#       if guess incorrect:
#           give hint
#           increase number of guesses
#       else:
#           congratulate player

def guessing_game():
    greeting = "DO YOU WANT TO PLAY A GAME? *Imagine I am the SAW dude on the tricycle*"
    print(greeting) #if i want to change the greeting 

    yes_no = input("Press Y)es N)o or I) like turtles")
    if yes_no in "Yy":  # i'll let them slide with a lowercase
        print("")
    elif yes_no in "Nn":

