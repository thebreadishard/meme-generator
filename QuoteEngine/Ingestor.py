"""All ingestors are packaged into a main Ingestor class."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """Main Ingestor class.

    This class encapsulates all the ingestors to provide one interface to
    load any supported file type.
    """

    importers = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file to get a list of quotes."""
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
