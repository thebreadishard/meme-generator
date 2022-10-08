from PIL import Image, ImageDraw, ImageFont


def make_meme(in_path, out_path, body=None, author=None, crop=None, width=None):
    """Create a Meme With a Quote

    Arguments:
        in_path {str} -- the file location for the input image.
        out_path {str} -- the desired location for the output image.
        crop {tuple} -- The crop rectangle, as a (left, upper, right, lower)-tuple. Default=None.
        width {int} -- The pixel width value. Default=None.
    Returns:
        str -- the file path to the output image.
    """
    img = Image.open(in_path)

    if crop is not None:
        img = img.crop(crop)

    if width is not None:
        if width > 500:
            raise Exception('Width must be 500 or less.')
        else:
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

    if body is not None:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
        draw.text((10, 30), body, font=font, fill='white')

    if author is not None:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
        draw.text((20, 40), author, font=font, fill='white')

    img.save(out_path)
    return out_path


if __name__ == '__main__':
    print(make_meme('./imgs/img.jpg',
                    './imgs/out.jpg',
                    'woof!',
                    (450, 900, 900, 1300),
                    200))
