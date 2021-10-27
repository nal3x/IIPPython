import math

def polygon_area(number_of_sides, side_length):
    
    """
    Calculates the area of a polygon given 
    the number of its sides and 
    the length of each sides.
    Uses the formula:
    1/4 n s^2 / tan(pi/n)
    """
    
    area = (1.0/4.0 * number_of_sides * side_length ** 2) / math.tan( math.pi / number_of_sides)
    return area

#self-test first -> area must be 84.3033926289

print polygon_area(5,7)

#calculation_after

print polygon_area(7,3)    