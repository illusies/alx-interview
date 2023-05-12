#!/usr/bin/python3
"""A program that rotates a NxN 2D matric 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """A function that rotates a NxN 2D matrix 90 degrees clockwise"""
    size = len(matrix)
    for y in range(size // 2):
        end = size - 1
        for x in range(y, end - y):
            temp = matrix[y][x]
            matrix[y][x] = matrix[end - x][y]
            matrix[end - x][y] = matrix[end - y][end - x]
            matrix[end - y][end - x] = matrix[x][end - y]
            matrix[x][end - y] = temp


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
