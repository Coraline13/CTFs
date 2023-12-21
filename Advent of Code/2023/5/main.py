import re


def part1(file_contents):
    chain = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
    file_contents = file_contents.read()
    seeds = [int(s) for s in file_contents.split('\n')[0][7:].split(' ')]
    pattern_string = r'(?P<source>\w+)-to-(?P<dest>\w+) map:\n(?P<values>(?:(?:\d+\s){3})+)'
    val = re.findall(pattern_string, file_contents[2:])
    almanac = {}
    for i in val:
        lst = []
        for row in i[2].split('\n'):
            row = row.split(' ')
            if len(row) < 3:
                continue
            lst.append({
                'dest_start': int(row[0]),
                'source_start': int(row[1]),
                'range': int(row[2]),
            })
        almanac[(i[0], i[1])] = lst

    locations = []
    for seed in seeds:
        current_value = seed
        for index, stage in enumerate(chain[:-1]):
            for values in almanac[(chain[index], chain[index + 1])]:
                if values['source_start'] <= current_value < (values['source_start'] + values['range']):
                    current_value += (values['dest_start'] - values['source_start'])
                    break
        locations.append(current_value)

    return min(locations)
