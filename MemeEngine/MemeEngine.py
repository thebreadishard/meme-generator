from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """Meme generator Class."""

    def __init__(self, out_img_path):
        if out_img_path is None:
            raise Exception("Where should the image be saved?")
        else:
            self.out_img_path = out_img_path

    def make_meme(self, img_path, text=None, author=None, crop=None, width=500):
        """Create a Meme With a Quote

        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- the body of the quote
            author {str} -- the author of the quote
            crop {tuple} -- The crop rectangle, as a (left, upper, right, lower)-tuple. Default=None.
            width {int} -- The pixel width value. Default=500.
        Returns:
            str -- the file path to the output image.
        """
        img = Image.open(img_path)

        if crop is not None:
            img = img.crop(crop)

        if width is not None:
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        if text is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
            draw.text((10, 30), text, font=font, fill='white')

        if author is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
            draw.text((20, 40), author, font=font, fill='white')

        img.save(self.out_img_path)
        return self.out_img_path


if __name__ == '__main__':
    print(make_meme('./imgs/img.jpg',
                    './imgs/out.jpg',
                    'woof!',
                    (450, 900, 900, 1300),
                    200))
