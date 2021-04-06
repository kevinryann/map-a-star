import geopy
from geopy.geocoders import Nominatim

locator = Nominatim(user_agent="myGeocoder")

with open("../test/input.txt", "w") as file: # Clear txt file
    file.writelines("")

with open("./coordinate/coordinate.txt", "r") as file : # Opening coordinate.txt in read mode
    coordinates = file.read().split("\n") # Splitting coordinates.txt by lines
    for i in range(len(coordinates)-1) : # Print the list of coordinates
        location = locator.reverse(coordinates[i])
        print("%d. %s" % (i+1, location.address))
    
    # Initializing adjacency matrix of size N * N 
    matriks = [[0 for i in range(len(coordinates)-1)] for j in range(len(coordinates)-1)]

    # Loop to build routes
    while(True) :
        masukan = input("Masukkan route yang ingin dihubungkan ('Point1' 'Point2'): ") # Read Input

        if masukan == "-99" : # Stop condition
            break
        indexes = masukan.split(" ")
        
        try: # Handling error inputs (index out of bounds)
            matriks[int(indexes[0])-1][int(indexes[1])-1] = 1
            matriks[int(indexes[1])-1][int(indexes[0])-1] = 1
        except:
            print("Sepertinya ada yang salah dengan inputnya")

with open ("../test/input.txt", "a") as file: # Open input.txt in append mode
    file.writelines("%d\n" % (len(coordinates)-1)) # Write N
    for i in range (len(coordinates)-1): # Write all the coordinates
        file.writelines("%s\n" % coordinates[i])
    
    for i in range(len(coordinates)-1) : # Write the adjacency matrix
        for j in range(len(coordinates)-1) :
            file.writelines("%d " % matriks[i][j])
        if i != len(coordinates)-2:
            file.writelines("\n")

print("Memasukkan matriks terbaru ke input.txt") # Success message