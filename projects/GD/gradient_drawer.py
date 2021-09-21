from PIL import Image, ImageDraw

image = Image.new("RGB", (128, 128), (255, 255, 255))
draw = ImageDraw.Draw(image)

shift = 0
for x in range(128):
    for y in range(128):
        c = 255 - y - shift
        draw.point((x, y), (127, c, c//2))
    shift += 1

del draw
image.save("./test.png", "PNG")
