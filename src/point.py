import math

class point :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.route = []

    def euclideanDistance(self, point2) :
        return math.sqrt((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2)

    def addRoute(self, point) :
        self.route.append(point)
    
    def printPoint(self) :
        print("(%d,%d)" % (self.x, self.y))