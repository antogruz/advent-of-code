#!/usr/bin/env python3

from map import Map

def main():
    input = readFile("inputs/day3.txt")

    trees = []
    for move in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        map = Map(input)
        trees.append(countTrees(map, move))

    product = 1
    for t in trees:
        product *= t

    print(product)


def countTrees(map, move):
    count = 0
    while not map.end():
        if map.tree():
            count += 1
        map.move(move[0], move[1])

    return count


def readFile(f):
    with open(f) as fh:
        return fh.read().splitlines()

main()
