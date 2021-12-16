import sys
import numpy as np
from collections import Counter


def part1():
    input = list(np.genfromtxt("./data/real/input.csv", delimiter=",", dtype=str))
    polymer = input[0]

    insertDict = dict()
    possibleCharacter = list()

    print(polymer.split())
    print(polymer)

    # make dictionary for the insert elements
    for i in range(1, len(input)):
        print(f"{input[i][:2]}   {input[i][-1:]}")
        insertDict.update({input[i][:2]: input[i][-1:]})
        possibleCharacter.append(input[i][-1:])
    possibleCharacter = set(possibleCharacter)
    print(possibleCharacter)

    print(f"Template:     {polymer}")
    for n in range(40):
        # create list of elements to add
        insertList = []
        for i in range(len(polymer) - 1):
            charToInsert = insertDict[str(polymer[0 + i:2 + i])]
            insertList.append(charToInsert)

        # interlace polymer string with insertList starting and ending with polymer
        addedElements = 0
        for i in range(1, len(polymer)):
            k = i + addedElements
            polymer = polymer[:k] + insertList[i - 1] + polymer[k:]
            addedElements += 1
        print(f"After step {n + 1} ")

    print(len(polymer))
    print(set(polymer))

    minCount = sys.maxsize
    maxCount = 0
    for c in set(polymer):
        counter = 0
        for x in range(len(polymer)):
            if polymer[x] == c:
                counter += 1
        print(f"character {c} occurs {counter} times")
        if counter > maxCount:
            maxCount = counter
        elif counter < minCount:
            minCount = counter

    print(f"max {maxCount} - min {minCount} = {maxCount - minCount}")


def part2():
    input = list(np.genfromtxt("./data/real/input.csv", delimiter=",", dtype=str))

    insertDict = dict()
    counterDict = dict()
    possibleCharacter = list()
    # make dictionary for the insert elements and a counter dictionary and a list with all possible characters
    for i in range(1, len(input)):
        # print(f"{input[i][:2]}   {input[i][-1:]}")
        insertDict.update({input[i][:2]: input[i][-1:]})
        counterDict.update({input[i][:2]: 0})
        possibleCharacter.append(input[i][-1:])
    possibleCharacter = set(possibleCharacter)

    print(insertDict)
    print(counterDict)

    # add the starting pairs into the counter Dictionary
    for i in range(len(input[0]) - 1):
        print(input[0][i:i + 2])
        counterDict[input[0][i:i + 2]] += 1
    print(counterDict)
    sumOfPairs = 0
    for _, v in counterDict.items():
        sumOfPairs += v
    # print(f"sumOfPairs is {sumOfPairs} => length = {sumOfPairs + 1}")
    for n in range(40):
        # the temporal storage
        tempDict = dict(counterDict)
        # set all values to zero in the temporal dictionary
        for k, v in tempDict.items():
            tempDict[k] = 0
        # iterate through the counter Dictionary
        for k, v in counterDict.items():
            # the character to insert for this pair
            c = insertDict[k]
            # the new pairs after inserting the new character
            newPairLeft = k[:1] + c
            newPairRight = c + k[-1:]
            # add the 2 new pairs to the temporal Dictionary
            tempDict[newPairLeft] += v
            tempDict[newPairRight] += v
        # print(tempDict)
        counterDict = dict(tempDict)
        sumOfPairs = 0
        for _, v in counterDict.items():
            sumOfPairs += v
        print(f"{n} sumOfPairs is {sumOfPairs} => length = {sumOfPairs + 1}")
    print(counterDict)

    # to store the counts in
    tempZeros = [0] * len(possibleCharacter)
    tempZipList = zip(possibleCharacter, tempZeros)
    possibleCharDict = dict(tempZipList)

    # counter occurrences of possible characters
    for c in possibleCharacter:

        for k, v in counterDict.items():
            if k[:1] == c:
                print(c, k)
                possibleCharDict[c] += v
    # add 1 to the last character cause above only the first is considered
    possibleCharDict[input[0][-1]] += 1
    # figure out the max and min values in the dictionary
    maxCount = 0
    minCount = sys.maxsize
    for k, v in possibleCharDict.items():
        if v > maxCount:
            maxCount = v
        elif v < minCount:
            minCount = v
    print(f"max = {maxCount} and min = {minCount} => max-min = {maxCount-minCount}")

    print(possibleCharDict)

if __name__ == "__main__":
    # part1()
    part2()
