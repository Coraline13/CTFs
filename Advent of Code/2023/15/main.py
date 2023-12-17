import re


def get_hash(input_str):
    current_value = 0
    for ch in input_str:
        current_value = ((current_value + ord(ch)) * 17) % 256
    return current_value


def part1(file_contents):
    return sum(get_hash(s) for s in file_contents.readlines()[0].rstrip().split(','))


def part2(file_contents):
    boxes = [[] for _ in range(256)]

    for s in file_contents.readlines()[0].rstrip().split(','):
        prefix = re.split(r'=|-', s)[0]
        current_box = boxes[get_hash(prefix)]
        if '=' in s:
            for idx, elem in enumerate(current_box):
                if s.split('=')[0] in elem:
                    current_box[idx] = s
                    break
            else:
                current_box.append(s)
        elif '-' in s:
            current_box[:] = [x for x in current_box if s[:-1] not in x]

    return sum(
        box_idx * elem_idx * int(elem.split('=')[1])
        for box_idx, box in enumerate(boxes, start=1)
        for elem_idx, elem in enumerate(box, start=1)
    )
