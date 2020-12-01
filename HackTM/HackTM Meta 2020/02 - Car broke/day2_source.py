from collections import defaultdict
from functools import reduce


def toposort(data):
    extra_items = reduce(set.union, data.values()) - set(data.keys())
    data.update({item: set() for item in extra_items})
    rest = set()

    while True:
        ordered = set(item for item, dep in data.items() if len(dep) == 0)
        ordered.update(rest)
        if not ordered:
            break
        list_ordered = sorted(list(ordered))
        yield {list_ordered[0]}
        rest = set(list_ordered) - {list_ordered[0]}
        data = {item: (dep - {list_ordered[0]}) for item, dep in data.items() if item not in ordered}

    if len(data) != 0:
        raise Exception('Circular dependency!')


commands = defaultdict(set)

with open('day2_eg.txt', 'r') as input_file:
    for line in input_file:
        words = line.split(" ")
        commands[words[1]].add(words[4])

inverted_commands = defaultdict(set)

for key, values in commands.items():
    for value in values:
        inverted_commands[value].add(key)

top = list(toposort(inverted_commands))

with open('day2_res.txt', 'w') as output_file:
    output_file.write(', '.join([i for s in top for i in s]))
