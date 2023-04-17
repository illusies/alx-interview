#!/usr/bin/python3
"""
A method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    A function that returns True if data is valid
    UTF-8 encoding or Fales it it is not valid
    """
    data = [n & 255 for n in data]
    try:
        bytes(data).decode()
    except (ValueError, UnicodeError):
        return False
    else:
        return True


if __name__ == "__main__":
    pass
