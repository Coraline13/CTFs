import PIL.ImageDraw as ImageDraw, PIL.Image as Image

var = 6000
im = Image.new("RGB", (var * 2, var * 2))
draw = ImageDraw.Draw(im)

old=[]
with open('day10_input_modified.txt', 'r') as input_file:
    for line in input_file:
        x, y, move_x, move_y = [int(i) // 2 for i in line.split(', ')]
        # print(x, y, x + move_x, y + move_y)
        draw.line((var + x, var + y, var + x + move_x, var + y + move_y), fill=(0, 255, 255), width=35)
# draw.line((1000, 0, 1000, 2000), fill=(0, 255, 255), width=15)
# draw.line((var, 0, var, var * 2), fill=255, width=5)
# draw.line((0, var, var * 2, var), fill=255, width=5)
im.show()
