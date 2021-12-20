import time


def main():
    targetXWest = 29
    targetXEast = 73
    targetYNorth = -194
    targetYSouth = -248

    constTopY = 1000

    foundPositionList = []

    def checkIfCombiHits(vX, vY):
        highestY = 0
        currentX = 0
        currentY = 0
        while currentX <= targetXEast and currentY >= targetYSouth:
            currentX += vX
            currentY += vY
            if currentY > highestY:
                highestY = currentY
            if vX < 0:
                vX += 1
            elif vX > 0:
                vX -= 1
            vY -= 1
            # check if found
            if targetXWest <= currentX <= targetXEast and targetYSouth <= currentY <= targetYNorth:
                foundPositionList.append((vX, vY))
                return True, highestY
        return False, highestY

    def findBestVYGivenVX(vX):
        currentBestVY = 0
        currentBestHeight = 0
        found = True
        foundCounter = 0
        # iterate overall possible vY's
        for possibleVY in range(targetYSouth, constTopY):
            f, height = checkIfCombiHits(vX, possibleVY)
            if f:
                foundCounter += 1
            if f and height > currentBestHeight:
                currentBestVY = possibleVY
                currentBestHeight = height
                found = True
        return found, currentBestHeight, (vX, currentBestVY), foundCounter

    def findBestVX():
        currentBestVs = (0, 0)
        currentBestHeight = 0
        found = False
        foundCounter = 0
        for possibleVX in range(targetXEast+3):
            f, height, vs, fC = findBestVYGivenVX(possibleVX)
            if f:
                found += fC
            if f and height > currentBestHeight:
                currentBestVs = vs
                currentBestHeight = height
                found = True
        return found, currentBestHeight, currentBestVs, foundCounter

    begin = time.time()
    print(findBestVX())
    print(time.time() - begin)
    print(len(foundPositionList))



if __name__ == "__main__":
    main()
