"""QuoteModel is the object in which quotes are stored."""

class QuoteModel:
    def __init__(self, body, author):
        """Create a new Quote.

        :param body: a str text, the message of the quote.
        :param author: a str text, the author of the quote.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        return f'{self.body} - {self.author}'
