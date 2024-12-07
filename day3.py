#!/usr/bin/env python3

from unittests import *
from input import *

def main():
    text = readFile("inputs/day3.txt")
    print(text)
    print(computeMults(text))
    print(moreAccurateResults(text))

import re
def moreAccurateResults(text):
    return computeMults(removeSections(text))

def removeSections(text):
    sections = re.split("(don't\(\)|do\(\))", text)
    shouldCompute = True
    onlyValidSections = []
    for section in sections:
        if section == "do()":
            shouldCompute = True
            continue
        if section == "don't()":
            shouldCompute = False
            continue
        if shouldCompute:
            onlyValidSections.append(section)
    return "".join(onlyValidSections)

    print(sections)
    return text

def computeMults(text):
    matches = re.findall(stringToFind(), text)
    return sum([multiply(match) for match in matches])


def multiply(match):
    return int(match[0]) * int(match[1])

def stringToFind():
    oneToThreeDigits = "[0-9]{1,3}"
    return "mul\(({}),({})\)".format(oneToThreeDigits, oneToThreeDigits)


class Tester:
    def testNoMult(self):
        assertEquals(0, computeMults(""))

    def testSimpleMult(self):
        assertEquals(6, computeMults("mul(2,3)"))

    def testTwoMults(self):
        assertEquals(10, computeMults("mul(3,2)mul(1,4)"))

    def testDifferentDigits(self):
        assertEquals(1900, computeMults("mul(19,100)"))

    def testExample(self):
        assertEquals(161, computeMults("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"))

    def testPartTwoExample(self):
        assertEquals(48, moreAccurateResults("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"))
        assertEquals(32, moreAccurateResults("mul(4,8)don't()mul(3,2)"))

runTests(Tester())
main()
