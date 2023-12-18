def read_maps(file_contents):
    maps = []
    current_map = []
    for line in file_contents:
        if line == '\n':
            maps.append(current_map)
            current_map = []
        else:
            current_map.append(line.rstrip())
    maps.append(current_map)
    return maps


def transpose_matrix(mat):
    return [''.join(s) for s in zip(*mat)]


def diff_letters(a, b):
    return sum(a[i] != b[i] for i in range(len(a)))


def diff_matrix(mat):
    return sum(diff_letters(mat[index], mat[len(mat) - 1 - index]) for index in range((len(mat) - 1) // 2 + 1))


def find_mirror(input_map, diff):
    for mirror_edge in range(len(input_map) - 1):
        size = min(mirror_edge + 1, len(input_map) - mirror_edge - 1)
        if diff_matrix(input_map[mirror_edge - size + 1:mirror_edge + size + 1]) == diff:
            return mirror_edge + 1
    return -1


def solve(file_contents, diff):
    maps = read_maps(file_contents)
    res_row = 0
    res_col = 0

    for current_map in maps:
        res = find_mirror(current_map, diff)
        if res != -1:
            res_row += res
        else:
            tm = transpose_matrix(current_map)
            res_col += find_mirror(tm, diff)

    return res_row * 100 + res_col


def part1(file_contents):
    return solve(file_contents, 0)


def part2(file_contents):
    return solve(file_contents, 1)
