import math

"""
Moon
====
-Z is North
+Z is South
+X is West
-X is East
"""

class Compass(object):
    world = 'Moon'
    compass_offset = 0

    def __init__(self, world):
        self.world = world
        
    @staticmethod
    def distance(start, finish):
        delta_x = abs(start[0]-finish[0])
        delta_y = abs(start[1]-finish[1])
        distance = (math.sqrt((delta_x*delta_x)+(delta_y*delta_y)))
        return distance

    def bearing(self, position, target):
        a = math.atan2(position[0]-target[0], position[1]-target[1])
        if(a<0):
            b = a+ (math.pi + math.pi)
        else:
            b = a
        bearing = math.degrees(b)

        return bearing
