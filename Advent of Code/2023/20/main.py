FLIP_FLOP = '%'
CONJUNCTION = '&'
ON = True
OFF = False
LOW = 1
HIGH = 2
MAX_ROUNDS = 1000000


def read_module_configuration(file_contents):
    module_configuration = {}
    for line in file_contents:
        split_line = line.rstrip().split(' -> ')

        if (module_type := split_line[0][0]) == FLIP_FLOP:
            module_configuration[split_line[0][1:]] = {
                'type': FLIP_FLOP,
                'destination': split_line[1].split(', '),
                'state': OFF,
                'pulses': [None] * MAX_ROUNDS,
            }

        elif module_type == CONJUNCTION:
            module_configuration[split_line[0][1:]] = {
                'type': CONJUNCTION,
                'destination': split_line[1].split(', '),
                'input_modules': {},
                'pulses': [None] * MAX_ROUNDS,
            }

        else:
            module_configuration[split_line[0]] = {
                'type': 'broadcaster',
                'destination': split_line[1].split(', '),
                'pulses': [None] * MAX_ROUNDS,
            }

    for module in module_configuration:
        if module_configuration[module]['type'] == CONJUNCTION:
            for m in module_configuration:
                if module in module_configuration[m]['destination']:
                    module_configuration[module]['input_modules'][m] = LOW

    return module_configuration


def get_next_pulse(module_configuration, module, pulse, step):
    mod = module_configuration[module]
    if mod['type'] == FLIP_FLOP:
        if pulse == LOW:
            if mod['state'] == OFF:
                mod['state'] = ON
                return HIGH
            else:
                mod['state'] = OFF
                return LOW
        else:
            return None

    if mod['type'] == CONJUNCTION:
        if all(im == HIGH for im in mod['input_modules'].values()):
            return LOW
        else:
            return HIGH

    if mod['type'] == 'broadcaster':
        return pulse

    return None


def part1(file_contents):
    module_configuration = read_module_configuration(file_contents)
    step = 0

    for _ in range(1000):
        current_modules = {'broadcaster'}
        module_configuration['broadcaster']['pulses'][step] = LOW

        while current_modules:
            next_modules = set()
            for module in current_modules:
                next_pulse = get_next_pulse(
                    module_configuration,
                    module,
                    module_configuration[module]['pulses'][step],
                    step,
                )
                if next_pulse:
                    for dest in module_configuration[module]['destination']:
                        if dest not in module_configuration:
                            module_configuration[dest] = {
                                'type': None,
                                'destination': [],
                                'pulses': [None] * MAX_ROUNDS,
                            }
                        elif module_configuration[dest]['type'] == CONJUNCTION:
                            module_configuration[dest]['input_modules'][module] = next_pulse
                        module_configuration[dest]['pulses'][step + 1] = next_pulse
                        next_modules.add(dest)
            step += 1
            current_modules = next_modules
    lows = sum(1 for mod in module_configuration.values() for p in mod['pulses'] if p == LOW)
    highs = sum(1 for mod in module_configuration.values() for p in mod['pulses'] if p == HIGH)
    return lows * highs


def part2(file_contents):
    for line in file_contents:
        pass

    return None


if __name__ == '__main__':
    print(part1(open('example_part1.txt', 'rt')))
