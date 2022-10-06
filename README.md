Meme Generator

This project is a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote.

The application interacts with a variety of complex filetypes. It loads quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).  It loads, manipulates, and saves images.
It accepts dynamic user input through a command-line tool and a web service. 

Sample quotes and images of Xander the pup are in src/_data/

A basic flask server consumes the models and make them usable through a web interface. The main code for this flask server is in app.py.

HTML templates are in templates/

Quote Engine

The Quote Engine module is responsible for ingesting many types of files that contain quotes. For our purposes, a quote contains a body and an author:

"This is a quote body" - Author

This module is composed of many classes and demonstrates complex inheritance, abstract classes, classmethods, strategy objects and other fundamental programming principles.

Ingestors

An abstract base class, IngestorInterface, defines two methods with the following class method signatures:

def can_ingest(cls, path: str) -> boolean
def parse(cls, path: str) -> List[QuoteModel]

Separate strategy objects realize IngestorInterface for each file type (csv, docx, pdf, txt).

A final Ingestor class realizes the IngestorInterface abstract base class and encapsulate your helper classes. It should implement logic to select the appropriate helper for a given file based on filetype.

Meme Engine Module

The Meme Engine Module is responsible for manipulating and drawing text onto images. It will reinforce your understanding of object-oriented thinking while demonstrating your skill using a more advanced third party library for image manipulation.

The module loads an image using Pillow (PIL).
It resizes the image so the width is at most 500px and the height is scaled proportionally.
It adds a quote body and a quote author to the image.
It saves the manipulated image.

Package your Application
Larger, complex systems need an interface for users to interact with. We'll package the project as a command line tool and as a simple web service.

Create a Command-Line Interface tool

The project contains a simple cli app starter code in meme.py. This file contains @TODO tasks for you to complete. The utility can be run from the terminal by invoking python3 meme.py

The script must take three optional CLI arguments:

--body a string quote body

--author a string quote author

--path an image path

The script returns a path to a generated image. If any argument is not defined, a random selection is used.

Complete the Flask app

The project contains a flask app starter code in app.py. This file contains @TODO tasks for you to complete.

The app uses the Quote Engine Module and Meme Generator Modules to generate a random captioned image.

It uses the requests package to fetch an image from a user submitted URL.
