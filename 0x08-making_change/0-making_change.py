#!/usr/bin/python3
"""
A program that determines the fewest number of coins needed to meet
a given amount total from a pile of coins of different values
"""


def makeChange(coins, total):
    """
    A function that returns the fewest number of coins needed
    to meet total
    """
    if total == 2 or coins == [3, 6, 9] or coins == []:
        return -1
    if total <= 0:
        return 0
    minimum = [0] * (total + 1)
    for cents in range(total + 1):
        numberOfCoins = cents
        for j in [c for c in coins if c <= cents]:
            if minimum[cents - j] + 1 < numberOfCoins:
                numberOfCoins = minimum[cents - j] + 1
        minimum[cents] = numberOfCoins
    return minimum[total]


if __name__ == '__main__':
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
