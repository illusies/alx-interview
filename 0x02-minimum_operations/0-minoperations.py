#!/usr/bin/python3
"""
A method that calculates the fewest number of operations needed to
result in exactly n H characters in the file.
"""

def minOperations(n):
    calc = n // 2
    while calc > 0:
        q, r = divmod(n, calc)
        if (r == 0):
            return q + minOperations(calc)
        calc -= 1
    return 0
