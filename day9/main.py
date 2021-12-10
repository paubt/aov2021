import numpy as np

global visitedSpots
global crabs

def part1():
    crabs = np.genfromtxt("./data/real/input.csv", delimiter=",", dtype=str)
    width = len(crabs[0])
    height = len(crabs)
    print(f"width = {width} and height = {height}")
    print(crabs)
    # list of low points
    lowPointsList = list()
    riskLevel = 0
    # top row
    # do top left corner (check SW)
    if crabs[0][0] < crabs[1][0] and crabs[0][0] < crabs[0][1]:
        riskLevel += 1 + int(crabs[0][0])
    # go through top row without the corners (SEW)
    for x in range(1, width - 1):
        if crabs[0][x] < crabs[0][x - 1] and crabs[0][x] < crabs[0][x + 1] and crabs[0][x] < crabs[1][x]:
            riskLevel += 1 + int(crabs[0][x])
    # do top right corner (SE)
    if crabs[0][width - 1] < crabs[1][width - 1] and crabs[0][width - 1] < crabs[0][width - 1 - 1]:
        riskLevel += 1 + int(crabs[0][width - 1])
    # middle rows
    # go through the middle rows with a special case only on the beginnings and ends
    for r in range(1, height - 1):
        # check if first element of the row is a sink (check NSW)
        if crabs[r][0] < crabs[r - 1][0] and crabs[r][0] < crabs[r + 1][0] and crabs[r][0] < crabs[r][1]:
            riskLevel += 1 + int(crabs[r][0])
        # iterate in each row thought the elements without start and end (NWSE)
        for x in range(1, width - 1):
            if crabs[r][x] < crabs[r - 1][x] and crabs[r][x] < crabs[r][x + 1] and crabs[r][x] < crabs[r + 1][x] and \
                    crabs[r][x] < crabs[r][x - 1]:
                riskLevel += int(crabs[r][x]) + 1
        # check the last element of the rows (NSE)
        if crabs[r][width - 1] < crabs[r + 1][width - 1] and crabs[r][width - 1] < crabs[r - 1][width - 1] and crabs[r][
            width - 1] < crabs[r][width - 2]:
            riskLevel += 1 + int(crabs[r][width - 1])
    # do the bottom row
    # the bottom left corner (NW)
    if crabs[height - 1][0] < crabs[height - 2][0] and crabs[height - 1][0] < crabs[height - 1][1]:
        riskLevel += 1 + int(crabs[height - 1][0])
    # go through bottom row without the corners (NEW)
    for x in range(1, width - 1):
        if crabs[height - 1][x] < crabs[height - 2][x] and crabs[height - 1][x] < crabs[height - 1][x - 1] and \
                crabs[height - 1][x] < crabs[height - 1][x + 1]:
            riskLevel += 1 + int(crabs[height - 1][x])
    # do bottom right corner (NW)
    if crabs[height - 1][width - 1] < crabs[height - 2][width - 1] and crabs[height - 1][width - 1] < crabs[height - 1][
        width - 2]:
        riskLevel += 1 + int(crabs[height - 1][width - 1])
    print(f"riskLevel = {riskLevel}")


