class QuoteModel(body, author):
    def __init__(self):
        self.body = body
        self.author = author

    def __repr__(self):
        return f'{self.body} - {self.author}'
