#!/usr/bin/env python3

from map import Map

def main():
    input = readFile("inputs/day3.txt")
    map = Map(input)

    print(countTrees(map, (3, 1)))


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
