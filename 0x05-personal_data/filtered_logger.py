#!/usr/bin/env python3
"""filtered_logger"""


import re
from typing import List
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.f = fields

    def format(self, record: logging.LogRecord) -> str:
        """format the record"""
        form = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.f, self.REDACTION, form, self.SEPARATOR)

    def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
        """function that returns the log message obfuscated"""
        for field in fields:
            message = re.sub(rf"{field}=.*?{separator}",
                             f"{field}={redaction}{separator}", message)
        return message
