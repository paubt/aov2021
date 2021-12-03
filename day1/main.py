import pandas as pd

if __name__ == "__main__":
    # read in input
    series = pd.read_csv(filepath_or_buffer="./data/input.csv", header=None)
    # counter for increases in measurement
    c = 0
    print(series.iloc[0, 0])
    # iterate through the series stepping over the first measurement
    for i in range(1, len(series)):
        print(f"{series.iloc[i, 0]} ", end="")
        # if new measurement larger than the last one increment the counter
        if series.iloc[i, 0] > series.iloc[i - 1, 0]:
            c += 1
            print("increased")
        else:
            print("decreased")
    print(f"the measurement incremented {c} times")
