import logging
from logging import LogRecord


class MinLenFilter(logging.Filter):
    def filter(self, record: LogRecord) -> bool:
        return len(record.getMessage()) > 10  # if True-> Hast! else, Nist!
