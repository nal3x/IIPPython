# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
result = ""
prompt = ""
wins = losses = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        string = "hand contains: "
        for card in self.hand:
            string += str(card) + " "
        return string
            
    def add_card(self, card): #if len(hand) <3 for SECURITY???
        self.hand.append(card)

    def get_value(self):
        """ count aces as 1, if the hand has an ace,
        then add 10 to hand value if it doesn't bust
        """
        value = 0
        hand_has_ace = False
        
        for card in self.hand:
            rank = card.get_rank()
            if rank == 'A':
                hand_has_ace = True
            value += VALUES[rank]
            
        if hand_has_ace and (value + 10 <= 21):
            return value + 10
        else:
            return value
        
    def draw(self, canvas, pos):
        """
        + CARD_SIZE[0]/2 determines initial x of first card
        """
        for i in range(len(self.hand)):
            self.hand[i].draw(canvas, [(pos[0] * i) + CARD_SIZE[0] / 2 , pos[1]])
    
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS] #PRO!

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        string = "Deck contains: "
        for card in self.deck:
            string += str(card) + " "
        return string


#define event handlers for buttons
def deal():
    global losses, result, prompt, in_play ,dealers_hand, players_hand, deck

    if in_play:
        result = "You lost the round"
        prompt = "New deal?"
        in_play = False
        losses += 1
    else:
        deck = Deck()
        deck.shuffle()
    
        players_hand = Hand()
        dealers_hand = Hand()
    
        for i in range(2):
            players_hand.add_card(deck.deal_card())
            dealers_hand.add_card(deck.deal_card())
    
        in_play = True
        result = ""
        prompt = "Hit or stand?"
        
def hit():
    global in_play, losses, result, prompt
    
    if in_play:
        players_hand.add_card(deck.deal_card())
        
    if players_hand.get_value() > 21 and in_play:
        result = "You went bust and lose."
        prompt = "New deal?"
        in_play = False
        losses += 1
        
def stand():   
    global in_play, wins, losses, prompt, result
    
    if in_play:
        while dealers_hand.get_value() < 17:
            dealers_hand.add_card(deck.deal_card())
            
        if dealers_hand.get_value() > 21:
            result = "Dealer went bust. You win!"
            prompt = "New deal?"
            wins += 1
            in_play = False
        else:
            if players_hand.get_value() <= dealers_hand.get_value():
                result = "You lose."
                prompt = "New deal?"
                losses += 1
                in_play = False
            else:
                result =  "You win!"
                prompt = "New deal?"
                wins += 1
                in_play = False

# draw handler    
def draw(canvas):
    """
    CARD_SIZE[0]*1.2 tunes the distance of cards on canvas
    6 cards are always visible on the canvas
    """
    dealers_hand.draw(canvas, [CARD_SIZE[0] * 1.2, 200])
    players_hand.draw(canvas, [CARD_SIZE[0] * 1.2, 400])
    canvas.draw_text(result, (150 + CARD_SIZE[0] / 2 , 180), 35, 'Red',"sans-serif")
    canvas.draw_text(prompt, (150 + CARD_SIZE[0] / 2, 380), 35, 'Red',"sans-serif")
    canvas.draw_text("Blackjack", (150, 70), 70, "Black", "sans-serif")
    canvas.draw_text("Dealer", (CARD_SIZE[0] / 2, 180), 35, "Black", "sans-serif")
    canvas.draw_text("Player", (CARD_SIZE[0] / 2, 380), 35, "Black", "sans-serif")
    canvas.draw_text(str(wins) + "-" + str(losses), (275, 560), 30, "Black", "monospace")
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (CARD_SIZE[0], 200 + CARD_SIZE[1] / 2), CARD_SIZE)        
        


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()