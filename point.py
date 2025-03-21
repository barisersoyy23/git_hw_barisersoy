class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
print(p, "mesafesi:", p.distance_to_origin())
