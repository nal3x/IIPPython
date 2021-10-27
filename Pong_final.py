# Pong!!!

import simplegui
import random

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
PAD_VELOCITY = 240 #in pixels per second
VEL_INCREASE_ON_STRIKE = 1.1 #10% increase


def spawn_ball(direction):
    """
    Ball position is initialized to the center of the canvas.
    The initial velocity of the ball is randomized: x value 
    in the range (120, 240) and y value in (60, 180) pixels/s.
    Finally, ball is spawned according to the direction value.
    """
    global ball_pos, ball_vel
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
     
    init_ball_vel_x = random.randrange(120, 240) / 60.0
    init_ball_vel_y = random.randrange(60, 180) / 60.0   
    
    if direction == RIGHT:
        ball_vel = [init_ball_vel_x, -init_ball_vel_y]
    elif direction == LEFT:
        ball_vel = [-init_ball_vel_x, -init_ball_vel_y]
        
def new_game():
    """
    When a new game is started, the paddles are centered, 
    their velocity becomes 0 and scores are zeroed. Random.range
    spawns the ball either to the left or to the right 
    (50% chance).
    """
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2
    
    paddle1_pos = paddle2_pos = (HEIGHT - 1) / 2
    paddle1_vel = paddle2_vel = 0
    
    score1 = score2 = 0
        
    spawn_ball(random.randrange(0,2)) 

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # ball collision top or bottom
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        
    # ball collision left & right 
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH: #left gutter check
        if ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT: #left paddle check
            ball_vel[0] = -VEL_INCREASE_ON_STRIKE * ball_vel[0]
        else:
            spawn_ball(RIGHT)
            score2 += 1 #right player wins
    
    if ball_pos[0] >= (WIDTH - 1) - PAD_WIDTH - BALL_RADIUS: #right gutter check 
        if ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT: #right paddle check
            ball_vel[0] = -VEL_INCREASE_ON_STRIKE * ball_vel[0]
        else:
            spawn_ball(LEFT)
            score1 += 1 #left player wins
        
    # update paddle's vertical position, keep paddle on screen
    if paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT :
        paddle1_pos += paddle1_vel
    if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT :
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    
    # draw scores
    canvas.draw_text(str(score1), [(1.0 / 4.0) * WIDTH, (1.0 / 4.0) * HEIGHT], 40, "White", "monospace")
    canvas.draw_text(str(score2), [(3.0 / 4.0) * WIDTH, (1.0 / 4.0) * HEIGHT], 40, "White", "monospace")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -PAD_VELOCITY / 60.0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = PAD_VELOCITY / 60.0
    
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -PAD_VELOCITY / 60.0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = PAD_VELOCITY / 60.0
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

def Restart():
    """
    Restart button handler
    """
    new_game()
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", Restart, 100)

# start frame
new_game()
frame.start()