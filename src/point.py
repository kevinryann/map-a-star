import math

class point : # Initializing class point
    def __init__(self, x, y): # Constructor
        self.x = x
        self.y = y
        self.route = []

    def euclideanDistance(self, point2) :
        R = 6373.0 # Radius of the earth (in km)

        # Converting coordinates to radians
        lat1 = math.radians(float(self.x)) 
        lon1 = math.radians(float(self.y))
        lat2 = math.radians(float(point2.x))
        lon2 = math.radians(float(point2.y))

        # Calculate longitude and latitude distance
        dlon = lon2 - lon1
        dlat = lat2 - lat1

        # Executing Haversine Formula
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c

        # Return distance
        return distance
        
    def addRoute(self, point) : # Add point to routes list
        self.route.append(point)
    
    def printPoint(self) :
        print("(%f,%f)" % (self.x, self.y)) # Print coordinate

    def isSame(self, point2):
        return self.x == point2.x and self.y == point2.y # Checks if 2 points are the same