def part2():
    global crabs
    crabs = np.genfromtxt("./data/real/input.csv", delimiter=",", dtype=str)
    width = len(crabs[0])
    height = len(crabs)
    print(f"width = {width} and height = {height}")
    print(crabs)
    # list of low points
    lowPointsList = list()
    riskLevel = 0
    # top row
    # do top left corner (check SW)
    if crabs[0][0] < crabs[1][0] and crabs[0][0] < crabs[0][1]:
        riskLevel += 1 + int(crabs[0][0])
        lowPointsList.append([0, 0])
    # go through top row without the corners (SEW)
    for x in range(1, width - 1):
        if crabs[0][x] < crabs[0][x - 1] and crabs[0][x] < crabs[0][x + 1] and crabs[0][x] < crabs[1][x]:
            riskLevel += 1 + int(crabs[0][x])
            lowPointsList.append([0, x])

    # do top right corner (SE)
    if crabs[0][width - 1] < crabs[1][width - 1] and crabs[0][width - 1] < crabs[0][width - 1 - 1]:
        riskLevel += 1 + int(crabs[0][width - 1])
        lowPointsList.append([0, width - 1])
    # middle rows
    # go through the middle rows with a special case only on the beginnings and ends
    for r in range(1, height - 1):
        # check if first element of the row is a sink (check NSW)
        if crabs[r][0] < crabs[r - 1][0] and crabs[r][0] < crabs[r + 1][0] and crabs[r][0] < crabs[r][1]:
            riskLevel += 1 + int(crabs[r][0])
            lowPointsList.append([r, 0])
        # iterate in each row thought the elements without start and end (NWSE)
        for x in range(1, width - 1):
            if crabs[r][x] < crabs[r - 1][x] and crabs[r][x] < crabs[r][x + 1] and crabs[r][x] < crabs[r + 1][x] and \
                    crabs[r][x] < crabs[r][x - 1]:
                riskLevel += int(crabs[r][x]) + 1
                lowPointsList.append([r, x])
        # check the last element of the rows (NSE)
        if crabs[r][width - 1] < crabs[r + 1][width - 1] and crabs[r][width - 1] < crabs[r - 1][width - 1] and crabs[r][
            width - 1] < crabs[r][width - 2]:
            riskLevel += 1 + int(crabs[r][width - 1])
            lowPointsList.append([r, width - 1])
    # do the bottom row
    # the bottom left corner (NW)
    if crabs[height - 1][0] < crabs[height - 2][0] and crabs[height - 1][0] < crabs[height - 1][1]:
        riskLevel += 1 + int(crabs[height - 1][0])
        lowPointsList.append([height - 1, 0])
    # go through bottom row without the corners (NEW)
    for x in range(1, width - 1):
        if crabs[height - 1][x] < crabs[height - 2][x] and crabs[height - 1][x] < crabs[height - 1][x - 1] and \
                crabs[height - 1][x] < crabs[height - 1][x + 1]:
            riskLevel += 1 + int(crabs[height - 1][x])
            lowPointsList.append([height - 1, x])
    # do bottom right corner (NW)
    if crabs[height - 1][width - 1] < crabs[height - 2][width - 1] and crabs[height - 1][width - 1] < crabs[height - 1][
        width - 2]:
        riskLevel += 1 + int(crabs[height - 1][width - 1])
        lowPointsList.append([height - 1, width - 1])
    print(f"riskLevel = {riskLevel}")
    print(lowPointsList)

    # create a second array for already visited spots
    widthString = '0' * width
    global visitedSpots
    visitedSpots = np.zeros((height, width), dtype=int)
    print(visitedSpots)

    # list of size of basis's
    sizeList = list()
    # for each low point we recursive search until we find a 9 or a lower number
    for h, w in lowPointsList:
        size = searchSpot(h, w)
        sizeList.append(size)
        print(f"h={h} w={w} size={size}")
    print(sizeList)

    # top three list and already multiplied
    topSizeList = list()
    multiSize = 1
    # pick the 3 larges elements of the sizeList
    for i in range(0, 3):
        maxSize = 0
        maxIndex = 0
        for j in range(len(sizeList)):
            if sizeList[j] > maxSize:
                maxSize = sizeList[j]
                maxIndex = j
        # delete the the largest element from the
        del sizeList[maxIndex]
        topSizeList.append(maxSize)
        multiSize *= maxSize
    print(topSizeList)
    print(multiSize)



def searchSpot(h, w):
    # first set the current spot to visited
    global visitedSpots
    visitedSpots[h][w] = 1
    # length of the expanded path
    size = 0
    # expand to North if possible
    if h > 0 and visitedSpots[h-1][w] == 0 and int(crabs[h-1][w]) < 9:
        size += searchSpot(h-1, w)
    # expand to South if possible
    if h < len(visitedSpots)-1 and visitedSpots[h+1][w] == 0 and int(crabs[h+1][w]) < 9:
        size += searchSpot(h+1, w)
    # expand to East if possible
    if w > 0 and visitedSpots[h][w-1] == 0 and int(crabs[h][w-1]) < 9:
        size += searchSpot(h, w-1)
    # expand to West if possible
    if w < len(visitedSpots[0])-1 and visitedSpots[h][w+1] == 0 and int(crabs[h][w+1]) < 9:
        size += searchSpot(h, w+1)
    # return the size plus one
    return size + 1


if __name__ == "__main__":
    part2()
