import math
import re


def count_winning_ways(time, record_distance):
    counter = 0
    for hold in range(time):
        dist = (time - hold) * hold
        if dist > record_distance:
            counter += 1
    return counter


def part1(file_contents):
    file_contents = file_contents.readlines()
    search_string = r'(\d+)\s'
    times = [int(t) for t in re.findall(search_string, file_contents[0])]
    distances = [int(d) for d in re.findall(search_string, file_contents[1])]
    return math.prod(count_winning_ways(times[i], distances[i]) for i in range(len(times)))


def part2(file_contents):
    file_contents = file_contents.readlines()
    search_string = r'(\d+)\s'
    time = int(''.join(re.findall(search_string, file_contents[0])))
    distance = int(''.join(re.findall(search_string, file_contents[1])))
    return count_winning_ways(time, distance)
