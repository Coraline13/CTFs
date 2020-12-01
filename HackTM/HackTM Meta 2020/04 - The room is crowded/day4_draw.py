import PIL.ImageDraw as ImageDraw, PIL.Image as Image, PIL.ImageShow as ImageShow

with open('teams.in', 'r') as input_file:
    counter = 0
    for line in input_file:
        if counter == 0:
            n = int(line)
            other_teams = []
        elif counter == n + 1:
            my_team_size = int(line)
        else:
            size, pos = line.split(' ')
            other_teams.append(list(map(float, line.split(' '))))
        counter += 1

im = Image.new("RGB", (2000, 2000), (255, 255, 255))
draw = ImageDraw.Draw(im)
colors = [(0, 0, 0), (255, 255, 0), (0, 255, 255), (0, 0, 255)]
j = 0
first_greater_than_260 = 0
first_greater_than_270 = 0
for i in other_teams:
    start = i[1] - i[0] / 2
    if not first_greater_than_270 and start > 270:
        first_greater_than_270 = 1
        print('270: {0}'.format(i))
        draw.pieslice((100, 100, 1900, 1900), start, start + i[0], fill=(0, 255, 0))
    if not first_greater_than_260 and start > 260:
        first_greater_than_260 = 1
        print('260: {0}'.format(i))
        draw.pieslice((100, 100, 1900, 1900), start, start + i[0], fill=(0, 128, 0))
    # else:
    # draw.pieslice((100, 100, 1900, 1900), start, start + i[0], fill=colors[j])
    j = (j + 1) % len(colors)

draw.line((1000, 0, 1000, 2000), fill=255, width=5)
draw.line((0, 1000, 2000, 1000), fill=255, width=5)
im.show()
