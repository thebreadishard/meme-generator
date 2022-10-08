class QuoteModel:
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        """Create a new Quote.
        :param body: a str text, the message of the quote.
        :param author: a str text, the author of the quote.
        """
        return f'{self.body} - {self.author}'

    def __repr__(self):
        """Return `repr(self)`.
        a computer-readable string representation of this object.
        """
        return f'<{self.body}, {self.author}>'
