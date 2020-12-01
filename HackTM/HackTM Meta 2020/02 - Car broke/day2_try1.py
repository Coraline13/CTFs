class Command(object):
    counter = 0

    def __init__(self, name: int) -> None:
        self.id = Command.counter
        self.name = name
        self.before = set([])
        Command.counter += 1

    def __str__(self):
        s = ''
        for i in self.before:
            s += str(i.id) + ', '
        return '{0} -> {1}'.format(str(self.id), s)

    def add_before(self, before: str):
        self.before.add(before)


commands = []

with open('day2_input.txt') as input_file:
    for line in input_file:
        words = line.split(" ")

        for c in commands:
            if c.name == words[1]:
                com1 = c
                break
        else:
            com1 = Command(words[1])
            commands.append(com1)

        for c in commands:
            if c.name == words[4]:
                com2 = c
                break
        else:
            com2 = Command(words[4])
            commands.append(com2)

        com1.add_before(com2)

# for c in commands:
#     print(c)

# def add_all_before(command):
#     for b in command.before:
#         command.before.add


# for c in commands:
#     if c.before is not None:


# codes = [0, 1, 12, 7, 8, 5, 13, 14, 3, 16, 19, 10, 11, 17, 2, 23, 15, 21, 4, 6, 22, 18, 9, 24, 25, 20]
# plm=''
# for i in codes:
#     for c in commands:
#         if c.id == i:
#             plm += c.name + ', '
#             break

# f = open("day2_res.txt", "w")
# f.write(plm)
# f.close()