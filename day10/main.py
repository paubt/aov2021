import numpy as np


def part1():
    navSystem = np.genfromtxt("./data/real/input.csv", delimiter=",", dtype=str)
    # counter for the incomplete lines
    firstIllegalCharacterCounter = 0
    # open stack list
    opePStackList = []
    # line index to delete
    index = 0
    indexToDelete = []
    for line in navSystem:
        # stack for open parenthesis
        openPStack = []
        # iterate through the characters in a line
        for c in line:
            print(c, end=" ")
            # push the character on a stack if its a opener
            if c == '(' or c == '[' or c == '{' or c == '<':
                openPStack.append(c)
            if c == ')':
                # the correct open-close combination
                if openPStack[-1] == '(':
                    del openPStack[-1]
                else:
                    print("error here", end="")
                    firstIllegalCharacterCounter += 3
                    indexToDelete.append(index)
                    break
                    # check if
            if c == ']':
                # the correct open-close combination
                if openPStack[-1] == '[':
                    del openPStack[-1]
                else:
                    print("error here", end="")
                    firstIllegalCharacterCounter += 57
                    indexToDelete.append(index)
                    break
                    # check if
            if c == '}':
                # the correct open-close combination
                if openPStack[-1] == '{':
                    del openPStack[-1]
                else:
                    print("error here", end="")
                    firstIllegalCharacterCounter += 1197
                    indexToDelete.append(index)
                    break
            if c == '>':
                # the correct open-close combination
                if openPStack[-1] == '<':
                    del openPStack[-1]
                else:
                    print("error here", end="")
                    firstIllegalCharacterCounter += 25137
                    indexToDelete.append(index)
                    break
        counterForIncomplete = 0
        while len(openPStack) > 0:
            k = openPStack.pop(-1)
            counterForIncomplete *= 5
            if k == '(':
                counterForIncomplete += 1
            if k == '[':
                counterForIncomplete += 2
            if k == '{':
                counterForIncomplete += 3
            if k == '<':
                counterForIncomplete += 4
            print(k, end="")
        index += 1
        print(f"  {counterForIncomplete}")
        opePStackList.append(counterForIncomplete)
    print(firstIllegalCharacterCounter)
    # return the illegal closing free list
    t = np.array(opePStackList)
    t = np.delete(t, indexToDelete)
    print(np.median(t))


if __name__ == "__main__":
    part1()

