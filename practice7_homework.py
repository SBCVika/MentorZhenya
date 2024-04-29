import random
import math
from math import sqrt
import json
from scipy.spatial import KDTree


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
        self.children = []  # Initialize connections
        self.eat_count = 0  # Number of circles this circle can eat

    @property
    def x(self):
        return self._coords[0]

    @property
    def y(self):
        return self._coords[1]

    @property
    def r(self):
        return self._radius

    def find_children(self, all_circles):
        # Convert the set to a list to allow indexing
        all_circles_list = list(all_circles)

        # Build a k-d tree using all circles' coordinates
        coords = [circle._coords for circle in all_circles_list]
        kd_tree = KDTree(coords)

        # Query the k-d tree to find potential neighbors within the possible range
        potential_indices = kd_tree.query_ball_point(self._coords, self._radius*2)
        potential_neighbors = [all_circles_list[i] for i in potential_indices]

        # Determine children circles that can be eaten
        eatable_neighbors = []
        for neighbor in potential_neighbors:
            if neighbor != self and self.can_eat(neighbor) and neighbor not in eatable_neighbors:
                self.children.append(neighbor)
                eatable_neighbors.append(neighbor)

        # Update eat_count based on the number of eatable neighbors
        self.eat_count = len(eatable_neighbors)

        # Build a k-d tree for eatable neighbors
        if eatable_neighbors:
            eatable_coords = [circle._coords for circle in eatable_neighbors]
            eatable_kd_tree = KDTree(eatable_coords)
            return eatable_kd_tree
        else:
            return None  # No eatable neighbors


    def can_eat(self, other):
        distance = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return self.r > other.r and distance <= self.r - other.r

    def update_eat_count(self):
        self.eat_count = sum(child.update_eat_count() for child in self.children) + len(self.children)
        return self.eat_count

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
        self._coords = (self._coords[0] + other[0], self._coords[1] + other[1])


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
            r = random.randint(50, 200)
            circles.append(Circle(r, (x, y)))
        return set(circles)

    def move_all(self):
        for c in self._circles:
            dx = random.randint(-1, 1)
            dy = random.randint(-1, 1)
            x, y = c._coords
            c._coords = (max(-self.field_size, min(self.field_size, x + dx)),
                         max(-self.field_size, min(self.field_size, y + dy)))


class CircleForest:
    def __init__(self, circles):
        self.circles = list(circles)
        self.trees = {}  # Dictionary to hold each circle's k-d tree

    def build_forest(self):
        # Sort circles by radius in descending order
        self.circles.sort(key=lambda c: c._radius, reverse=True)
        for circle in self.circles:
            kd_tree = circle.find_children(self.circles)
            if kd_tree is not None:
                self.trees[circle] = kd_tree

    def get_trees(self):
        return self.trees

    def __repr__(self):
        return f"CircleForest with {len(self.circles)} circles"


if __name__ == '__main__':
    f1 = Field()

    # Create the CircleForest
    forest = CircleForest(f1._circles)

    # Build the forest (all k-d trees)
    forest.build_forest()

    # Output the k-d trees for each circle
    max_eated = 0

    for circle, tree in forest.get_trees().items():
        print(f"Circle at {circle._coords} with radius {circle._radius} can eat {circle.eat_count} circles:")
        print(f"The k-d tree for this circle has {len(tree.data)} eatable members:")

    # Print all members (coordinates) of the k-d tree
        for coords in tree.data:
            print(f"    Member at {coords}")

        if circle.eat_count > max_eated:
            max_eated = circle.eat_count
    print(f" max eated =  {max_eated}. \n")