import queue
import re
import sys

import numpy as np
from matplotlib import pyplot as plt

np.set_printoptions(threshold=sys.maxsize, linewidth=np.inf)


def decode_input(color):
    if color[-1] == '0':
        direction = 'R'
    elif color[-1] == '1':
        direction = 'D'
    elif color[-1] == '2':
        direction = 'L'
    elif color[-1] == '3':
        direction = 'U'
    else:
        print(f'Invalid color:{color}')
    return direction, int(color[:-1], 16)


def read_input(file_contents):
    search_string = r'([LRUD]) (\d+) \(#(\w{6})\)'
    indications = []
    for line in file_contents:
        parts = re.search(search_string, line)
        direction, meters = decode_input(parts.group(3))
        indications.append({
            'direction': direction,
            'meters': meters,
        })
    return indications


def part1(file_contents):
    indications = read_input(file_contents)
    ground_map = np.full((500, 500), '.')
    current_location = {'x': len(ground_map) // 2, 'y': len(ground_map) // 2}
    ground_map[current_location['x']][current_location['y']] = '#'
    directions = {'R': {'x': 0, 'y': 1}, 'L': {'x': 0, 'y': -1}, 'U': {'x': -1, 'y': 0}, 'D': {'x': 1, 'y': 0}}
    for indication in indications:
        for _ in range(indication['meters']):
            current_location['x'] += directions[indication['direction']]['x']
            current_location['y'] += directions[indication['direction']]['y']
            ground_map[current_location['x']][current_location['y']] = '#'

    def dig_interior(x, y):
        q = queue.Queue()
        q.put((x, y))
        while not q.empty():
            (x1, y1) = q.get()
            ground_map[x1][y1] = '#'
            if ground_map[x1 + 1][y1] != '#':
                q.put((x1 + 1, y1))
            if ground_map[x1 - 1][y1] != '#':
                q.put((x1 - 1, y1))
            if ground_map[x1][y1 + 1] != '#':
                q.put((x1, y1 + 1))
            if ground_map[x1][y1 - 1] != '#':
                q.put((x1, y1 - 1))

    print(ground_map[249][248])
    # dig_interior(249, 248)
    # plt.imsave('image.png',ground_map)
    print(sum(1 for row in ground_map for col in row if col == '#'))
    return str(ground_map)
