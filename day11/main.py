from pprint import pprint

import numpy as np

if __name__ == "__main__":
    grid = list(np.genfromtxt("./data/real/input.csv", delimiter=",", dtype=str))
    g = []
    for r in grid:
        tempRow = []
        for o in r:
            tempRow.append(int(o))
        g.append(tempRow)
    #print("start grid")
    #pprint(g)

    # counts the times the octopuses flashed
    flashCounter = 0
    newFlash = True
    stepCounter = 0
    while True:
        stepCounter += 1
        print(f"step nr {stepCounter}")
        # increment all by 1
        for r in range(10):
            for c in range(10):
                g[r][c] = g[r][c] + 1
        # repeat until
        newFlash = True
        while newFlash:
            newFlash = False
            # iterate through the grid
            # # first element in top left corner (NE)
            if g[0][0] >= 10:
                g[0][0] = 0
                flashCounter += 1
                newFlash = True
                if 0 < g[0][1] < 10:
                    g[0][1] += 1
                if 0 < g[1][0] < 10:
                    g[1][0] += 1
                if 0 < g[1][1] < 10:
                    g[1][1] += 1
            # top row without corners
            for o in range(1, 9):
                if g[0][o] >= 10:
                    g[0][o] = 0
                    flashCounter += 1
                    newFlash = True
                    # left and right
                    if 0 < g[0][o-1] < 10:
                        g[0][o-1] += 1
                    if 0 < g[0][o+1] < 10:
                        g[0][o+1] += 1
                    # bottom
                    if 0 < g[1][o] < 10:
                        g[1][o] += 1
                    # bottom left and right
                    if 0 < g[1][o-1] < 10:
                        g[1][o-1] += 1
                    if 0 < g[1][o+1] < 10:
                        g[1][o+1] += 1
            # the top right corner of (NW)
            if g[0][9] >= 10:
                g[0][9] = 0
                flashCounter += 1
                newFlash = True
                if 0 < g[0][8] < 10:
                    g[0][8] += 1
                if 0 < g[1][9] < 10:
                    g[1][9] += 1
                if 0 < g[1][8] < 10:
                    g[1][8] += 1
            # the middle rows
            for r in range(1, 9):
                # the most left/east beginning
                if g[r][0] >= 10:
                    g[r][0] = 0
                    flashCounter += 1
                    newFlash = True
                    # top and bot
                    if 0 < g[r-1][0] < 10:
                        g[r-1][0] += 1
                    if 0 < g[r+1][0] < 10:
                        g[r+1][0] += 1
                    # right/east
                    if 0 < g[r][1] < 10:
                        g[r][1] += 1
                    # right top and bot
                    if 0 < g[r-1][1] < 10:
                        g[r-1][1] += 1
                    if 0 < g[r+1][1] < 10:
                        g[r+1][1] += 1
                # the middle
                for c in range(1,9):
                    if g[r][c] >= 10:
                        g[r][c] = 0
                        flashCounter += 1
                        newFlash = True
                        # top- left, middle and right
                        if 0 < g[r-1][c-1] < 10:
                            g[r-1][c-1] += 1
                        if 0 < g[r-1][c] < 10:
                            g[r-1][c] += 1
                        if 0 < g[r-1][c+1] < 10:
                            g[r-1][c+1] += 1
                        # left and right
                        if 0 < g[r][c-1] < 10:
                            g[r][c-1] += 1
                        if 0 < g[r][c+1] < 10:
                            g[r][c+1] += 1
                        # bot left, middle and right
                        if 0 < g[r+1][c-1] < 10:
                            g[r+1][c-1] += 1
                        if 0 < g[r+1][c] < 10:
                            g[r+1][c] += 1
                        if 0 < g[r+1][c+1] < 10:
                            g[r+1][c+1] += 1
                # the last element / west-most
                if g[r][9] >= 10:
                    g[r][9] = 0
                    flashCounter += 1
                    newFlash = True
                    # top and bot
                    if 0 < g[r-1][9] < 10:
                        g[r-1][9] += 1
                    if 0 < g[r+1][9] < 10:
                        g[r+1][9] += 1
                    # right/east
                    if 0 < g[r][8] < 10:
                        g[r][8] += 1
                    # right top and bot
                    if 0 < g[r-1][8] < 10:
                        g[r-1][8] += 1
                    if 0 < g[r+1][8] < 10:
                        g[r+1][8] += 1
            # the bottom row
            # # first element in top left corner (NE)
            if g[-1][0] >= 10:
                g[-1][0] = 0
                flashCounter += 1
                newFlash = True
                if 0 < g[-1][1] < 10:
                    g[-1][1] += 1
                if 0 < g[-2][0] < 10:
                    g[-2][0] += 1
                if 0 < g[-2][1] < 10:
                    g[-2][1] += 1
            # top row without corners
            for o in range(1, 9):
                if g[-1][o] >= 10:
                    g[-1][o] = 0
                    flashCounter += 1
                    newFlash = True
                    # left and right
                    if 0 < g[-1][o - 1] < 10:
                        g[-1][o - 1] += 1
                    if 0 < g[-1][o + 1] < 10:
                        g[-1][o + 1] += 1
                    # top
                    if 0 < g[-2][o] < 10:
                        g[-2][o] += 1
                    # top left and right
                    if 0 < g[-2][o - 1] < 10:
                        g[-2][o - 1] += 1
                    if 0 < g[-2][o + 1] < 10:
                        g[-2][o + 1] += 1
            # the top right corner of (NW)
            if g[-1][9] >= 10:
                g[-1][9] = 0
                flashCounter += 1
                newFlash = True
                if 0 < g[-1][8] < 10:
                    g[-1][8] += 1
                if 0 < g[-2][9] < 10:
                    g[-2][9] += 1
                if 0 < g[-2][8] < 10:
                    g[-2][8] += 1
        print("\n after new Flash")
        pprint(g)

        allZeros = True
        for r in g:
            for c in r:
                if c != 0:
                    allZeros = False

        if allZeros:
            print(f"fund after {stepCounter} steps")
            break

    print(flashCounter)