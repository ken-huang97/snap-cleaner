from PIL import Image
from PIL import ImageDraw
from sys import argv
import argparse
import os.path
import sys

def remove_rec(im, y1, y2, alpha):
    pixels = im.load()
    for i in range(im.size[0]):
        for j in range(y1, y2+1):
            new_color = tuple([int(v/(1-alpha)) for v in pixels[i,j]])
            pixels[i,j]=new_color

def draw_rec(im, y1, y2):
    rec = Image.new('RGBA', im.size, (255,255,255,0))

    rec_loc = (0, y1, im.size[0], y2)
    draw = ImageDraw.Draw(rec)

    draw.rectangle(rec_loc, fill=(0,0,0,128))

    return Image.alpha_composite(im, rec)

def stitch_imgs(*images):
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
      new_im.paste(im, (x_offset,0))
      x_offset += im.size[0]

    return new_im

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "y1",
        nargs='?',
        default=685,
        help="top of rectangle",
        type=int
        )
    parser.add_argument(
        "y2",
        nargs='?',
        default=753,
        help="bottom of rectangle",
        type=int
    )
    parser.add_argument(
        "--img",
        "-i",
        default="test_images/snap_test.jpg",
        help="input image",
    )
    parser.add_argument(
        "--out",
        "-o",
        default="stitched_out.jpg",
        help="output file"
    )
    parser.add_argument(
        "--alpha",
        "-a",
        default=0.6,
        help="rectangle alpha",
        type=float
    )
    parser.add_argument(
        "--show",
        "-s",
        help="open image",
        action="store_true"
    )

    return parser.parse_args()

def main():
    args=get_args()

    img_name=args.img
    out_name=args.out
    y1, y2 = args.y1, args.y2
    alpha = args.alpha
    show_img = args.show

    if not os.path.isfile(img_name):
        sys.exit("File {} does not exist".format(img_name))
    print("Fixing " + img_name)

    im = Image.open(img_name)
    if not im:
        sys.exit("input image '{}' not found".format(img_name))

    new_im = im.copy()
    remove_rec(new_im, y1, y2, alpha)
    stitched_im = stitch_imgs(im, new_im)

    print("Saving stitched before/after pic to " + out_name)
    stitched_im.save(out_name)

    if show_img:
        stitched_im.show()

def snap_test():
    im = Image.open("snap_test.jpg").convert('RGBA')

    y1, y2 = 690, 750

    draw_rec(im, y1, y2).show()

main()
