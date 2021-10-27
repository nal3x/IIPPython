import random
import simplegui
import math

#global variables initialization
range = 100
random_number = -1
remaining_guesses = -1
        

def new_game(range):
    """ Used to start and restart the game. Computes a 
    random number in the given range and the remaining
    guesses allowed for the player using the base 2
    logarithm. Prints a New game message with the
    corresponding range and the number of guesses 
    allowed each time the game is restarted. Remove
    the # to reveal the secret value for debbuging.
    """
    
    global random_number
    random_number = random.randrange(0, range)
    
    global remaining_guesses
    remaining_guesses = int(math.ceil(math.log(range, 2)))
    
    print "New game. Range is from 0 to", range
    #print "Random number is:", random_number
    print "Remaining guesses:", remaining_guesses
    print
   
def range100():
    """Button handler. Sets range to 100 and starts 
    a new game with that range.
    """
    global range
    range = 100
    new_game(range)

def range1000():
    """Button handler. Sets range to 1000 and starts 
    a new game with that range. 
    """
    global range 
    range = 1000
    new_game(range)
    
def input_guess(guess):
    """
    This is the main part. It gets the user input (guess)
    and converts it to an integer. The remaining guesses 
    are reduced each time a guess is entered. The guess 
    is compared to the secret value and the appropriate 
    message is printed. If the player finds the hidden 
    number a new game is started. A final check restarts
    the game if no other attempts are allowed.
    """
    guess = int(guess)
    print "Guess was: ", guess
    
    global remaining_guesses
    remaining_guesses -= 1
    
    if guess < random_number:
        print "Higher!"
        print "Remaining guesses:", remaining_guesses
        print
    elif guess > random_number:
        print "Lower!"
        print "Remaining guesses:", remaining_guesses
        print
    elif guess == random_number:
        print "Correct!!!\n"
        new_game(range)
    
    if remaining_guesses == 0:
        print "Game over\n"
        new_game(range)
        
# create frame    
frame = simplegui.create_frame("Guess the number!", 200, 200)

# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game and start frame
new_game(range)
frame.start()

