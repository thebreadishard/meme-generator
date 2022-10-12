from PIL import Image, ImageDraw, ImageFont
from random import randint

class MemeEngine:
    """Meme generator Class.
    """
    def __init__(self, img_path_out):
        """Initialize MemeEngine object.
        """
        if img_path_out is None:
            raise Exception("Where should the image be saved?")
        else:
            self.img_path_out = img_path_out

    def make_meme(self, path, text=None, author=None, crop=None, width=500):
        """Create a Meme With a Quote.

        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- the body of the quote
            author {str} -- the author of the quote
            crop {tuple} -- The crop rectangle, as a (left, upper, right,
                lower)-tuple. Default=None.
            width {int} -- The pixel width value. Default=500.
        Returns:
            str -- the file path to the output image.
        """
        img = Image.open(path)

        if crop is not None:
            img = img.crop(crop)

        if width is not None:
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        if text is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=30)
            draw.text((randint(10, 100), randint(10, 100)), text,
                      font=font, fill='white')

        if author is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=30)
            draw.text((randint(110, 200), randint(110, 200)), author,
                      font=font, fill='white')

        img.save(self.img_path_out)

        return self.img_path_out
