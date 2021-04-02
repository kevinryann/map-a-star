
def writeText(longitude, latitude) :
    with open("../coordinate.txt",'w') as file :
        file.writelines("%f, %f" % (longitude, latitude))