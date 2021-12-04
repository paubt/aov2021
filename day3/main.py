import numpy
import numpy as np


def binaryStringToDecimal(binaryString):
    print(binaryString)
    # reverse string
    reverseBin = binaryString[::-1]
    decimal = 0
    for n in range(0, len(reverseBin)):
        if reverseBin[n] == "1":
            decimal += pow(2, n)
    return decimal


def part1(binDiagnostic):
    gammaString = ""
    # iterate through the diagnostic range
    for i in range(0, len(binDiagnostic[0])):
        # gamma rate most common bit
        mcb = 0
        # iterate through all the diagnostic sequences
        for j in range(0, len(binDiagnostic)):
            print(binDiagnostic[j][i])
            if int(binDiagnostic[j][i]) == 1:
                mcb += 1
            else:
                mcb -= 1
        if mcb > 0:
            gammaString += "1"
        else:
            gammaString += "0"
    # swap bit to get epsilon form gamma
    epsilonString = ""
    for x in gammaString:
        if x == "0":
            epsilonString += "1"
        else:
            epsilonString += "0"
    print(f"gamma = {gammaString}")
    print(f"epsilon = {epsilonString}")
    gamma = binaryStringToDecimal(gammaString)
    epsilon = binaryStringToDecimal(epsilonString)
    print(f"gamma {gamma} * epsilon {epsilon}  = power Consumption {gamma * epsilon}")

def co2ScrRat(diagnostic):
    index = 0
    while len(diagnostic) > 1:
        print(diagnostic)
        if index >= 12:
            index = 0
        print(f"index is {index}")
        mcb = 0
        for i in range(0, len(diagnostic)):
            if int(diagnostic[i][index]) == 1:
                mcb += 1
            else:
                mcb -= 1
        # delete all with 0 at that i position or equal amount
        print(f"mcb is {mcb}")
        if mcb < 0:
            deleteList = list()
            for i in range(0, len(diagnostic)):
                if diagnostic[i][index] == "0":
                    # add the index to a delete list
                    deleteList.append(i)
        else:
            deleteList = list()
            for i in range(0, len(diagnostic)):
                if diagnostic[i][index] == "1":
                    deleteList.append(i)
        print(deleteList)
        diagnostic = numpy.delete(diagnostic, deleteList)
        index += 1
    return diagnostic


def oxyGenRat(diagnostic):
    index = 0
    while len(diagnostic) > 1:
        print(diagnostic)
        if index >= 12:
            index = 0
        print(f"index is {index}")
        mcb = 0
        for i in range(0, len(diagnostic)):
            if int(diagnostic[i][index]) == 1:
                mcb += 1
            else:
                mcb -= 1
        # delete all with 0 at that i position or equal amount
        print(f"mcb is {mcb}")
        if mcb >= 0:
            deleteList = list()
            for i in range(0, len(diagnostic)):
                if diagnostic[i][index] == "0":
                    # add the index to a delete list
                    deleteList.append(i)
        else:
            deleteList = list()
            for i in range(0, len(diagnostic)):
                if diagnostic[i][index] == "1":
                    deleteList.append(i)
        print(deleteList)
        diagnostic = numpy.delete(diagnostic, deleteList)
        index += 1
    return diagnostic



def part2(diagnostic):
    oxyGen = oxyGenRat(diagnostic)
    print(oxyGen)
    oxy = binaryStringToDecimal(str(oxyGen[0]))


    co2Scr = co2ScrRat(diagnostic)
    print(co2Scr)
    co2 = binaryStringToDecimal(str(co2Scr[0]))

    print(co2 * oxy)



if __name__ == "__main__":
    diagnostic = np.genfromtxt("./data/input.csv", dtype=str)
    test = np.genfromtxt("./data/testinput.csv", dtype=str)
    part2(diagnostic)