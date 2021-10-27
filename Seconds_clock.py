import time
import simplegui
import math

radius = 30
center = (50, 50)
x = 50
y = 20
theta = 0
initial_time = time.time()

    
def timer():
    
    global theta, x, y
    theta = theta % 360
    theta += 6
    x = 50 - radius * math.sin(math.radians(theta - 180))
    y = 50 + radius * math.cos(math.radians(theta - 180))
    
def draw_handler(canvas):
    canvas.draw_text(str(int((time.time() - initial_time) % 60)), (140, 60), 40, "White")
    canvas.draw_circle(center, radius, 2, "White")
    canvas.draw_line(center, (x, y), 3, "White")
    


frame = simplegui.create_frame("Timer", 200, 100)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(1000, timer)
timer.start()
frame.start()
