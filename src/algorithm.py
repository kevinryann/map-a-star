import point

def aStar(start, end):
    path = [start]
    cost = 0
    findCost = []
    curr = start
    found = True

    while (not curr.isSame(end)):
        adjacent = [i for i in curr.route]
        if not any(adjacent):
            found = False
            break

        for adjacentPoints in adjacent:
            if adjacentPoints not in path:
                if len(path) == 1:
                    tmpCost = adjacentPoints.euclideanDistance(end) + adjacentPoints.euclideanDistance(curr)    
                else:
                    tmpCost = adjacentPoints.euclideanDistance(end) + cost
                
                findCost.append(tmpCost)
        
        minIdx = findCost.index(min(findCost))
        cost = findCost[minIdx]
        path.append(adjacent[minIdx])
        curr = adjacent[minIdx]
        
        findCost.clear()

    if found:
        return path
    return [start]