f = open("day1_input.txt", "r")
input = f.read().split(", ")

x = 0
y = 0
dir = 'N'


def new_dir(actual_dir, turn):
    if actual_dir == 'N':
        if turn == 'R':
            return 'E'
        else:
            return 'W'
    if actual_dir == 'E':
        if turn == 'R':
            return 'S'
        else:
            return 'N'
    if actual_dir == 'S':
        if turn == 'R':
            return 'W'
        else:
            return 'E'
    if actual_dir == 'W':
        if turn == 'R':
            return 'N'
        else:
            return 'S'


def update_pos(dir, x, y, steps):
    if dir == 'N':
        return x, y + steps
    if dir == 'E':
        return x + steps, y
    if dir == 'S':
        return x, y - steps
    if dir == 'W':
        return x - steps, y


for i in input:
    dir = new_dir(dir, i[0])
    x, y = update_pos(dir, x, y, int(i[1:]))

print('{0}, {1}'.format(x, y))
