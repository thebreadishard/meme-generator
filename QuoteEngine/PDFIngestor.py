from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Import quotes from a pdf-document."""
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Turn pdf into text,
         and read the text file line by line to make a list of quotes."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./tmp/{random.randint(0, 1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split(' - ')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
