"""Meme generator web app."""

import random
import os
import requests
from flask import Flask, render_template, request
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static/image.jpeg')


def setup():
    """Load all resources.
    """
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quote_list = []
    for f in quote_files:
        quote_list.extend(Ingestor.parse(f))

    images_path = "_data/photos/dog/"

    img_list = []
    for root, dirs, files in os.walk(images_path):
        img_list = [os.path.join(root, name) for name in files]

    return quote_list, img_list


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme.
    """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information.
    """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme.

    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form parameters.
    # 3. Remove the temporary saved image.
    """
    image_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    img = None

    try:
        img = requests.get(image_url)
    except requests.exceptions.ConnectionError:
        print('Cannot get image at this URL.')

    tmp_img = './temp.jpg'
    with open(tmp_img, 'wb') as f:
        f.write(img.content)

    path = meme.make_meme(tmp_img, body, author)
    os.remove(tmp_img)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
