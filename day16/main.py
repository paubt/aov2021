import numpy as np

globalVersionCounter = 0


def calcWithTypeID(valueList, typeID):
    typeID = int(typeID, 2)
    print(typeID)
    if typeID == 0:
        return sum(valueList)
    if typeID == 1:
        p = 1
        for x in valueList:
            p *= x
        return p
    if typeID == 2:
        return min(valueList)
    if typeID == 3:
        return max(valueList)
    if typeID == 5:
        assert len(valueList) == 2
        if valueList[0] > valueList[1]:
            return 1
        return 0
    if typeID == 6:
        assert len(valueList) == 2
        if valueList[0] < valueList[1]:
            return 1
        return 0
    if typeID == 7:
        assert len(valueList) == 2
        if valueList[0] == valueList[1]:
            return 1
        return 0
    raise ValueError


def recursivePars(binaryString):
    # take the first
    version, typeID, binaryString = binaryString[:3], binaryString[3:6], binaryString[6:]
    # sum version to global counter variable
    global globalVersionCounter
    globalVersionCounter += int(version, 2)
    # if type 4 this is literal value
    if typeID == "100":
        if VERBOSE:
            print("\nenter literal\n", end="")
            print(version, typeID, binaryString)
        prefix = '1'
        vList = ""
        while prefix == '1':
            prefix, value, binaryString = binaryString[0], binaryString[1:5], binaryString[5:]
            if VERBOSE:
                print(prefix, value, binaryString)
            vList += value
        return int(vList, 2), binaryString
    # operator type
    else:
        lengthTypeID, binaryString = binaryString[0], binaryString[1:]
        if VERBOSE:
            print(version, typeID, lengthTypeID, binaryString)
        # length type id  0->total length and 1->number of sub packets
        if lengthTypeID == '0':
            totalLength, binaryString = binaryString[:15], binaryString[15:]
            if VERBOSE:
                print(totalLength, binaryString)
                print(int(totalLength, 2))
            totalLength = int(totalLength, 2)
            substring, binaryString = binaryString[:totalLength], binaryString[totalLength:]
            if VERBOSE:
                print(substring, binaryString)
            vList = []
            while len(substring) > 0:
                newV, substring = recursivePars(substring)
                vList.append(newV)
                if VERBOSE:
                    print(newV, substring)
            vSum = calcWithTypeID(vList, typeID)
            if VERBOSE:
                print(vList)
                print(vSum)
            return vSum, binaryString
        else:
            numberOfSubPackets, binaryString = binaryString[:11], binaryString[11:]
            if VERBOSE:
                print(numberOfSubPackets, binaryString)
            numberOfSubPackets = int(numberOfSubPackets, 2)
            vList = []
            for x in range(numberOfSubPackets):
                vNew, binaryString = recursivePars(binaryString)
                vList.append(vNew)
                if VERBOSE:
                    print(vNew, binaryString)
            vSum = calcWithTypeID(vList, typeID)
            if VERBOSE:
                print(vSum)
                return vSum, binaryString


if __name__ == "__main__":
    VERBOSE = False
    # read in input and transform in int 2d array
    f = np.genfromtxt("data/test/input3.csv", dtype=str)
    # translate to binary
    binary = ""
    for c in f.item(0):
        if c == "0":
            binary += "0000"
        elif c == "1":
            binary += "0001"
        elif c == "2":
            binary += "0010"
        elif c == "3":
            binary += "0011"
        elif c == "4":
            binary += "0100"
        elif c == "5":
            binary += "0101"
        elif c == "6":
            binary += "0110"
        elif c == "7":
            binary += "0111"
        elif c == "8":
            binary += "1000"
        elif c == "9":
            binary += "1001"
        elif c == "A":
            binary += "1010"
        elif c == "B":
            binary += "1011"
        elif c == "C":
            binary += "1100"
        elif c == "D":
            binary += "1101"
        elif c == "E":
            binary += "1110"
        elif c == "F":
            binary += "1111"
        else:
            raise ValueError

    print(binary)

    v, rest = recursivePars(binary)
    print(f"the value is {v}")
    print(f"with version sum of {globalVersionCounter}")
