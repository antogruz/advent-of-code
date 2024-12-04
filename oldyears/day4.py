#!/usr/bin/env python3

from valid import countValids
from passport import SimplePassport, ComplexPassport
from input import readFileByBlocks

def main():
    input = readFileByBlocks("inputs/day4.txt")
    simplePassports = [SimplePassport(s) for s in input]

    print(countValids(simplePassports))

    complexPassports = [ComplexPassport(s) for s in input]
    print(countValids(complexPassports))



main()
