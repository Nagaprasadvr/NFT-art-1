import PIL
from PIL import Image, ImageDraw, ImageChops
import random


def color_rand():

    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color

def art():
    thickness = 1
    points = []
    print("ntfs")
    target = 256
    scale = 2
    img_size_px = target * scale
    padding_px = 12 * scale
    bg_color = (0, 0, 0)
    start_color = color_rand()
    end_color = color_rand()
    image = Image.new(mode="RGB", size=(img_size_px, img_size_px), color=bg_color)
    draw = ImageDraw.Draw(image)
    for _ in range(10):
        random_point = (random.randint(padding_px, img_size_px-padding_px), random.randint(padding_px, img_size_px-padding_px))
        points.append(random_point)
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = min([p[1] for p in points])
    #draw.rectangle((min_x, min_y, max_x, max_y), outline=(255, 0, 0))
    delta_x = min_x - (img_size_px - max_x)
    delta_y = min_y - (img_size_px - max_y)

    for i, point in enumerate(points):
        points[i] = ((point[0] - delta_x) // 1, point[1])

    for i, point in enumerate(points):
        overimage = Image.new(mode="RGB", size=(img_size_px, img_size_px), color=bg_color)
        overdraw = ImageDraw.Draw(overimage)
        p1 = point
        if i == len(points)-1:
            p2 = points[0]
        else:
            p2 = points[i+1]

        line_xy = (p1, p2)
        thickness += 1 * scale
        line_color= (0,0,0)
        overdraw.line(line_xy, fill=color_rand(), width=thickness)
        image = ImageChops.add(image, overimage)
    image.resize((target, target), resample=Image.ANTIALIAS)
    image.save("test.png")


if __name__ == "__main__":
    art()


