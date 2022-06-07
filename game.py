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

    greeting = "DO YOU WANT TO PLAY A GAME? *Imagine I am the SAW dude on the little tricycle*"
    print(greeting) #if i want to change the greeting 

    player_name = input("How would you like me to address you sir/maam?\n>")

    yes_no = input("Type Y)es N)o or I) like turtles\n>")
    
    if yes_no in "Yy":  # i'll let them slide with a lowercase
        print("Just guess my number from 1-100 inclusive...\n" 
              "I didn't say it was a fun game...")        

    elif yes_no in "Nn":
        print("")
        end_game(player_name)

    elif yes_no in "Ii":
        print("Hey me too dude. Me too.\n"
              "I'll save you the trouble - don't play this game...")

        end_game(player_name)

    else:
        print("Listen here bud. You should have typed a Y or N or I." 
              "But since you didn't I will force you to play the game.")
        
    
    player_guess = input("Guess my number from 1 - 100 inclusive...\n>")
    


def end_game(player_name):
    print(f"Bye {player_name}. Hope you have a good day! Or don't. It's your life :)")
