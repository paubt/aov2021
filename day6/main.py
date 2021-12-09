import numpy as np


# 0-6
# 8 if new


if __name__ == "__main__":
    start = np.genfromtxt("./data/real/input.csv", delimiter=",", dtype=int)
    repeats = 256

    # solution with individual modeling
    """
    for i in range(1, repeats+1):
        print(f"\n\n{i}  {population}")
        add8Counter = 0
        for x in range(0, len(population)):
            if population[x] > 0:
                population[x] -= 1
            else:
                population[x] = 6
                add8Counter += 1
        adds = np.zeros(add8Counter, dtype=int)
        adds.fill(8)
        population = np.append(population, adds)

    print(f"after {i} days there are {len(population)} many angelfishes")
    """

    # modeling only the number of each group

    population = np.zeros(9, dtype=int)
    print(population)
    print(start)
    # init the start population
    for x in start:
        population[x] += 1
    #
    print(population )
    for i in range(1, repeats+1):
        #
        tempHoldZeros = population[0]
        population[0] = population[1]
        population[1] = population[2]
        population[2] = population[3]
        population[3] = population[4]
        population[4] = population[5]
        population[5] = population[6]
        population[6] = population[7] + tempHoldZeros
        population[7] = population[8]
        population[8] = tempHoldZeros
    print(population)
    print(np.sum(population))