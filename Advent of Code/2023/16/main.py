from queue import Queue

import numpy as np

DIRECTIONS = {
    'L': [0, -1],
    'R': [0, 1],
    'U': [-1, 0],
    'D': [1, 0],
}


def valid(matrix, current_location, inertia, history):
    return not (
            (*current_location, inertia) in history
            or current_location[0] < 0
            or current_location[1] < 0
            or current_location[0] >= len(matrix)
            or current_location[1] >= len(matrix[0])
    )


def new_step(current_location, inertia):
    return (
        current_location[0] + DIRECTIONS[inertia][0],
        current_location[1] + DIRECTIONS[inertia][1],
        inertia,
    )


def parse_special_char(current_location, inertia, special_char):
    if special_char == '/':
        if inertia == 'R':
            inertia = 'U'
        elif inertia == 'L':
            inertia = 'D'
        elif inertia == 'U':
            inertia = 'R'
        elif inertia == 'D':
            inertia = 'L'
        return new_step(current_location, inertia),

    if special_char == '\\':
        if inertia == 'R':
            inertia = 'D'
        elif inertia == 'L':
            inertia = 'U'
        elif inertia == 'U':
            inertia = 'L'
        elif inertia == 'D':
            inertia = 'R'
        return new_step(current_location, inertia),

    if special_char == '|':
        if inertia in ['L', 'R']:
            return new_step(current_location, 'U'), new_step(current_location, 'D')
        else:
            return new_step(current_location, inertia),

    if special_char == '-':
        if inertia in ['U', 'D']:
            return new_step(current_location, 'L'), new_step(current_location, 'R')
        else:
            return new_step(current_location, inertia),

    raise AssertionError(f'Unexpected char: {special_char}')


def get_all_possible_starts(grid):
    return (
            [(0, y, 'D') for y in range(len(grid[0]))]
            + [(x, 0, 'R') for x in range(len(grid))]
            + [(len(grid) - 1, y, 'U') for y in range(len(grid[0]))]
            + [(x, len(grid[0]) - 1, 'L') for x in range(len(grid))]
    )


def solve(grid, initial_location):
    matrix_copy = np.full((len(grid), len(grid[0])), '.')
    queue = Queue()
    history = set()
    queue.put(initial_location)

    while not queue.empty():
        *current_location, inertia = queue.get()

        while True:
            if not valid(grid, current_location, inertia, history):
                break

            matrix_copy[current_location[0]][current_location[1]] = '#'
            history.add((*current_location, inertia))
            current_element = grid[current_location[0]][current_location[1]]

            if current_element == '.':
                *current_location, inertia = new_step(current_location, inertia)
            else:
                next_steps = parse_special_char(current_location, inertia, current_element)
                for step in next_steps:
                    queue.put(step)
                break

    return sum(1 for row in matrix_copy for elem in row if elem == '#')


def part1(file_contents):
    grid = [line.rstrip() for line in file_contents]
    return solve(grid, (0, 0, 'R'))


def part2(file_contents):
    grid = [line.rstrip() for line in file_contents]
    most_energized_tiles = -1

    for start in get_all_possible_starts(grid):
        if (res := solve(grid, start)) > most_energized_tiles:
            most_energized_tiles = res

    return most_energized_tiles
