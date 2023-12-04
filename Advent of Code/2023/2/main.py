import re


def get_games(file_contents):
    games = []
    for game in file_contents:
        search_string = r'(\d+) (\w+)'
        game = game.split(':')[1].split(';')
        current_game = {'red': 0, 'green': 0, 'blue': 0}
        for turn in game:
            extractions = (re.findall(search_string, turn))
            for e in extractions:
                if int(e[0]) > current_game[e[1]]:
                    current_game[e[1]] = int(e[0])
        games.append(current_game)
    return games


def part1(file_contents):
    target = {'red': 12, 'green': 13, 'blue': 14}
    s = 0
    for index, game in enumerate(get_games(file_contents)):
        if all(game[color] <= target[color] for color in target.keys()):
            s += index + 1
    return s


def part2(file_contents):
    return sum(game['red'] * game['green'] * game['blue'] for game in get_games(file_contents))
