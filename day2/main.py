import pandas as pd


def part1(commandSeries):
    forward = 0
    depth = 0
    for index in range(0, len(commandSeries)):
        command = commandSeries.iloc[index, 0]
        direction, amount = command.split(' ')
        print(f"direction: {direction} and amount: {amount} and amount into int {int(amount)}")
        if direction == "forward":
            print(f"forward update from {forward} to {forward + int(amount)}")
            forward += int(amount)
        elif direction == "down":
            print(f"forward update from {depth} to {depth + int(amount)}")
            depth += int(amount)
        else:
            print(f"forward update from {depth} to {depth - int(amount)}")
            depth -= int(amount)
    print(f"summed forward: {forward} and depth: {depth}")
    print(f"multiplied: {depth * forward}")

def part2(commandSeries):
    forward = 0
    depth = 0
    aim = 0
    for index in range(0, len(commandSeries)):
        command = commandSeries.iloc[index, 0]
        direction, amount = command.split(' ')
        print(f"direction: {direction} and amount: {amount} and amount into int {int(amount)}")
        if direction == "forward":
            print(f"foeward update from {forward} to {forward + int(amount)}")
            forward += int(amount)
            depth += aim * int(amount)
        elif direction == "down":
            print(f"from {aim} to {aim + int(amount)}")
            aim += int(amount)
        else:
            print(f"update from {aim} to {aim - int(amount)}")
            aim -= int(amount)
    print(f"summed forward: {forward} and depth: {depth}")
    print(f"multiplied: {depth * forward}")


if __name__ == "__main__":
    commandSeries = pd.read_csv("./data/input.csv")
    #part1(commandSeries)
    part2(commandSeries)