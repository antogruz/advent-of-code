#!/usr/bin/env python3

from unittests import *
from input import *

def main():
    reports = parseReports()
    print(countSafeReports(reports, 0))
    print(countSafeReports(reports, 1))

def countSafeReports(reports, chances):
    return len([ r for r in reports if isSafe(r, chances)])

def isSafe(report, chances):
    if chances <= 0:
        return wasSafe(report)
    for i, element in enumerate(report):
        subReport = [ x for j, x in enumerate(report) if j != i ]
        if wasSafe(subReport):
            return True
    return False

class Checker:
    def __init__(self, chances):
        self.direction = 0
        self.lastNumber = "ff"
        self.chances = chances

    def nextElementStillValid(self, e):
        if self.chances < 0:
            return False
        if not self.check(e):
            if self.chances > 0:
                self.chances -= 1
                return True
            else:
                return False
        self.lastNumber = e
        return True

    def check(self, e):
        if self.lastNumber == "ff":
            return True
        if self.direction == 0:
            self.direction = 1 if self.lastNumber < e else -1
            return self.checkDistance(e)
        if not sameDirection(self.direction, self.lastNumber, e):
            return False
        return self.checkDistance(e)

    def checkDistance(self, e):
        if distance(self.lastNumber, e) not in [-3, -2, -1, 1, 2, 3]:
            return False
        return True


def sameDirection(direction, a, b):
    if direction > 0:
        return a <= b
    else:
        return a > b

def distance(a, b):
    if a > b:
        return a - b
    return b - a


def wasSafe(report):
    distances = [ int(report[i]) - int(report[i+1]) for i in range(0, len(report) - 1) ]
    if not sameSign(distances):
        return False
    if forbiddenDistance(distances):
        return False
    return True

def sameSign(distances):
    if distances[0] >= 0:
        return checkAllPositives(distances)
    return checkAllNegatives(distances)

def checkAllPositives(l):
    for e in l:
        if e < 0:
            return False
    return True

def checkAllNegatives(l):
    for e in l:
        if e > 0:
            return False
    return True

def forbiddenDistance(distances):
    for d in distances:
        if d == 0 or d > 3 or d < -3:
            return True
    return False

def parseReports():
    lines = readLines("inputs/day2.txt")
    return [ line.split() for line in lines ]

class Tester:
    def testBigRange(self):
        assertEquals(False, isSafe([32, 40], 0))


main()
runTests(Tester())
