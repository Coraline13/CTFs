class Team(object):
    counter = 1

    def __init__(self, size: float, position: float) -> None:
        self.size = size
        self.position = position
        self.start = position - size / 2
        self.end = position + size / 2
        self.id = Team.counter
        Team.counter += 1

    def __repr__(self):
        return 'Team {0}: size={1}, pos={2}, start={3}, end={4}\n'.format(self.id, self.size, self.position, self.start, self.end)


class Gap(object):
    counter = 1

    def __init__(self, team_left: Team, team_right: Team, size: float) -> None:
        self.team_left = team_left
        self.team_right = team_right
        self.size = size
        self.id = Gap.counter
        Gap.counter += 1

    def __repr__(self):
        return 'Gap {0}: size={1}, team_left={2}, team_right={3} team_right_size={4}\n'.format(self.id, self.size, self.team_left.id,
                                                                                               self.team_right.id, self.team_right.size)


def try_moves(x, y):
    default_dif = max_gap
    size_gr = 0
    dif_gr = 0
    best_cost = 99999
    history = []
    cost = 0

    for gr in list(list(range(y, n + 1)) + list(range(1, max_size_index))):
        dif_gl = 0
        size_gr += gaps[gr - 1].team_left.size
        dif_gr += gaps[gr - 1].size
        cost += gaps[gr - 1].team_left.size * gaps[gr - 1].size
        total_dif = default_dif + dif_gr + dif_gl
        gl = x - 1
        cost_gl = 0

        while total_dif < my_team_size:
            dif_gl += gaps[gl - 1].size
            cost_gl += gaps[gr - 1].team_right.size * gaps[gl - 1].size
            total_dif = default_dif + dif_gr + dif_gl
            gl = 1 if gl == n else gl - 1

        if total_dif < my_team_size:
            continue
        cost_gl -= (total_dif - my_team_size) * gaps[gr - 1].team_right.size

        if cost + cost_gl < best_cost:
            best_cost = cost + cost_gl
            history = [gl + 1, gr]

        print(f'{cost=} {best_cost=} {gr=} {gl=}')

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

gaps = []
for t in range(1, len(other_teams)):
    if t == n:
        gaps.append(Gap(other_teams[n], other_teams[1], 360 - other_teams[n].end + other_teams[1].start))
    else:
        gaps.append(Gap(other_teams[t], other_teams[t + 1], other_teams[t + 1].start - other_teams[t].end))

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

gaps_left = list(reversed(gaps[19:34]))
gaps_right = gaps[35:] + gaps
# print(try_moves(max_gap_indexes[0], max_gap_indexes[1]))


for i in range(len(gaps_left)):
    cost = 0
    size_left = 0
    gaps_plm_left = 0
    for gap in gaps_left[:i]:
        size_left += gap.team_right.size
        cost += size_left * gap.size
        gaps_plm_left += gap.size
    dif = my_team_size - max_gap - gaps_plm_left

    size_right = 0
    if dif <= 0:
        break

    for gap_right in gaps_right:
        if dif <= 0:
            print(gap_right)
            break

        plm = min(dif, gap_right.size)
        size_right += gap_right.team_left.size
        dif -= plm
        cost += size_right * plm

    print(f'cost when {i} gaps from left: {cost}')
