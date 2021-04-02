import point
import visualize
import algorithm

listPoints = []

def pointInList(point, listPoint) :
    for elmt in listPoint :
        if point.x == elmt.x and point.y == elmt.y :
            return True
    return False

def findPoint(point, listPoint) :
    for elmt in listPoint :
        if point.x == elmt.x and point.y == elmt.y :
            return elmt
    return None

with open("../test/input1.txt", 'r') as file :
    line = file.read()
    listLines = line.split("\n")

    lineCount = int(listLines[0])

    for i in range(1, 1 + lineCount) :
        tmpString = listLines[i].replace(' ','').split(",")
        tmpPoint = point.point(float(tmpString[0]), float(tmpString[1]))

        if (not(pointInList(tmpPoint, listPoints))):
            listPoints.append(tmpPoint)

    for i in range(1 + lineCount, 1 + 2 * lineCount) :
        tmpString = listLines[i].split(' ')

        for j in range(lineCount) :
            if tmpString[j] == "1" :
                if not(pointInList(listPoints[j], listPoints[i - 1 - lineCount].route)) :
                    listPoints[i - 1 - lineCount].addRoute(listPoints[j])

start = listPoints[0]
end = listPoints[0]






path = algorithm.aStar(start, end)
visualize.visualizee(listPoints, path, start, end)