from abc import ABC, abstractmethod


class AbstractMessageLogger(ABC):
    """Abstract writer to access log."""

    def __init__(self, logger):
        self.logger = logger

    @abstractmethod
    def log(self, message, addr):
        """Emit log to logger."""

    @abstractmethod
    def exception(self, addr):
        """Emit log to logger."""
