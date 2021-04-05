with open("coordinate.txt", "r") as file :
    coordinates = file.read().split("\n")
    for i in range(len(coordinates)) :
        print("%d. %s" % (i, coordinates[i]))
    
    matriks = [[0 for i in range(len(coordinates))] for j in range(len(coordinates))]

    masukan = "0"
    while(True) :
        masukan = input("Masukkan route : ")
        if masukan == "-99" :
            break
        indexes = masukan.split(" ")
        matriks[int(indexes[0])][int(indexes[1])] = 1

for i in range(len(coordinates)) :
    for j in range(len(coordinates)) :
        print (matriks[i][j], end = " ")
    print()

print("Copy matriks dan paste ke file input")