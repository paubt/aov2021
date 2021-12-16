import sys
import time

import numpy as np

from queue import PriorityQueue

def printCameFrom(cameFrom):
    for row in cameFrom:
        for point in row:
            print(f"{point[0]}|{point[1]} ", end="")
        print()


def printScore(gScore):
    for row in gScore:
        for element in row:
            print(f"{element} ", end="")
        print()


def part1(riskScore):
    startx, starty = 0, 0
    endRow, endColumn = len(riskScore) - 1, len(riskScore[0]) - 1

    # A* algorithm
    # h() is the manhatten (taxi) distance from point n to end
    def h(row, column):
        return (endRow - row) + (endColumn - column)

    # helper function that returns all  the neighbours as a list (row, col)
    def neighboursList(row, column):
        neighbours = []
        # add points above
        if row > 0:
            neighbours.append((row - 1, column))
        # add middle points
        if column > 0:
            neighbours.append((row, column - 1))
        if column < endColumn:
            neighbours.append((row, column + 1))
        # add bottom
        if row < endRow:
            neighbours.append((row + 1, column))
        return neighbours

    # helper function to check if a point is already in the queue
    def checkIfInQueue(row, column):
        tempPrioQueue = PriorityQueue()
        found = False
        while not openQueue.empty():
            fS, (r, c) = openQueue.get()
            if r == row and c == column:
                found = True
            tempPrioQueue.put((fS, (r, c)))
        return tempPrioQueue, found

    # reconstruct path
    def reconstructPath(row, column):
        totalPath = f"{row}|{column} "
        while row != 0 or column != 0:
            row, column = cameFrom[row,column, 0], cameFrom[row,column, 1]
            totalPath += f"{row}|{column} "
        return totalPath


    # openSet is a priority Queue that stores all the points that still need to be explored
    # it is saved as a (f, (x,y)) where p is the fScore (the priority) and (x,Y) the corresponding coordinates
    openQueue = PriorityQueue()

    # cameFrom is a map where (x,y) -> (x,y) for each tuple the tuple it came from is recorded
    cameFrom = np.zeros((len(riskScore), len(riskScore[0]), 2), dtype=int)
    cameFrom[0, 0, 1] = 123

    # gScore() is a map (x,y) -> gScore that records the cheapest path from start to the point (x,Y) currently known
    gScore = np.full((len(riskScore), len(riskScore[0])), sys.maxsize)
    # set start to Zero
    gScore[0, 0] = 0

    # fScore() is a map (x,y) -> fScore that holds the sum of gScore() and h() for each point
    # the sum of the cheapest cost to travel to a point plus the minimal cost from this point to the end
    fScore = np.full((len(riskScore), len(riskScore[0])), sys.maxsize)
    # set start to h() cause gScore()==0 and fScore = h() + gScore()
    fScore[0, 0] = h(0, 0)

    # put the start into the openQueue with the fScore as its priority
    # note: the priority doesn't really matter but is added for logical consistency
    openQueue.put((fScore[0, 0], (0, 0)))

    while not openQueue.empty():
        # get the next element from the priorityQueue this is also the one with the lowest fScore cause fScore==Priority
        currentFScore, (currentRow, currentColumn) = openQueue.get()
        print(currentFScore, currentRow, currentColumn)
        # check if current is the end point
        if currentRow == endRow and currentColumn == endColumn:
            # return the fScore
            # print(reconstructPath(currentRow,currentColumn))
            return fScore[currentRow, currentColumn]
        # for each neighbour of the current point
        # currentRow, Current
        for neighbourRow, neighbourColumn in neighboursList(currentRow, currentColumn):
            # the gScore from the current, plus the risk value at the new position
            tentativeGScore = gScore[currentRow, currentColumn] + riskScore[neighbourRow, neighbourColumn]
            #print(f"{neighbourRow}|{neighbourColumn} = {tentativeGScore}")
            # if tentativeGScore is better than the one currently stored
            # ergo this is a better/cheaper path to this point
            if tentativeGScore < gScore[neighbourRow,neighbourColumn]:
                # set the current point as cameFrom for this neighbour
                cameFrom[neighbourRow, neighbourColumn, 0] = currentRow
                cameFrom[neighbourRow, neighbourColumn, 1] = currentColumn
                # set the new gScore
                gScore[neighbourRow, neighbourColumn] = tentativeGScore
                # calculate the fScore for the element
                fScore[neighbourRow, neighbourColumn] = tentativeGScore + h(neighbourRow, neighbourColumn)
                # get if the neighbour is allready in the priority list of openQueue
                openQueue, found = checkIfInQueue(neighbourRow, neighbourColumn)
                if not found:
                    openQueue.put((fScore[neighbourRow, neighbourColumn],(neighbourRow,neighbourColumn)))


def part2(riskScore):
    # horizontal expanded riskScore array
    hRiskScore = riskScore.copy()
    # add 4 arrays with increments to the right
    for x in range(1,5):
        tempArray = np.zeros((len(riskScore), len(riskScore[0])), dtype=int)
        for r in range(len(riskScore)):
            for c in range(len(riskScore[0])):
                if riskScore[r, c] + x > 9:
                    tempArray[r, c] = ((riskScore[r, c] + x) % 10) + 1
                else:
                    tempArray[r, c] = riskScore[r, c] + x
        hRiskScore = np.concatenate((hRiskScore, tempArray), axis=1)
    # vertical expanded arrray
    vRiskScore = hRiskScore.copy()
    # add 4 arrays with increments to the bottom
    for x in range(1, 5):
        tempArray = np.zeros((len(hRiskScore), len(hRiskScore[0])), dtype=int)
        for r in range(len(hRiskScore)):
            for c in range(len(hRiskScore[0])):
                if hRiskScore[r, c] + x > 9:
                    tempArray[r, c] = ((hRiskScore[r, c] + x) % 10) + 1
                else:
                    tempArray[r, c] = hRiskScore[r, c] + x
        vRiskScore = np.concatenate((vRiskScore, tempArray), axis=0)
    # with the expanded RiskScore array call part1
    return part1(vRiskScore)

if __name__ == "__main__":
    # read in input and transform in int 2d array
    f = np.genfromtxt("data/real/input.csv", dtype=str)
    riskScore = np.zeros((len(f), len(f[0])), dtype=int)
    for row in range(len(f)):
        for column in range(len(f[0])):
            riskScore[row, column] = int(f[row][column])
    """
    # part 1
    begin = time.time()
    fS = part1(riskScore)
    end = time.time()
    print(f"part1 lowest risk path is {fS} with {end-begin} sec needed for computation")
    """
    # part 2
    begin= time.time()
    fS = part2(riskScore)
    end = time.time()
    print(f"part2 lowest risk path is {fS} with {end-begin} sec needed for computation")
