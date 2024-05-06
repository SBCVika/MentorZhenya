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
        return hash((self.radius, self.coords))
    def __eq__(self, other):
        return (self.radius, self.coords) == (other.radius, other.coords)

    def __repr__(self):
        return f'(Circle - {self.radius} | {self.coords})'
#    def __del__(self):
#       print(f"{self.__hash__} is deleted.")
# Magic methods

class Field:
    FIELD_SIZE = 100
    circle_amount = 200
    def __init__(self, field_size, circle_amount):
        self.FIELD_SIZE = field_size
        self.CIRCLE_AMOUNT = circle_amount
        self._circles = self.generate_random_circles(circle_amount)

    def generate_random_circles(self, circle_amount):
        circles = []
        for _ in range(self.circle_amount):
            x = random.randint(-self.FIELD_SIZE, self.FIELD_SIZE)
            y = random.randint(-self.FIELD_SIZE, self.FIELD_SIZE)
            r = random.randint(0, 20)
            circles.append(Circle(r, (x, y)))
        return set(circles)

    def run(self):
        collided_circles = set()
        for c in self._circles:
            for c1 in self._circles:
                if c != c1 and c.collided(c1):
                    collided_circles.add(c)
                    collided_circles.add(c1)
        for c in collided_circles:
            del c  # Remove the reference to the object

        # Remove collided circles from the set after the loop
        self._circles -= collided_circles

    def move(self):
        for c in self._circles:
            dx = random.randint(-1, 1)
            dy = random.randint(-1, 1)
            x, y = c.coords
            c.coords = (max(-self.FIELD_SIZE, min(self.FIELD_SIZE, c.coords[0] + dx)),
                        max(-self.FIELD_SIZE, min(self.FIELD_SIZE, c.coords[1] + dy)))
if __name__ == '__main__':
    circles = []
    field_size = 100
    circle_amount = 200
    f1 = Field(field_size, circle_amount)

    for _ in range(500):
        f1.run()
        f1.move()

    for c in f1._circles:
        print(c)