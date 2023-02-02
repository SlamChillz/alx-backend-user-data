#!/usr/bin/env python3
"""
Defines a function that filters logs
"""
import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str,
    message: str, seperator: str
) -> str:
    """Filters message by replacing each value in fields with redaction"""
    for key in fields:
        pattern = r'({0}=)([^{1}]*)({1})'.format(key, seperator)
        message = re.sub(pattern, r'\1{}\3'.format(redaction), message)
    return message
