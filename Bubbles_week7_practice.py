# Basic infrastructure for Bubble Shooter

import simplegui
import random
import math

# Global constants
WIDTH = 800
HEIGHT = 600
FIRING_POSITION = [WIDTH // 2, HEIGHT]
FIRING_LINE_LENGTH = 60
FIRING_ANGLE_VEL_INC = 0.02
FIRING_ANGLE_ACC_INC = 0.01
BUBBLE_RADIUS = 20
COLOR_LIST = ["Red", "Green", "Blue", "White"]

# global variables
firing_angle = math.pi / 2
firing_angle_vel = firing_angle_acc = 0
bubble_stuck = True

# firing sound
firing_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Collision8-Bit.ogg")
firing_sound.set_volume(0.5)


# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)


# class defintion for Bubbles
class Bubble:
    
    def __init__(self):
        self.pos = list(FIRING_POSITION)
        self.vel = [0, 0]
        self.color = COLOR_LIST[random.randrange(0,4)]
    
    def __str__(self):
        return "Ball_position = " + str(self.pos) + "\n" + "Ball_velocity = " + str(self.vel) + "\n" + "Ball_color    = " + self.color
    
    def update(self):        
        for i in range(0,2):
            self.pos[i] += self.vel[i]
        if self.pos[0] - BUBBLE_RADIUS <= 0 or self.pos[0] + BUBBLE_RADIUS >= WIDTH: 
            self.vel[0] = -self.vel[0]
    
    def fire_bubble(self, vel):
        self.vel = vel
        
    def is_stuck(self): 
        pass

    def collide(self, bubble):
        pass
            
    def draw(self, canvas):
        canvas.draw_circle(self.pos, BUBBLE_RADIUS, 1, self.color, self.color)
        

# define keyhandlers to control firing_angle
def keydown(key):
    global a_bubble, firing_angle_acc, bubble_stuck
    
    if key == simplegui.KEY_MAP['right']:
        firing_angle_acc += FIRING_ANGLE_ACC_INC
    elif key == simplegui.KEY_MAP['left']:
        firing_angle_acc -= FIRING_ANGLE_ACC_INC
    elif key == simplegui.KEY_MAP['space']:
        bubble_stuck = False
        vel = angle_to_vector(firing_angle)
        a_bubble.fire_bubble([-4 * vel[0], -4 * vel[1]])
        firing_sound.play()
        
        
        

def keyup(key):
    global firing_angle_acc
    if key == simplegui.KEY_MAP['right']:
        firing_angle_acc -= FIRING_ANGLE_ACC_INC
    if key == simplegui.KEY_MAP['left']:
        firing_angle_acc += FIRING_ANGLE_ACC_INC
    
# define draw handler
def draw(canvas):
    global firing_angle, a_bubble, bubble_stuck, firing_angle_vel, firing_angle_acc
    
    # update firing angle
    firing_angle_vel += firing_angle_acc
    firing_angle_vel = 0.9 * firing_angle_vel
    if 0 < firing_angle + firing_angle_vel < math.pi:
        firing_angle += firing_angle_vel
        
    # draw firing line
    upper_point = [FIRING_POSITION[i] - FIRING_LINE_LENGTH * angle_to_vector(firing_angle)[i] for i in range(0,2)]
    canvas.draw_line(FIRING_POSITION, upper_point, 4, "White")
    
    # update a_bubble and check for sticking
    a_bubble.update()
    # draw a bubble and stuck bubbles
    a_bubble.draw(canvas)
   
 
# create frame and register handlers
frame = simplegui.create_frame("Bubble Shooter", WIDTH, HEIGHT)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# create initial buble and start frame
frame.start()

a_bubble = Bubble()
