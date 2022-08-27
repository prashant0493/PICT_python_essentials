class Point:

    style = "fun"

    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(10, 10)

print(p1.x)

print(Point.style)
