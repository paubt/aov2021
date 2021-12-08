import numpy as np

if __name__ == "__main__":
    vents = np.genfromtxt("./data/test/input.csv", dtype=str)
    fieldSize = 10
    field = np.zeros((fieldSize, fieldSize))

    # drop middle column
    vents = np.delete(vents, 1, axis=1)
    try:
        for i in range(0, len(vents)):
            x1, y1 = vents[i][0].split(",", 1)
            x2, y2 = vents[i][1].split(",", 1)

            # if only one vent
            if x1 == x2 and y1 == y2:
                print("lel")
            # check if horizontal

            elif x1 == x2:
                print(f"vertical: {x1} {y1} | ", end="")
                print(f"{x2} {y2}")
                if int(y1) <= int(y2):
                    for k in range(int(y1), int(y2)+1):
                        field[k][int(x1)] += 1
                else:
                    for k in range(int(y2), int(y1)+1):
                        field[k][int(x1)] += 1
                continue
            elif y1 == y2:
                print(f"horizontal: {x1} {y1} | ", end="")
                print(f"{x2} {y2}")
                if int(x1) <= int(x2):
                    for k in range(int(x1), int(x2)+1):
                        field[int(y1)][k] += 1
                else:
                    for k in range(int(x2), int(x1)+1):
                        field[int(y1)][k] += 1
            elif x1 < x2 and y1 < y2:
                print(f"dia nw-se: {x1} {y1} | {x2} {y2}")
                for k in range(0, int(x2)-int(x1)+1):
                    # print(f"{int(x1)+k} {int(y1)+k}")
                    field[int(x1)+k][int(y1)+k] += 1
            elif x1 > x2 and y1 > y2:
                print(f"dia se-nw: {x1} {y1} | {x2} {y2}")
                for k in range(0, int(x1)-int(x2)+1):
                    # print(f"{int(x1)-k} {int(y1)-k}")
                    field[int(y1)-k][int(x1)-k] += 1
                    # print(k)
            elif x1 < x2 and y1 > y2:
                print(f"dia sw-ne: {x1} {y1} | {x2} {y2}")
                for k in range(0, int(x2)-int(x1)+1):
                    # print(k)
                    # print(f"{int(x1)-k} {int(y1)+k}")
                    field[int(x1)-k][int(y1)+k] += 1
            elif x1 > x2 and y1 < y2:
                print(f"dia ne-sw: {x1} {y1} | {x2} {y2}")
                for k in range(0, int(x1)-int(x2)+1):
                    print(k)
                    print(f"{int(x1) - k} {int(y1) + k}")
                    field[int(y1)+k][int(x1)-k] += 1


    except IndexError:
        print(i)
        print(x1, y2)

    print(field)
    # count where >2
    counter = 0
    for y in range(0, fieldSize):
        for x in range(0, fieldSize):
            if field[y][x] >= 2:
                counter += 1
    print(counter)