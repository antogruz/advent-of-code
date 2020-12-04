#!/usr/bin/env python3

from map import Map

def main():
    input = readFile("inputs/day3.txt")
    print(input)
    map = Map(input)
    count = 0
    while not map.end():
        if map.tree():
            count += 1
        map.move(3, 1)

    print(count)

def readFile(f):
    with open(f) as fh:
        return fh.read().splitlines()

main()
