import random
from math import sqrt
import json

class Singleton(type):
    _instances = {}
    _config = None

    def __call__(cls, *args, **kwargs):
        if cls._config is None:
            with open("file.json") as f:
                cls._config = json.load(f)
        inst = cls._instances.get(cls.__name__, None)
        if inst is None:
            inst = super().__call__(*args, **kwargs)
            cls._instances[cls.__name__] = inst
        return inst

class Circle:
    def __init__(self, radius, coords):
        self._radius = radius
        self._coords = coords

    def collided(self, other):
        return (self - other) < (self._radius + other._radius)

    def __sub__(self, other):
        x1, y1 = other._coords
        x, y = self._coords
        return sqrt((y1 - y) ** 2 + (x1 - x) ** 2)

    def __hash__(self):
        return hash(id(self))

    def __eq__(self, other):
        return (self._radius, self._coords) == (other._radius, other._coords)

    def __repr__(self):
        return f'(Circle - {self._radius} | {self._coords})'

    def shift(self, other):
        self.coords = self.coords[0] + other[0], self.coords[1] + other[1]

class Field(metaclass=Singleton):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        field_config = self._config.get("field", {})  # Accessing nested key "field"
        self.field_size = field_config.get("field_size", None)
        self.circles_amount = field_config.get("number_circles", None)
        self._circles = self.generate_random_circles(self.circles_amount)

    def generate_random_circles(self, circle_amount):
        circles = []
        for _ in range(circle_amount):
            x = random.randint(-self.field_size, self.field_size)
            y = random.randint(-self.field_size, self.field_size)
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
        for c in self._circles:
            dx = random.randint(-1, 1)
            dy = random.randint(-1, 1)
            x, y = c._coords
            c._coords = (max(-self.field_size, min(self.field_size, x + dx)),
                        max(-self.field_size, min(self.field_size, y + dy)))

if __name__ == '__main__':
    f1 = Field()

    for _ in range(500):
        f1.run()
        f1.move_all()

    for c in f1._circles:
        print(c)