import point

listPoints = []

def pointInList(point, listPoint) :
    if not(any(listPoint)) :
        return False
    for elmt in listPoint :
        if point.x == elmt.x and point.y == elmt.y :
            return True
    return False

def findClass(point, listPoint) :
    if not(any(listPoint)) :
        return False
    for elmt in listPoint :
        if point.x == elmt.x and point.y == elmt.y :
            return elmt
    return None

with open("../test/input1.txt", "r") as file :
    while True :
        # Read line
        line = file.readline()
        if not line :
            break

        tmpListCoordinates = line.replace("\n","").split(";")
        
        # Coordinate 1
        coordinate1 = tmpListCoordinates[0].split(",")
        tmppoint = point.point(int(coordinate1[0]), int(coordinate1[1]))
        if pointInList(tmppoint, listPoints) :
            point1 = findClass(tmppoint, listPoints)
            point1.printPoint()
        else :
            point1 = point.point(int(coordinate1[0]), int(coordinate1[1]))
            point1.printPoint()

        # Coordinate 2
        coordinate2 = tmpListCoordinates[1].split(",")
        tmppoint = point.point(int(coordinate2[0]), int(coordinate2[1]))
        if pointInList(tmppoint, listPoints) :
            point2 = findClass(tmppoint, listPoints)
            point2.printPoint()
        else :
            point2 = point.point(int(coordinate2[0]), int(coordinate2[1]))
            point2.printPoint()

        if not(pointInList(point1, listPoints)) :
            listPoints.append(point1)

        if not(pointInList(point2, listPoints)) :
            listPoints.append(point2)
        
        if not(pointInList(point2, point1.route)) :
            point1.addRoute(point2)
        
        if not(pointInList(point1, point2.route)) :
            point2.addRoute(point1)

for elmt in listPoints :
    elmt.printPoint()
    print ("Route : ", end="")
    for elmt2 in elmt.route :
        print(elmt2.x, end = ",")
        print(elmt2.y, end = ";")
    print()
