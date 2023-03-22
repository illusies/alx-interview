#!/usr/bin/python3
"""
A function that returns a list of lists of integers representing the
Pascal’s triangle of n
"""

def pascal_triangle(n):
    """A function that returns an empty list if n <= 0"""
    a = []
    if n <= 0:
        return a

    for i in range(n):
        b = [1]
        if a:
            for j in range(i):
                b.append(sum(a[-1][j:j+2]))
        a.append(b)
    return a
