#!/usr/bin/env python3

from unittests import assert_equals
from input import readFile

def main():
    seats = readFile("inputs/day5.txt")
    print(findHighest(seats))

def findHighest(seats):
    max = 0
    for s in seats:
        n = id(s)
        if n > max:
            max = n
    return max


def id(seat):
    r = row(seat[0:7])
    l = line(seat[7:10])
    return 8 * r + l


def tests():
    assert_equals(0, row("F"))
    assert_equals(1, row("B"))
    assert_equals(2, row("BF"))
    assert_equals(44, row("FBFBBFF"))
    assert_equals(5, line("RLR"))
    assert_equals(357, id("FBFBBFFRLR"))
    assert_equals(1023, id("BBBBBBBRRR"))

def row(s):
    return binary(s, 'B')

def line(s):
    return binary(s, 'R')

def binary(s, one):
    result = 0
    for c in s:
        result *= 2
        if c == one:
            result += 1
    return result


tests()
main()
