import simplegui

#global constants
counter = 0
times_stopped = 0
times_success = 0
tenths_left = 0

def format(t):
    """
    The format(t) helper function, uses constants to convert 
    the counter value (tenths of a second) to seconds(secs) 
    and minutes(mins). Using modular arithmetic the counter 
    value is reduced to the set (0...9) and seconds are 
    reduced in the set (0... 59). The corresponding variables
    are tenths_left and secs_left. The function returns a 
    properly formatted string (A:BC.D), adding a leading 
    zero to seconds if needed. The returned string is used 
    by the draw handler.
    """
    
    global tenths_left
    
    tenths_per_sec = 10
    secs_per_min = 60
    tenths_per_min = tenths_per_sec * secs_per_min
    
    secs = t / tenths_per_sec
    mins = t / tenths_per_min
   
    tenths_left = t % tenths_per_sec
    secs_left = secs % secs_per_min
        
    if secs_left < 10:
        return str(mins) + ":" + "0" + str(secs_left) + "." + str(tenths_left)
    else:
        return str(mins) + ":" + str(secs_left) + "." + str(tenths_left)
    
def start_butt_handler():
    """
    Initializes the counter. Would you like to... 
    PUSH THE BUTTON???
    """
    timer.start()
    
def stop_butt_handler():
    """
    Handler for the stop button. The timer is stopped only if
    it is already running! Each time the timer is stopped, the
    times_stopped counter increases. An if statement checks if 
    the timer was stopped "on time" (1.0, 2.0...) and 
    increases the corresponding counter (times_success).
    """
    global times_stopped, tenths_left, times_success
    
    if timer.is_running() == True:
        timer.stop()
        times_stopped += 1
        if tenths_left == 0:
            times_success += 1
    
def reset_butt_handler():
    """
    The reset button handler. Each time the Reset button is
    pressed, the timer is stopped. The counter (which counts
    the tenths of a second) resets and becomes zero, together
    with the two counters which count a) how many times the
    stop button was pressed and b) how many times the stop 
    button was pressed "on time" i.e. 1.0, 2.0 etc.
    """
    global counter, times_success, times_stopped
    
    timer.stop()
    counter = times_success = times_stopped = 0

def timer_handler():
    """
    The timer handler is called every 0.1s and simply 
    increases the global counter.
    """
    global counter
    counter += 1
    
def draw_handler(canvas):
    canvas.draw_text(format(counter), (55, 85), 80, 'White','monospace')
    canvas.draw_text(str(times_success) + "/" + str(times_stopped), (350, 20), 20, 'Red', 'monospace') 

frame = simplegui.create_frame('Timer', 400, 125)
frame.set_draw_handler(draw_handler)
frame.add_button('Start', start_butt_handler, 100)
frame.add_button('Stop', stop_butt_handler, 100)
frame.add_button('Reset', reset_butt_handler, 100)

timer = simplegui.create_timer(100, timer_handler)

frame.start()