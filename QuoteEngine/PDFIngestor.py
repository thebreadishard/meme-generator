"""PDF Ingestor of the Quote Engine module."""

from typing import List
import subprocess
import os
import random

from .TextIngestor import TextIngestor
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Import quotes from a pdf-document."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Turn pdf into text.

        And read the text file line by line to make a list of quotes.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./tmp/{random.randint(0, 1000000)}.txt'
        with open(tmp, 'w') as fp:
            pass

        cmd = f"./pdftotext -layout -nopgbrk {path} {tmp}"
        subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        quotes = TextIngestor.parse(tmp)
        os.remove(tmp)
        return quotes
