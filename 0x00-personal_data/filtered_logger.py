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
    """
    Filters message by replacing each value in fields with redaction
    Args:
        fields (List): a list of strings representing all fields to obfuscate
        redaction (str): representing by what the field will be obfuscated
        message (str):  a string representing the log line
        seperator (str): character separating all fields in log `message` line
    Returns:
        message (str): the filtered `message` log line
    """
    for key in fields:
        pattern = r'({0}=)([^{1}]*)({1}?)'.format(key, seperator)
        message = re.sub(pattern, r'\1{}\3'.format(redaction), message)
    return message
