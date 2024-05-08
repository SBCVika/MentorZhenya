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
        return hash(id(self))

    def __eq__(self, other):
        return (self.radius, self.coords) == (other.radius, other.coords)

    def __repr__(self):
        return f'(Circle - {self.radius} | {self.coords})'

    def shift(self, other):
        # other int to shift to
        self.coords = self.coords[0] + other[0], self.coords[1] + other[1]


def validate_positive_integer(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            argsi = args[1:]
            for i, arg in enumerate(argsi):  # Assuming the value is passed as the second argument
                if not isinstance(arg, types[i]) or arg < 0:
                    raise ValueError(f"{func.__name__.replace('_', ' ')} must be a positive integer")
            return func(*args, **kwargs)
        return wrapper
    return decorator


class Field:
    DEFAULT_FIELD_SIZE = config.d['field_size']
    DEFAULT_CIRCLES_AMOUNT = 200

    def __init__(self, field_size=DEFAULT_FIELD_SIZE , circles_amount=DEFAULT_CIRCLES_AMOUNT):
        self.field_size = field_size
        self.circles_amount = circles_amount
        self._circles = self.generate_random_circles(self.circles_amount)

    @property
    def field_size(self):
        return self._field_size

    @field_size.setter
    @validate_positive_integer(int)
    def field_size(self, value):
        self._field_size = value

    @property
    def circles_amount(self):
        return self._field_size

    @circles_amount.setter
    @validate_positive_integer(int)
    def circles_amount(self, value):
        self._circles_amount = value

    def generate_random_circles(self, circle_amount):
        circles = []
        for _ in range(circle_amount):
            x = random.randint(-self._field_size, self._field_size)
            y = random.randint(-self._field_size, self._field_size)
            r = random.randint(1, 20)
            circles.append(Circle(r, (x, y)))
        return set(circles)

    def run(self):
        collided_circles = set()
        for c in self._circles:
            for c1 in self._circles:
                if c != c1 and c.collided(c1):
                    collided_circles.add(c)
                    collided_circles.add(c1)

        # Remove collided circles from the set after the loop
        self._circles -= collided_circles
        print(len(self._circles), len(collided_circles))

    def move_all(self):
        for c in self._circles: # (1, (3,2)) (1, (1,3)) (1, (1,4))
            dx = random.randint(-1, 1)
            dy = random.randint(-1, 1)
            x, y = c.coords
            c.coords = (max(-self._field_size, min(self._field_size, c.coords[0] + dx)),
                        max(-self._field_size, min(self._field_size, c.coords[1] + dy)))


if __name__ == '__main__':
    circles = []
    f1 = Field()
    f1.field_size = 100  # Using setter method to update field_size
    f1.circles_amount = 200  # Using setter method to update circles_amount

    for _ in range(500):
        f1.run()
        f1.move_all()

    for c in f1._circles:
        print(c)