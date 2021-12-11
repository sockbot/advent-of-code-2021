from itertools import chain
from pprint import pprint
import copy
lines = """
6617113584
6544218638
5457331488
1135675587
1221353216
1811124378
1387864368
4427637262
6778645486
3682146745
"""
# lines = """
# 5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526
# """
# lines = """
# 11111
# 19991
# 19191
# 19991
# 11111
# """
lines = lines.strip()
lines = lines.split('\n')
input = [[int(digit) for digit in num] for num in lines]


def increment_adj(grid, row, col) -> bool:
    # returns whether or not has 10s
    has_10s = False
    for d_row in (-1, 0, 1):
        for d_col in (-1, 0, 1):
            if d_row == 0 and d_col == 0:
                continue
            if row+d_row < 0 or row+d_row >= len(grid):
                continue
            if col+d_col < 0 or col+d_col >= len(grid[0]):
                continue
            if not isinstance(grid[row+d_row][col+d_col], int):
                continue
            grid[row+d_row][col+d_col] += 1
            if grid[row+d_row][col+d_col] > 9:
                has_10s = True
    return has_10s


def flash(grid: list[list]):
    has_10s = True
    while has_10s:
        has_10s = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "x":
                    continue
                if grid[row][col] > 9:
                    grid[row][col] = "x"
                    if increment_adj(grid, row, col):
                        has_10s = True


def part1(input):
    total_flashes = 0
    grid = copy.copy(input)
    for _ in range(100):
        grid = [[element + 1 for element in row] for row in grid]
        flash(grid)
        total_flashes += len([energy for energy in list(chain(*grid))
                             if energy == "x"])
        grid = [[0 if (element == 'x') else element for element in row]
                for row in grid]
        pprint(grid)
    return total_flashes


def part2(input):
    grid = copy.copy(input)
    step = 0
    while True:
        grid = [[element + 1 for element in row] for row in grid]
        flash(grid)
        step += 1
        if len([energy for energy in list(chain(*grid)) if energy == "x"]) == 100:
            return step
        grid = [[0 if (element == 'x') else element for element in row]
                for row in grid]
        pprint(grid)


print(part1(input))
print(part2(input))
