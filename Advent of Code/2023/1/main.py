import re

DIGITS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def get_num(s):
    if not s.isdigit():
        if s in DIGITS:
            return DIGITS[s]
        if s[::-1] in DIGITS:
            return DIGITS[s[::-1]]
    return s


def part1(file_contents):
    s = 0
    for line in file_contents:
        search_pattern = r'\d'
        first = (re.search(search_pattern, line)).group(0)
        second = (re.search(search_pattern, line[::-1])).group(0)
        s += int(f'{first}{second}')
    return str(s)


def part2(file_contents):
    search_string = rf'\d|{"|".join(DIGITS.keys())}'
    search_string_reversed = rf'\d|{"|".join(d[::-1] for d in DIGITS.keys())}'
    s = 0
    for line in file_contents:
        first = get_num((re.search(search_string, line)).group(0))
        second = get_num((re.search(search_string_reversed, line[::-1])).group(0))
        s += int(f'{first}{second}')
    return str(s)
