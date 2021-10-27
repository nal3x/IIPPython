# template for "Stopwatch: The Game"

import simplegui

# define global variables
counter = 0
state = "OFF"
state_pos = (320, 120)
state_colour = "Red"


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass

def on_off():
    global state, state_colour, state_pos
    
    if timer.is_running() == True:
        state = "ON"
        state_pos = (320, 100)
        state_colour = "Green"
    else:
        state = "OFF"
        state_pos = (320, 120)
        state_colour = "Red" 

def start_butt_handler():
    timer.start()
    
def stop_butt_handler():
    timer.stop()
    
def reset_butt_handler():
    timer.stop()
    global counter
    counter = 0


def timer_handler():
    global counter
    counter += 1
        
    
def draw_handler(canvas):
    canvas.draw_text(str(counter), (10, 85), 80, 'White','monospace')
    canvas.draw_text(state, state_pos, 20, state_colour,'monospace')
    on_off()

frame = simplegui.create_frame('Timer', 400, 125)
frame.set_draw_handler(draw_handler)
frame.add_button('Start', start_butt_handler, 100)
frame.add_button('Stop', stop_butt_handler, 100)
frame.add_button('Reset', reset_butt_handler, 100)

timer = simplegui.create_timer(100, timer_handler)

frame.start()
