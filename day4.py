#!/usr/bin/env python3

from valid import countValids
from passport import SimplePassport, ComplexPassport

def main():
    input = readFile("inputs/day4.txt")
    simplePassports = [SimplePassport(s) for s in input]

    print(countValids(simplePassports))

    complexPassports = [ComplexPassport(s) for s in input]
    print(countValids(complexPassports))


def readFile(f):
    with open(f) as fh:
        return fh.read().split("\n\n")


main()
