"""The interface to each of the different Ingestors."""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Ingestor interface class."""

    allowed_extensions = []

    @classmethod
    @abstractmethod
    def can_ingest(cls, path):
        """See if the file can be ingested."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse as defined in each Ingestor."""
        pass
