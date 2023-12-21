import math
from collections import defaultdict

DIRECTIONS = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


def invalid_pos(engine, row, col, d):
    return row + d[0] < 0 or row + d[0] >= len(engine) or col + d[1] < 0 or col + d[1] >= len(engine[0])


def part1(file_contents):
    engine = [list(line.rstrip()) for line in file_contents]
    s = 0
    current_num = 0
    is_part = False
    for row in range(len(engine)):
        if is_part:
            s += current_num
            is_part = False
        current_num = 0
        for col in range(len(engine[0])):
            if engine[row][col].isdigit():
                current_num = current_num * 10 + int(engine[row][col])
                for d in DIRECTIONS:
                    if invalid_pos(engine, row, col, d):
                        continue
                    cell = engine[row + d[0]][col + d[1]]
                    if cell != '.' and not cell.isdigit():
                        is_part = True
                        break
            else:
                if is_part:
                    s += current_num
                    is_part = False
                current_num = 0
    return s


def part2(file_contents):
    engine = [list(line.rstrip()) for line in file_contents]
    gears = defaultdict(list)
    gear_pos = None
    current_num = 0
    for row in range(len(engine)):
        if gear_pos:
            gears[gear_pos].append(current_num)
        gear_pos = None
        current_num = 0
        for col in range(len(engine[0])):
            if engine[row][col].isdigit():
                current_num = current_num * 10 + int(engine[row][col])
                for d in DIRECTIONS:
                    if invalid_pos(engine, row, col, d):
                        continue
                    cell = engine[row + d[0]][col + d[1]]
                    if cell == '*':
                        gear_pos = (row + d[0], col + d[1])
                        break
            else:
                if gear_pos:
                    gears[gear_pos].append(current_num)
                gear_pos = None
                current_num = 0
    return sum(math.prod(gears[g]) for g in gears if len(gears[g]) > 1)
