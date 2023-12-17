import itertools
import math
import re


def read_map_and_directions(file_contents):
    file_contents = file_contents.readlines()
    directions = file_contents[0].rstrip()
    search_string = r'(\w+) = \((\w+), (\w+)\)'
    input_map = {}
    for line in file_contents[2:]:
        values = re.search(search_string, line.rstrip())
        input_map[values[1]] = {'L': values[2], 'R': values[3]}
    return input_map, directions


def compute_steps(input_map, directions, current_locations):
    counter = 0
    locations_counter = {}
    for step in itertools.cycle(directions):
        counter += 1
        finished = True
        for idx, location in enumerate(current_locations):
            current_locations[idx] = input_map[location][step]
            if not current_locations[idx].endswith('Z'):
                finished = False
            elif current_locations[idx] not in locations_counter:
                locations_counter[current_locations[idx]] = counter
            if len(locations_counter) == 6:
                return math.lcm(*locations_counter.values())
        if finished:
            return counter


def part1(file_contents):
    input_map, directions = read_map_and_directions(file_contents)
    current_locations = ['AAA']
    return compute_steps(input_map, directions, current_locations)


def part2(file_contents):
    input_map, directions = read_map_and_directions(file_contents)
    current_locations = [location for location in input_map if location.endswith('A')]
    return compute_steps(input_map, directions, current_locations)
