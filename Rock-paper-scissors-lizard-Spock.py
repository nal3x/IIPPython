import random

def name_to_number(name):
    """
    Helper function to convert number to string
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "name to number ERROR"

def number_to_name(number):
    """
    Helper function to convert string to number
    """
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "number to name ERROR"
        
def rpsls(player_choice):
    """
    This is the main function of the game.
    It takes the player's choice as input and randomly makes a choice for the computer.
    Finally it computes and prints the winner of the game.
    """
    
    #prints a blank line
    print
    
    #prints player's choice and assigns a number to it
    print  "Player chooses", player_choice
    player_number = name_to_number(player_choice)
    
    #computes a number for the computer, converts it to a choice and prints it
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses", comp_choice

    #computes the difference of the choices mod five
    #this choice determines the winner
    difference = (comp_number - player_number) % 5
    
    #if the difference is 1 or 2, the first item wins
    #if the difference is 3 or 4, the first item wins
    if (difference == 1) or (difference == 2):
        print "Computer wins!"
    elif (difference == 3) or (difference == 4):
        print "Player wins!"
    elif (difference == 0):
        print "Player and computer tie!"
    else:
        print "rpsls ERROR"

    
# test calls
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
