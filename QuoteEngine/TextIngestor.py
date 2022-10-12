"""Text Ingestor of the Quote Engine module."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Import quotes from a txt-file."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Read the text file line by line to make a list of quotes."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, 'r') as f:
            for line in f:
                if line != "":
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)

        return quotes
