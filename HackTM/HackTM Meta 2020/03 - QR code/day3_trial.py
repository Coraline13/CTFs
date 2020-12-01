# from PIL import Image
#
# picture = Image.open("day3_input.png")
#
# # Get the size of the image
# width, height = picture.size
#
# # print(width, height)
#
# # Process every pixel
# for x in range(width):
#     for y in range(height):
#         print(picture.getpixel((x, y)))


from PIL import Image


def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


img = Image.open('day3_input.png')

if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
    pixels = img.convert('RGBA').load()
    width, height = img.size
    print(width, height)

    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]
            print('plm')
            print('x = %s, y = %s, hex = %s' % (x, y, rgb2hex(r, g, b)))
