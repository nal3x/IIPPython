#Memory

import simplegui
import random

NUM_OF_CARDS = 16
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 100
CARD_WIDTH = CANVAS_WIDTH / NUM_OF_CARDS
DRAW_POINTS = range(3, CANVAS_WIDTH, CARD_WIDTH)
POLYGON = [ [ [i*CARD_WIDTH, 0],
              [(i + 1) * CARD_WIDTH, 0],
              [(i + 1) * CARD_WIDTH, CANVAS_HEIGHT],
              [i * CARD_WIDTH, CANVAS_HEIGHT] ] for i in range(NUM_OF_CARDS) ]

def new_game():
    global number, exposed, state, turns
    
    state = turns = 0
    label.set_text("Turns = 0")
 
    list1 = range(0, NUM_OF_CARDS / 2)
    number = range(0, NUM_OF_CARDS / 2)
    number.extend(list1)
    random.shuffle(number)
        
    exposed = [False for index in range(NUM_OF_CARDS)]

def mouseclick(pos):
    global state, card1, card2, turns

    clicked_card =  pos[0] / CARD_WIDTH
    if exposed[clicked_card] == False:
        exposed[clicked_card] = True
        if state == 0:
            card1 = clicked_card
            state = 1
        elif state == 1:
            card2 = clicked_card
            state = 2
            turns += 1
            label.set_text("Turns = " + str(turns))
        else:
            if number[card1] <> number[card2]:
                exposed[card1] = exposed[card2] = False
                exposed[clicked_card] = True
            state = 1
            card1 = clicked_card
                        
def draw(canvas):
    for i in range(NUM_OF_CARDS):
        canvas.draw_text(str(number[i]), (DRAW_POINTS[i], CANVAS_HEIGHT - 22), 70, 'White', "monospace")
        if exposed[i] == False:
            canvas.draw_polygon(POLYGON[i], 2, 'Red','Green')  

frame = simplegui.create_frame("Memory", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()
