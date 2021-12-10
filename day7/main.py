import sys

import numpy as np
import matplotlib.pyplot as plt

def test():
    crabs = np.genfromtxt("./data/test/input.csv", delimiter=",", dtype=int)
    print(crabs)

    length = 10
    series = np.zeros(length)
    for a in range(0, length):
        s = 0
        for x in range(0, len(crabs)):
            d = abs(a-crabs[x])
            s += d*(d+1)/2
        series[a] = s

    print(series)
    minimum = np.amin(series)
    minIndex = np.where(series == np.amin(series))
    print(minimum)
    print(minIndex)
    print(minIndex[0])
    plt.plot(series)
    plt.show()

    crabsD = np.zeros(length, dtype=int)
    for a in range(0, length):
        s = 0
        for x in range(0, len(crabs)):
            if crabs[x]-a != 0:
                s += ((crabs[x]-a)*(abs(crabs[x]-a)+1)/(2*abs(crabs[x]-a)))
                # s += (crabs[x]-a)/abs(crabs[x]-a)
            # s += (crabs[x]-a)/abs(crabs[x]-a)
        crabsD[a] = s

    print(crabsD)
    plt.plot(crabsD)
    plt.show()

    # now do bisection method https://en.wikipedia.org/wiki/Bisection_method



def realPlot():
    crabs = np.genfromtxt("./data/real/input.csv", delimiter=",", dtype=int)
    print(crabs.max())
    print(crabs.min())
    print(np.mean(crabs))
    print(np.median(crabs))
    length = crabs.max()

    crabsD = np.zeros(length, dtype=int)
    lowest = 0
    lowestValue = sys.maxsize
    for a in range(0, length):
        s = 0
        for x in range(0, len(crabs)):
            d = abs(a-crabs[x])
            s += d*(d+1)/2
        if s <= lowestValue:
            lowest = a
            lowestValue = s
        crabsD[a] = s
    plt.plot(crabsD)
    plt.show()
    print(f"found at {lowest} with fuelvalue = {lowestValue}")

"""
    crabsD = np.zeros(length, dtype=int)
    for a in range(0, length):
        s = 0
        for x in range(0, len(crabs)):
            if crabs[x] - a != 0:
                s += (crabs[x] - a) / abs(crabs[x] - a)
            # s += (crabs[x]-a)/abs(crabs[x]-a)
        crabsD[a] = s

    plt.plot(crabsD)
    plt.show()

    # now do bisection method https://en.wikipedia.org/wiki/Bisection_method
    top = len(crabsD)
    bot = 0
    maxIter = 100
    while top > bot:
        maxIter -= 1
        mid = int((top + bot) / 2)
        if crabsD[mid] == 0 or maxIter == 0:
            print(f"bisect: found it at {mid}", end=" ")
            k = 0
            for x in range(0, len(crabs)):
                k += abs(crabs[x] - mid)
            print(f"with fuel value {k}")
            break
        elif crabsD[mid] > 0:
            bot = mid
        else:
            top = mid
"""

if __name__ == "__main__":
    # test()

    realPlot()

#    real()

    # for x in range(0, 15):
    #    print(f"{x} with f value {x*(x+1)/2}")