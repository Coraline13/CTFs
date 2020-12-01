directions = ['N', 'E', 'S', 'W']


class Position(object):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.history = [(x, y)]
        self.orientation = 'N'

    def __str__(self):
        return '{0}, {1}'.format(self.x, self.y)

    def move_one(self):
        if self.orientation == 'N':
            self.y += 1
        elif self.orientation == 'E':
            self.x += 1
        elif self.orientation == 'S':
            self.y -= 1
        elif self.orientation == 'W':
            self.x -= 1

        self.history.append((self.x, self.y))

    def move(self, times: int):
        for t in range(times):
            self.move_one()

    def turn(self, direction: str):
        curr = directions.index(self.orientation)
        if direction == 'L':
            result = (curr - 1) % len(directions)
        elif direction == 'R':
            result = (curr + 1) % len(directions)

        self.orientation = directions[result]


f = open("day1_input.txt", "r")
input = f.read().split(", ")

pos = Position(0, 0)

for i in input:
    pos.turn(i[0])
    pos.move(int(i[1:]))

print(pos)
