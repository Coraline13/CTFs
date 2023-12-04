import re


def part1(file_contents):
    cards = {}
    for index, card in enumerate(file_contents):
        numbers = card.split(':')[1].strip().split('|')
        cards[index + 1] = {
            'winning_numbers': re.findall(r'\w+', numbers[0]),
            'my_numbers': re.findall(r'\w+', numbers[1]),
        }

    total = 0
    for card in cards:
        cards[card]['points'] = 0
        for nb in cards[card]['my_numbers']:
            if nb in cards[card]['winning_numbers']:
                cards[card]['points'] = cards[card]['points'] * 2 if cards[card]['points'] > 0 else 1
        total += cards[card]['points']

    return total


def part2(file_contents):
    cards = []
    for index, card in enumerate(file_contents):
        numbers = card.split(':')[1].strip().split('|')
        cards.append({
            'winning_numbers': re.findall(r'\w+', numbers[0]),
            'my_numbers': re.findall(r'\w+', numbers[1]),
        })

    for index, card in enumerate(cards):
        wins = 0
        card['cards_won'] = []
        for nb in card['my_numbers']:
            if nb in card['winning_numbers']:
                wins += 1
                card['cards_won'].append(index + wins)

    return recursive_cards(cards, list(range(len(cards))))


def recursive_cards(all_cards, cards_index_list):
    if not cards_index_list:
        return 0

    total = 0
    for c in cards_index_list:
        total += recursive_cards(all_cards, all_cards[c]['cards_won']) + 1
    return total
