import numpy as np


def main():

    def tryExplode(numberToReduce):
        for x in numberToReduce:
            print(x, end="")
        print()
        # counts the "inside-ness" how many pairs inside we currently are
        insideCounter = 0
        # store the index's of the numbers in list
        indexOfLastNumbers = []
        indexOfNextNumber = 0
        # iterate over the number
        for index in range(len(numberToReduce)):
            # if next is opener only increment the "recursion"/"inside" depth counter
            if numberToReduce[index] == '[':
                insideCounter += 1
            # if next is closer check if this is closing inside deeper than 4 and if so perform explode on last pair
            elif numberToReduce[index] == ']':
                if insideCounter > 4:
                    # conditions are meet and perform explode
                    # first find the next number if there exist one
                    # by continuing the for loop until a number is found or hits end
                    nextIndex = len(numberToReduce)-1
                    for nextIndex in range(index, len(numberToReduce)):
                        if numberToReduce[nextIndex] == '[' or numberToReduce[nextIndex] == ']':
                            continue
                        else:
                            break
                    print(f"index {index}")
                    # there is a next number
                    if nextIndex == len(numberToReduce)-1:
                        thereIsNextNumber = False
                        print(f"there is no next number {nextIndex}")
                    else:
                        thereIsNextNumber = True
                        print(f"next number at index {nextIndex} with value {numberToReduce[nextIndex]}")
                    # check if there is a number before
                    if len(indexOfLastNumbers) < 3:
                        thereIsLastNumber = False
                        print(f"there is no last number {nextIndex}")
                    else:
                        thereIsLastNumber = True
                        print(f"here we need explode {index} and lastNumer {numberToReduce[indexOfLastNumbers[-3]]}")
                    # increment the next and last number correspondingly
                    if thereIsNextNumber:
                        # t = int(numberToReduce[nextIndex]) + int(numberToReduce[index-1])
                        numberToReduce[nextIndex] = str(int(numberToReduce[nextIndex]) + int(numberToReduce[index-1]))
                    if thereIsLastNumber:
                        # t = int(numberToReduce[indexOfLastNumbers[-3]]) + int(numberToReduce[index-2])
                        numberToReduce[indexOfLastNumbers[-3]] = str(int(numberToReduce[indexOfLastNumbers[-3]]) + int(numberToReduce[index-2]))
                    # replace the middle part with zero
                    newNumber = numberToReduce[:index-3] + ["0"] + numberToReduce[index+1:]
                    for x in newNumber:
                        print(x, end="")
                    print()
                    return True, newNumber
                insideCounter -= 1
            # if only number append the number's index to the last index list
            else:
                indexOfLastNumbers.append(index)
        print("no explode")
        return False, numberToReduce


    def reduce():
        while True:
            # Explode    check for nested inside four pairs

            # Split      check for 10 or greater
            pass

    numbersAsString = np.genfromtxt("data/test/input.csv", dtype=str)
    # transform string to list
    numbersList = []
    for x in numbersAsString:
        numberAsList = []
        for c in x:
            if c == ',':
                continue
            numberAsList.append(c)
        numbersList.append(numberAsList)

    print(tryExplode(numbersList[4]))

if __name__ == "__main__":
    main()