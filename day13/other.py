import pathlib

FILLED_SPACE = "■"
EMPTY_SPACE = " "


def get_input_data_from_input_file() -> tuple[
    set[tuple[int, int]], list[tuple[str, int]]
]:
    with open(
        pathlib.Path(__file__).parent / "data" / "data.csv"
    ) as input_file:
        points: set[tuple[int, int]] = set()
        while (line := input_file.readline()) != "\n":
            points.add(tuple(map(int, line.strip().split(","))))

        instructions: list[tuple[str, int]] = []
        instruction_prefix = "fold along "
        for line in input_file.readlines():
            assert line.startswith(instruction_prefix)
            axis, index = line[len(instruction_prefix) :].strip().split("=")
            instructions.append((axis, int(index)))

    return points, instructions


def create_grid_from_input_data(input_data: set[tuple[int, int]]) -> list[list[str]]:
    max_column = max(point[0] for point in input_data)
    max_row = max(point[1] for point in input_data)
    return [
        [
            FILLED_SPACE if (column, row) in input_data else EMPTY_SPACE
            for column in range(max_column + 1)
        ]
        for row in range(max_row + 1)
    ]


def fold_grid(
    grid: list[list[str]], fold_axis: str, fold_index: int
) -> list[list[str]]:
    """Brute force solution"""
    if fold_axis == "x":
        # iterate grid2 columns in reverse
        row_iterator = [(index, index) for index in range(len(grid))]
        column_iterator = [
            indexes
            for indexes in zip(
                range(fold_index), range(len(grid[0]) - 1, fold_index, -1)
            )
        ]

    else:  # fold_axis == "y"
        # iterate grid2 rows in reverse
        row_iterator = [
            indexes
            for indexes in zip(range(fold_index), range(len(grid) - 1, fold_index, -1))
        ]
        column_iterator = [(index, index) for index in range(len(grid[0]))]

    return [
        [
            FILLED_SPACE
            if grid[row_index1][column_index1] == FILLED_SPACE
            or grid[row_index2][column_index2] == FILLED_SPACE
            else EMPTY_SPACE
            for column_index1, column_index2 in column_iterator
        ]
        for row_index1, row_index2 in row_iterator
    ]


def print_grid(grid: list[list[str]]):
    for row in grid:
        for value in row:
            print(value, end="")

        print("\n", end="")


def fold_points(
    points: set[tuple[int, int]], fold_axis, fold_index
) -> set[tuple[int, int]]:
    """Optimized solution"""
    if fold_axis == "x":

        def fold_point(column, row):
            return (fold_index - abs(fold_index - column), row)

    else:  # fold_axis == "y"

        def fold_point(column, row):
            return (column, fold_index - abs(fold_index - row))

    return {fold_point(*point) for point in points}


def print_points(points: set[tuple[int, int]]):
    max_column = max(point[0] for point in points)
    max_row = max(point[1] for point in points)
    for row in range(max_row + 1):
        for column in range(max_column + 1):
            print(FILLED_SPACE if (column, row) in points else EMPTY_SPACE, end="")

        print("\n", end="")


def part1(points: set[tuple[int, int]], axis: str, index: int):
    """
    --- Day 13: Transparent Origami ---

    You reach another volcanically active part of the cave. It would be nice if you could do some kind of thermal imaging so you could tell ahead of time which caves are too hot to safely enter.

    Fortunately, the submarine seems to be equipped with a thermal camera! When you activate it, you are greeted with:

    Congratulations on your purchase! To activate this infrared thermal imaging
    camera system, please enter the code found on page 1 of the manual.

    Apparently, the Elves have never used this feature. To your surprise, you manage to find the manual; as you go to open it, page 1 falls out. It's a large sheet of transparent paper! The transparent paper is marked with random dots and includes instructions on how to fold it up (your puzzle input). For example:

    6,10
    0,14
    9,10
    0,3
    10,4
    4,11
    6,0
    6,12
    4,1
    0,13
    10,12
    3,4
    3,0
    8,4
    1,10
    2,14
    8,10
    9,0

    fold along y=7
    fold along x=5

    The first section is a list of dots on the transparent paper. 0,0 represents the top-left coordinate. The first value, x, increases to the right. The second value, y, increases downward. So, the coordinate 3,0 is to the right of 0,0, and the coordinate 0,7 is below 0,0. The coordinates in this example form the following pattern, where # is a dot on the paper and . is an empty, unmarked position:

    ...#..#..#.
    ....#......
    ...........
    #..........
    ...#....#.#
    ...........
    ...........
    ...........
    ...........
    ...........
    .#....#.##.
    ....#......
    ......#...#
    #..........
    #.#........

    Then, there is a list of fold instructions. Each instruction indicates a line on the transparent paper and wants you to fold the paper up (for horizontal y=... lines) or left (for vertical x=... lines). In this example, the first fold instruction is fold along y=7, which designates the line formed by all of the positions where y is 7 (marked here with -):

    ...#..#..#.
    ....#......
    ...........
    #..........
    ...#....#.#
    ...........
    ...........
    -----------
    ...........
    ...........
    .#....#.##.
    ....#......
    ......#...#
    #..........
    #.#........

    Because this is a horizontal line, fold the bottom half up. Some of the dots might end up overlapping after the fold is complete, but dots will never appear exactly on a fold line. The result of doing this fold looks like this:

    #.##..#..#.
    #...#......
    ......#...#
    #...#......
    .#.#..#.###
    ...........
    ...........

    Now, only 17 dots are visible.

    Notice, for example, the two dots in the bottom left corner before the transparent paper is folded; after the fold is complete, those dots appear in the top left corner (at 0,0 and 0,1). Because the paper is transparent, the dot just below them in the result (at 0,3) remains visible, as it can be seen through the transparent paper.

    Also notice that some dots can end up overlapping; in this case, the dots merge together and become a single dot.

    The second fold instruction is fold along x=5, which indicates this line:

    #.##.|#..#.
    #...#|.....
    .....|#...#
    #...#|.....
    .#.#.|#.###
    .....|.....
    .....|.....

    Because this is a vertical line, fold left:

    #####
    #...#
    #...#
    #...#
    #####
    .....
    .....

    The instructions made a square!

    The transparent paper is pretty big, so for now, focus on just completing the first fold. After the first fold in the example above, 17 dots are visible - dots that end up overlapping after the fold is completed count as a single dot.

    How many dots are visible after completing just the first fold instruction on your transparent paper?
    """
    points = fold_points(points, axis, index)
    print(len(points))
    return points


def part2(points: set[tuple[int, int]], instructions: list[tuple[str, int]]):
    """
    Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.

    What code do you use to activate the infrared thermal imaging camera system?
    """
    for axis, index in instructions:
        points = fold_points(points, axis, index)

    print_points(points)


def main():
    points, instructions = get_input_data_from_input_file()
    axis, index = instructions[0]
    points = part1(points, axis, index)
    part2(points, instructions[1:])


if __name__ == "__main__":
    main()
