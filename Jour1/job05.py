class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def afficher(self):
        print(self.x)
        print(self.y)
    def modifier(self, x, y):
        self.x = x
        self.y = y
        print(x)
        print(y)

points = Point(4, 8)
points.afficher()
points.modifier(14, 85)