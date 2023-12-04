CARDS = {c: i + 2 for i, c in enumerate('23456789TJQKA')}


def read_file_contents(file_contents):
    hands = []
    bids = []

    for index, line in enumerate(file_contents):
        line = line.split(' ')
        hands.append({'hand': line[0]})
        bids.append(int(line[1]))

    return hands, bids


def get_win_type(counter_results):
    if max(counter_results) == 5:
        return 5
    elif max(counter_results) == 4:
        return 4
    elif max(counter_results) == 3 and 2 in counter_results:
        return 3
    elif max(counter_results) == 3:
        return 2
    elif list(counter_results).count(2) == 2:
        return 1
    elif max(counter_results) == 2:
        return 0
    else:
        return -1


def compute_total_winnings(hands):
    ranking = sorted(hands, key=lambda x: (x['win_type'], *(CARDS[x['hand'][i]] for i in range(5))))
    return sum((i + 1) * r['bid'] for i, r in enumerate(ranking))


def part1(file_contents):
    hands, bids = read_file_contents(file_contents)

    for index, hand in enumerate(hands):
        hand['bid'] = bids[index]
        counter = {card: hand['hand'].count(card) for card in hand['hand']}
        hand['win_type'] = get_win_type(counter.values())

    return compute_total_winnings(hands)


def part2(file_contents):
    CARDS['J'] = 1
    hands, bids = read_file_contents(file_contents)

    for index, hand in enumerate(hands):
        hand['bid'] = bids[index]

        if hand['hand'] == 'JJJJJ':
            hand['win_type'] = 5
        else:
            counter = {card: hand['hand'].count(card) for card in hand['hand'] if card != 'J'}
            hand['win_type'] = get_win_type(counter.values())
            jokers = hand['hand'].count('J')

            for _ in range(jokers):
                if hand['win_type'] in [-1, 3, 4]:
                    hand['win_type'] += 1
                elif hand['win_type'] in [0, 1, 2]:
                    hand['win_type'] += 2

    return compute_total_winnings(hands)
