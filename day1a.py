#!/usr/bin/env python3

def main():
    numbers = readFile("inputs/day1a.txt")
    a, b = findPair(numbers, 2020)
    print(a * b)

    a, b, c = findTriplet(numbers, 2020)
    print(a * b * c)

def readFile(f):
    with open(f, 'r') as fh:
        return [int(l) for l in fh.readlines()]


def findPair(numbers, sum):
    for a in numbers:
        for b in numbers:
            if a + b == sum:
                return a, b

def findTriplet(numbers, sum):
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if a + b + c == sum:
                    return a, b, c

main()
