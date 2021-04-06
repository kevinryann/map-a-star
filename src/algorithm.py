import point

def aStar(start, end):
    path = [start] # initialize path that will be used
    pathCost = []
    curr = start # initialize the current path to be the starting point
    found = True # used if there's no path to be found
    visited = [start] # for backtracking purposes

    while (not curr.isSame(end)): # loop until the current point = end point
        adjacent = [x for x in curr.route if x not in visited and x not in path] # list of adjacent points
        findCost = [(99999*99999) for y in range(len(adjacent))] # array that will be filled with the distance between 2 points, the number 99999*99999 is used to avoid big distance numbers
        if not any(adjacent): # if adjacent is empty
            visited.append(path[len(path)-1]) # to state that the point can no longer be used
            path.pop() # remove the path that can't be used anymore
            if len(path) != 0: # if there might still be a way
                pathCost.pop()
                curr = path[len(path)-1]
                continue # go back to the start of the loop
            found = False # to indicate there aren't any paths
            break # end the loop

        for adjacentPoints in adjacent: # get ajdacent point in adjacent
            tmpCost = adjacentPoints.euclideanDistance(end) + adjacentPoints.euclideanDistance(curr) # temp cost = distance between adjacent point and end point + distance between ajacent point and current point
            findCost[adjacent.index(adjacentPoints)] = tmpCost # to set the distances of temp cost based on the index of the adjacent point that was used to calculate temp cost

        minIdx = findCost.index(min(findCost)) # to find the minimum distance in findCost
        pathCost.append(findCost[minIdx])
        path.append(adjacent[minIdx]) # add point that has the minimum distance to path
        curr = adjacent[minIdx] # set current point to point that has the minimum distance
        
    if found: # if the path between start point and end point exists
        print("Jarak :", sum(pathCost), "km") # print the distance between start point and end point
        return path # return the path
    print("Tidak ada jalan yang terbentuk")
    return [start] # return only start point