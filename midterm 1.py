#question 1: examples

class Point:
    def __init__(self, x, y):          # magic (__init__)
        self.x = x
        self.y = y

    def distance_orig(self):           # regular method
        return (self.x**2 + self.y**2) ** 0.5

    def __str__(self):                 # magic (__str__)
        return f"point({self.x}, {self.y})"
