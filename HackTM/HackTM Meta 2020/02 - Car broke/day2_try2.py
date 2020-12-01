from collections import defaultdict
from functools import reduce as _reduce

class CircularDependencyError(ValueError):
    def __init__(self, data):
        # Sort the data just to make the output consistent, for use in
        #  error messages.  That's convenient for doctests.
        s = 'Circular dependencies exist among these items: {{{}}}'.format(
            ', '.join('{!r}:{!r}'.format(key, value) for key, value in sorted(data.items())))
        super(CircularDependencyError, self).__init__(s)
        self.data = data


def toposort(data):
    # Special case empty input.
    if len(data) == 0:
        return

    # Copy the input so as to leave it unmodified.
    data = data.copy()

    # Ignore self dependencies.
    for k, v in data.items():
        v.discard(k)
    # Find all items that don't depend on anything.
    extra_items_in_deps = _reduce(set.union, data.values()) - set(data.keys())
    # Add empty dependences where needed.
    data.update({item: set() for item in extra_items_in_deps})
    rest = set()
    while True:
        ordered = set(item for item, dep in data.items() if len(dep) == 0)
        ordered.update(rest)
        # print(data)
        if not ordered:
            break
        list_ordered = list(ordered)
        list_ordered.sort()
        yield set([list_ordered[0]])
        rest = set(list_ordered) - set([list_ordered[0]])
        data = {item: (dep - set([list_ordered[0]])) for item, dep in data.items() if item not in ordered}
    if len(data) != 0:
        raise CircularDependencyError(data)


commands = dict()

with open('day2_eg.txt') as input_file:
    for line in input_file:
        words = line.split(" ")

        if words[1] in commands:
            commands[words[1]].add(words[4])
        else:
            commands[words[1]] = set([words[4]])

inverted_commands = defaultdict(set)
for key, values in commands.items():
    for value in values:
        inverted_commands[value].add(key)
print(inverted_commands)

top = list(toposort(inverted_commands))
print(top)
res = ''

for i in top:
    for j in i:
        res += j + ', '

f = open("day2_res.txt", "w")
f.write(res)
f.close()
