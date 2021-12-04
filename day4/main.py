import numpy as np


def check5x5ForWin(b):
    # check rows
    for r in range(0, 5):
        winCondition = True
        for c in range(0, 5):
            if b[r][c] == 0:
                winCondition = False
        if winCondition:
            return True
    # check columns
    for c in range(0, 5):
        winCondition = True
        for r in range(0, 5):
            if b[r][c] == 0:
                winCondition = False
        if winCondition:
            return True
    return False


def sumOfUnmarked(b, wCb):
    # iterate through the wCb
    s = 0
    for r in range(0, 5):
        for c in range(0, 5):
            if wCb[r][c] == 0:
                s += int(b[r][c])
    return s


def firstWinBoardSumOfUnmarked(boards, winConBoard, numbers):
    while len(numbers) > 0:
        # add the new number to the winConBoard
        randomNumber, numbers = numbers[0], np.delete(numbers, 0)
        print(randomNumber)
        # go through the boards and set 0 to 1 where number matches on winConBoard
        for y in range(0, len(boards)):
            for x in range(0, len(boards[0])):
                if boards[y][x] == randomNumber:
                    winConBoard[y][x] = 1
        # check in winConBoard if a board wins
        for b in range(0, int(len(boards) / 5)):
            print(f"for b = {b}:")
            print(boards[0 + b * 5:5 + b * 5])
            print(winConBoard[0 + b * 5:5 + b * 5])
            if check5x5ForWin(winConBoard[0 + b * 5:5 + b * 5]):
                print(f"found a board number: {b}")
                soum = sumOfUnmarked(boards[0 + b * 5:5 + b * 5], winConBoard[0 + b * 5:5 + b * 5])
                print(f"{soum} * {int(randomNumber)} = {str(soum * int(randomNumber))}")
                return soum * int(randomNumber)
            else:
                print("no luck")


def lastWinBoardSumOfUnmarked(boards, winConBoard, numbers):
    numberOfBoars = int(len(boards) / 5)
    foundArray = np.ones(numberOfBoars)
    print(foundArray)
    while len(numbers) > 0:
        # add the new number to the winConBoard
        randomNumber, numbers = numbers[0], np.delete(numbers, 0)
        print(randomNumber)
        # go through the boards and set 0 to 1 where number matches on winConBoard
        for y in range(0, len(boards)):
            for x in range(0, len(boards[0])):
                if boards[y][x] == randomNumber:
                    winConBoard[y][x] = 1
        # check in winConBoard if a board wins
        for b in range(0, int(len(boards) / 5)):
            print(f"for b = {b}:")
            print(boards[0 + b * 5:5 + b * 5])
            print(winConBoard[0 + b * 5:5 + b * 5])
            if check5x5ForWin(winConBoard[0 + b * 5:5 + b * 5]):
                print(f"found a board number: {b}")
                soum = sumOfUnmarked(boards[0 + b * 5:5 + b * 5], winConBoard[0 + b * 5:5 + b * 5])
                print(f"{soum} * {int(randomNumber)} = {str(soum * int(randomNumber))}")
                foundArray[b] = 0
                if np.sum(foundArray) == 0:
                    return soum * int(randomNumber)
            else:
                print("no luck")


if __name__ == "__main__":
    boards = np.genfromtxt("./data/real/boards.csv", dtype=str)
    winConBoard = np.zeros((len(boards), len(boards[0])))
    numbers = np.genfromtxt("./data/real/numbers.csv", delimiter=",", dtype=str)

    s = lastWinBoardSumOfUnmarked(boards, winConBoard, numbers)
