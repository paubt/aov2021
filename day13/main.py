from pprint import pprint

import numpy as np
import other


def part12():
    testOrReal = "test"
    points = np.genfromtxt(f"data/{testOrReal}/points.csv", delimiter=",", dtype=int)
    folds = np.genfromtxt(f"data/{testOrReal}/folds.csv", delimiter=" ", dtype=str)

    # safe folds axis and index in a 2d list
    temp = []
    for row in folds:
        axis, index = row[2].split("=", 2)
        temp.append([axis, int(index)])
    folds = temp

    # calculate the max values
    maxX = 0
    maxY = 0
    for x, y in points:
        if x > maxX:
            maxX = x
        if y > maxY:
            maxY = y
    print(f"maxX ={maxX} maxY = {maxY}")

    # use the max values to create a numpy zero array and put the points in as 1
    transparentPaper = np.zeros([maxY + 1, maxX + 1])
    # put in the points
    for x, y in points:
        transparentPaper[y, x] = 1

    # folds bottom part up
    def foldY(y):
        for row in transparentPaper[:y]:
            for element in row:
                print(f"{int(element)} ", end="")
            print()
        for x in range(len(transparentPaper[0])):
            print("- ", end="")
        print()
        # flip the bottom part
        bottomPart = np.copy(transparentPaper[y + 1:])
        for row in bottomPart:
            for element in row:
                print(f"{int(element)} ", end="")
            print()
        print("flip")
        bottomPart = np.flip(bottomPart, axis=0)
        for row in bottomPart:
            for element in row:
                print(f"{int(element)} ", end="")
            print()
        # iterate through both at the same time and put OR in the bot Part
        for row in range(len(bottomPart)):
            for col in range(len(bottomPart[0])):
                if transparentPaper[row, col] == 1:
                    bottomPart[row, col] = 1
        print("after fold")
        for row in bottomPart:
            for element in row:
                print(f"{int(element)} ", end="")
            print()
        return bottomPart

    def foldX(x):
        # flip the bottom part
        rightPart = np.copy(transparentPaper[:, x + 1:])
        for row in range(len(rightPart)):
            for colLeft in transparentPaper[row, :x]:
                print(f"{int(colLeft)} ", end="")
            print("| ", end="")
            for colRight in rightPart[row]:
                print(f"{int(colRight)} ", end="")
            print()

        print("flip")
        rightPart = np.flip(rightPart, axis=1)
        for row in rightPart:
            for element in row:
                print(f"{int(element)} ", end="")
            print()

        # iterate through both at the same time and put OR in the bot Part
        for row in range(len(rightPart)):
            for col in range(len(rightPart[0])):
                if transparentPaper[row, col] == 1:
                    rightPart[row, col] = 1
        print("after fold")
        for row in rightPart:
            for element in row:
                print(f"{int(element)} ", end="")
            print()
        return rightPart

    # iterate through the fold list
    for axis, index in folds:
        if axis == 'x':
            transparentPaper = foldX(index)
        else:
            transparentPaper = foldY(index)

    print(np.sum(transparentPaper))
    for row in transparentPaper:
        for c in row:
            if int(c) == 0:
                c = " "
            else:
                c = "x"
            print(f"{c} ", end="")
        print()


if __name__ == "__main__":
    part12()
    other.main()
