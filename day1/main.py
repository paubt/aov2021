import numpy as np
import pandas as pd


def part1():
    # read in input
    series = pd.read_csv(filepath_or_buffer="data/real/input.csv", header=None)
    # counter for increases in measurement
    c = 0
    # iterate through the series stepping over the first measurement
    for i in range(1, len(series)):
        # if new measurement larger than the last one increment the counter
        if series.iloc[i, 0] > series.iloc[i - 1, 0]:
            c += 1
    print(f"the measurement incremented {c} times")


def part2():
    # read in input
    series = np.genfromtxt("data/real/input.csv")
    # list to store the new series in
    threeWindowList = list()
    # create the 3 measurement sum window
    for x in range(0, len(series) - 2):
        t = series[x] + series[x+1] + series[x+2]
        threeWindowList.append(t)
    # counter for the number of increases
    increases = 0
    # check if there is a increase
    for x in range(0, len(threeWindowList)-1):
        if threeWindowList[x] < threeWindowList[x+1]:
            increases += 1
    print(f"the measurement increased {increases} times")


if __name__ == "__main__":
    part1()
    part2()
