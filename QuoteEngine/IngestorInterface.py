from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Ingestor interface class."""

    allowed_extensions = []

    @classmethod
    @abstractmethod
    def can_ingest(cls, path):
        """See if we can ingest this."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
