with open("../test/input.txt", "w") as file:
    file.writelines("")

with open("./coordinate/coordinate.txt", "r") as file :
    coordinates = file.read().split("\n")
    for i in range(len(coordinates)-1) :
        print("%d. %s" % (i+1, coordinates[i]))
    
    matriks = [[0 for i in range(len(coordinates)-1)] for j in range(len(coordinates)-1)]

    masukan = "0"
    while(True) :
        masukan = input("Masukkan route yang ingin dihubungkan ('Route 1' 'Route 2'): ")
        if masukan == "-99" :
            break
        indexes = masukan.split(" ")
        try:
            matriks[int(indexes[0])-1][int(indexes[1])-1] = 1
            matriks[int(indexes[1])-1][int(indexes[0])-1] = 1
        except:
            print("Sepertinya ada yang salah dengan inputnya")

with open ("../test/input.txt", "a") as file:
    file.writelines("%d\n" % (len(coordinates)-1))
    for i in range (len(coordinates)-1):
        file.writelines("%s\n" % coordinates[i])
    
    for i in range(len(coordinates)-1) :
        for j in range(len(coordinates)-1) :
            # print (matriks[i][j], end = " ")
            file.writelines("%d " % matriks[i][j])
        if i != len(coordinates)-2:
            file.writelines("\n")
        # print()

print("Memasukkan matriks terbaru ke input.txt")