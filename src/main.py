import point
import visualize
import algorithm
from geopy.geocoders import Nominatim

locator = Nominatim(user_agent="myGeocoder")

# Check if a point is in a list. Returns boolean
def pointInList(point, listPoint) : # Checks if point is in listPoint
    for elmt in listPoint : # Iterating every element in listPoint
        if point.x == elmt.x and point.y == elmt.y : # Returns True if found
            return True
    return False # Returns False by default

# Find a point in a list. Returns object point
def findPoint(point, listPoint) : # Find point in listPoint
    for elmt in listPoint : # Iterating every element in listPoint
        if point.x == elmt.x and point.y == elmt.y : # Returns elmnt if found
            return elmt
    return None # Returns None by default

# Read file and initialize listPoints (a list with elements of all points in input file)
def read_file(file_name): # Read {file_name}.txt if located in test folder
    listPoints=[] # Initializing empty list

    with open("../test/" + file_name, 'r') as file : # Opening file
        line = file.read() # Reads the content of the text file
        listLines = line.split("\n") # Make a list with elements of each line in the text file

        lineCount = int(listLines[0]) # Initializing N

        for i in range(1, 1 + lineCount) : # Initializing every points and store it in listPoints
            tmpString = listLines[i].replace(' ','').split(",") # Remove spaces and split by , to get coordinates
            tmpPoint = point.point(float(tmpString[0]), float(tmpString[1])) # Construct point

            if (not(pointInList(tmpPoint, listPoints))): # Add point to list if listPoints doesn't contain the point
                listPoints.append(tmpPoint)

        # Initialize all routes
        for i in range(1 + lineCount, 1 + 2 * lineCount) : # Iterating every coordinate (2nd line to (2 + N)th line)
            tmpString = listLines[i].split(' ')

            for j in range(lineCount) : # Add to route if the element in adjacency matrix == 1
                if tmpString[j] == "1" :
                    if not(pointInList(listPoints[j], listPoints[i - 1 - lineCount].route)) : # Add to route if point hasn't been added
                        listPoints[i - 1 - lineCount].addRoute(listPoints[j])
    return listPoints # Returns listPoints

# Main program
print("1. Dari titik yang sudah dipilih di web")
print("2. Dari file")

choice = input("Pilihlah input yang akan digunakan : ")
if choice == "1":
    file_name = "input.txt"
else:
    file_name = input("Input file name: ")

# Handling the case where user did not input .txt extension
if ".txt" not in file_name:
    file_name += ".txt"
listPoints = read_file(file_name)

# Opening file
with open("../test/" + file_name, 'r') as file :
    line = file.read() # Read the content of the file
    listLines = line.split("\n") # Splitting by line

    linecount = int(listLines[0]) # Initializing N

    for i in range(1, 1+linecount) : # Prints addresses
        location = locator.reverse(listLines[i])
        print("%d. %s" %(i, location.address))

start_index = int(input("Masukkan titik asal : ")) # Input start coordinate
end_index = int(input("Masukkan titik tujuan : ")) # Input end coordinate

choice = "0"
while (choice != "2") :
    print("\n1. Visualisasi graf dalam bidang kartesian")
    print("2. Jalankan A* dan visualisasi")
    choice = input("Pilihan : ")
    if choice == "1" :
        visualize.visualize(listPoints) # Visualize graph
    elif choice == "2" :
        path = algorithm.aStar(listPoints[start_index-1], listPoints[end_index-1]) # Call the A* Algorithm
        visualize.visualizee(listPoints, path, listPoints[start_index-1], listPoints[end_index-1]) # Visualizing result into a map
        break
    else :
        print("Input salah")
