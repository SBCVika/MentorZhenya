import random
import time
from math import sqrt


#  Task - many objects: find all collided object in 2-dimensional surface, use radius and coords for computation

class Circle:
    def __init__(self, radius, coords):
        self._radius = radius
        self._coords = coords

    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self, value):
        assert isinstance(value, (list, tuple)) and all(type(v) is int for v in value) , \
            "Coords should be tuple(int or float) with 2 elements"
        self._coords = value

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        assert isinstance(value, (int, float)), "Radius should be int or float"
        self._radius = value

    def collided(self, other):
        return (self - other) < (self.radius + other.radius)

    def __sub__(self, other):
        x1, y1 = other.coords
        x, y = self.coords
        return sqrt((y1 - y) ** 2 + (x1 - x) ** 2)

    def __hash__(self):
        return hash(self.data)

    def __eq__(self, other):
        return (self.radius, self.coords) == (other.radius, other.coords)

    def __repr__(self):
        return f'(Circle - {self.radius} | {self.coords})'

# Magic methods

circles = []
# area 0,0 - 100, 100

for _ in range(200):
    x, y, r = random.randint(0, 100), random.randint(0, 100), random.randint(0, 10)
    circles.append(Circle(r, (x, y)))

set_circles = set(circles)
for c in circles:
    for c1 in circles:
        if c != c1 and c.collided(c1):
            set_circles.discard(c)
            set_circles.discard(c1)

for c in set_circles:
    print(c)



class Field:
    def __init__(self):
        self._circles # random generated

    def run(self, number_iteration=500):
        # run the game until all circles collided
        # each period of move all circles randomly x e [-1,0,1]  y e [-1, 0, 1] etc
        # if they are collided - destroy both
        # output circles that are left in 500 iterations
        # print when Circle collided  ------ USE __del__ method !!

# 0, 0, 100, 100
