CARDS = {c: i for i, c in enumerate('23456789TJQKA', start=2)}
FIVE_OF_A_KIND = 5
FOUR_OF_A_KIND = 4
FULL_HOUSE = 3
THREE_OF_A_KIND = 2
TWO_PAIR = 1
ONE_PAIR = 0
HIGH_CARD = 0


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
        return FIVE_OF_A_KIND
    elif max(counter_results) == 4:
        return FOUR_OF_A_KIND
    elif max(counter_results) == 3 and 2 in counter_results:
        return FULL_HOUSE
    elif max(counter_results) == 3:
        return THREE_OF_A_KIND
    elif list(counter_results).count(2) == 2:
        return TWO_PAIR
    elif max(counter_results) == 2:
        return ONE_PAIR
    else:
        return HIGH_CARD


def compute_total_winnings(hands):
    ranking = sorted(hands, key=lambda x: (x['win_type'], *(CARDS[c] for c in x['hand'])))
    return sum(i * r['bid'] for i, r in enumerate(ranking, start=1))


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
                if hand['win_type'] in [HIGH_CARD, FOUR_OF_A_KIND]:
                    hand['win_type'] += 1
                elif hand['win_type'] in [ONE_PAIR, TWO_PAIR, THREE_OF_A_KIND]:
                    hand['win_type'] += 2

    return compute_total_winnings(hands)
