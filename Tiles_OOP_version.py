import simplegui
import random

TILE_WIDTH = 50
TILE_HEIGHT = 100
DISTINCT_TILES = 8

def new_game():
    global my_tiles, state, turns

    tile_numbers = range(DISTINCT_TILES) * 2
    random.shuffle(tile_numbers)
    my_tiles = [Tile(tile_numbers[i], False, [TILE_WIDTH * i, TILE_HEIGHT]) for i in range(2 * DISTINCT_TILES)]
    
    state = 0
    turns = 0
    label.set_text("Turns = "+str(turns))  

class Tile:
    
    # definition of intializer
    def __init__(self, num, exp, loc):
        self.number = num
        self.exposed = exp
        self.location = loc
        
    # definition of getter for number
    def get_number(self):
        return self.number
    
    # check whether tile is exposed
    def is_exposed(self):
        return self.exposed
    
    # expose the tile
    def expose_tile(self):
        self.exposed = True
    
    # hide the tile       
    def hide_tile(self):
        self.exposed = False
        
    # string method for tiles    
    def __str__(self):
        return "Number is " + str(self.number) + ", exposed is " + str(self.exposed)    

    # draw method for tiles
    def draw_tile(self, canvas):
        loc = self.location
        if self.exposed:
            text_location = [loc[0] + 0.2 * TILE_WIDTH, loc[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.number), text_location, TILE_WIDTH, "White")
        else:
            tile_corners = (loc, [loc[0] + TILE_WIDTH, loc[1]], [loc[0] + TILE_WIDTH, loc[1] - TILE_HEIGHT], [loc[0], loc[1] - TILE_HEIGHT])
            canvas.draw_polygon(tile_corners, 1, "Red", "Green")

    # selection method for tiles
    def is_selected(self, pos):
        inside_hor = self.location[0] <= pos[0] < self.location[0] + TILE_WIDTH
        inside_vert = self.location[1] - TILE_HEIGHT <= pos[1] <= self.location[1]
        return  inside_hor and inside_vert     

def mouseclick(pos):
    global state, turns, tile1, tile2
    
    for tile in my_tiles:
        if tile.is_selected(pos) and not tile.is_exposed():
            tile.expose_tile()
            if state == 0:
                tile1 = tile
                state = 1
            elif state == 1:
                tile2 = tile
                state = 2
                turns += 1
            else:
                if tile1.get_number() != tile2.get_number(): #fail closes previous tiles
                    tile1.hide_tile(), tile2.hide_tile()
                    tile1 = tile
                    state = 1
                else: 
                    tile1 = tile
                    state = 1
                    
def draw(canvas):
    label.set_text('Turns = ' + str(turns))
    for tile in my_tiles:
        tile.draw_tile(canvas)

frame = simplegui.create_frame("Memory", 2 * DISTINCT_TILES * TILE_WIDTH, TILE_HEIGHT)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)


new_game()
frame.start()