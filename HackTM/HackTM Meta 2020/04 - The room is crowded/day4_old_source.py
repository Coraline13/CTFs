class Team(object):
    counter = 1

    def __init__(self, size: float, position: float) -> None:
        self.size = size
        self.position = position
        self.start = position - size / 2
        self.end = position + size / 2
        self.id = Team.counter
        Team.counter += 1

    def __str__(self):
        return 'Team {0}: size={1}, pos={2}, start={3}, end={4}'.format(self.id, self.size, self.position, self.start, self.end)


def calculate_cost(start, stop, dif, partial_dif, clockwise=True):
    cost = 0

    if clockwise:
        for i in range(start, stop, -1):
            cost += other_teams[i].size * dif
            dif -= other_teams[i].start - other_teams[i - 1].end
    else:
        for i in range(start, max(n, stop) - 1):
            cost += abs(other_teams[i].size * dif)
            if i == n:
                dif -= other_teams[1].start - other_teams[i].end
            else:
                dif -= other_teams[i + 1].start - other_teams[i].end
        if stop == n:
            cost += abs(other_teams[i].size * partial_dif)
        if stop > 0:
            for i in range(1, stop - 1):
                cost += abs(other_teams[i].size * dif)
                dif -= other_teams[i + 1].start - other_teams[i].end
            cost += abs(other_teams[i].size * partial_dif)

    return cost


def try_moves(x, y, dnd):
    default_dif = other_teams[y].start - other_teams[x].end
    dif = 0
    best_cost = 99999
    history = []

    for k in range(x, dnd, -1):
        rest_dif = 0
        j = y
        cost = 0
        total_dif = default_dif + dif + rest_dif

        while total_dif < my_team_size and j != dnd:
            if j == n:
                rest_dif += 360 - other_teams[n].end + other_teams[1].start
                j = 1
            else:
                rest_dif += other_teams[j + 1].start - other_teams[j].end
                j = (j + 1) % (n + 1)
            total_dif = default_dif + dif + rest_dif

        if total_dif >= my_team_size:
            partial_dif = abs(total_dif - my_team_size)
            cost += calculate_cost(x, k, dif, partial_dif) + calculate_cost(y, j, rest_dif, partial_dif, clockwise=False)

            if cost < best_cost:
                best_cost = cost
                history = [k, j]

        dif += other_teams[k].start - other_teams[k - 1].end

    return 'best_cost: {}\nHackTM{{{}, {}, {}, {}}}'.format(best_cost, history[0], x, y, history[1])


with open('teams.in', 'r') as input_file:
    counter = 1
    for line in input_file:
        if counter == 1:
            n = int(line)
            other_teams = [[0, 0]]
        elif counter == n + 2:
            my_team_size = int(line)
        else:
            s, pos = line.split(' ')
            other_teams.append(Team(float(s), float(pos)))
        counter += 1

max_size = 0
max_size_index = 0
for i in range(1, len(other_teams)):
    if other_teams[i].size > max_size:
        max_size = other_teams[i].size
        max_size_index = other_teams[i].id

max_gap = 0
max_gap_indexes = [0, 0]
for i in range(1, len(other_teams) - 1):
    if other_teams[i + 1].start - other_teams[i].end > max_gap:
        max_gap = other_teams[i + 1].start - other_teams[i].end
        max_gap_indexes = [i, i + 1]

print(try_moves(max_gap_indexes[0], max_gap_indexes[1], max_size_index))

# for i in other_teams:
#     print(i)
