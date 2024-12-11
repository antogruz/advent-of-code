#!/usr/bin/env python3

from unittests import *
from input import *

def main():
    text = readFile("inputs/day8.txt")
    print(countAntinodes(text))
    print(countResonances(text))

def countAntinodes(text):
    detector = AntennasDetector(text)
    map = AntinodesMap(text)
    for antennasGroup in detector.getAntennas():
        antinodes = findAntinodes(antennasGroup)
        for a in antinodes:
            map.appendAntinode(a[0], a[1])
    return map.countAntinodes()

def countResonances(text):
    detector = AntennasDetector(text)
    map = AntinodesMap(text)
    for antennasGroup in detector.getAntennas():
        antinodes = findResonances(antennasGroup, map.I, map.J)
        for a in antinodes:
            map.appendAntinode(a[0], a[1])
    return map.countAntinodes()

class AntinodesMap:
    def __init__(self, text):
        lines = text.splitlines()
        self.I = len(lines)
        self.J = len(lines[0])
        self.antinodes = []

    def appendAntinode(self, i, j):
        if i < 0 or i >= self.I or j < 0 or j >= self.J:
            return
        if (i, j) in self.antinodes:
            return
        self.antinodes.append((i, j))

    def countAntinodes(self):
        return len(self.antinodes)


class AntennasDetector:
    def __init__(self, text):
        self.antennas = {}
        lines = text.splitlines()
        for i, line in enumerate(lines):
            for j, element in enumerate(line):
                self.handleElement(element, i, j)

    def handleElement(self,element, i, j):
        if element == ".":
            return
        if element not in self.antennas.keys():
            self.antennas[element] = []
        self.antennas[element].append((i, j))

    def getAntennas(self):
        return self.antennas.values()


def findAntinodes(antennas):
    antinodes = []
    for (a, b) in getPairs(antennas):
        v = vector(a, b)
        antinodes += [remove(a, v), add(b, v)]
    return antinodes

def findResonances(antennas, I, J):
    resonances = []
    for (a, b) in getPairs(antennas):
        v = simplify(vector(a, b))
        resonances += findAligned(a, v, I, J)
    return resonances

def simplify(v):
    pgcd = computePgcd(v[0], v[1])
    return (v[0]/pgcd, v[1]/pgcd)

def computePgcd(a, b):
    if a < 0:
        return computePgcd(-a, b)
    if b < 0:
        return computePgcd(a, -b)
    if a == b:
        return a
    if a > b:
        return computePgcd(a - b, b)
    if a < b:
        return computePgcd(a, b - a)

def findAligned(point, vector, I, J):
    return [point] + findSemiDroite(point, vector, I, J, -1) + findSemiDroite(point, vector, I, J, 1)

def findSemiDroite(point, vector, I, J, increment):
    points = []
    coeff = increment
    while True:
        candidate = add(point, multiply(vector, coeff))
        if not inBounds(candidate, I, J):
            return points
        points.append(candidate)
        coeff += increment

def multiply(vector, scalar):
    return (vector[0] * scalar, vector[1] * scalar)

def inBounds(point, I, J):
    return between(point[0], 0, I) and between(point[1], 0, J)

def between(a, min, maj):
    return a >= min and a < maj

def getPairs(l):
     return [ (l[i], l[j]) for i in range(len(l)) for j in range(i + 1, len(l)) ]


def add(point, vector):
    return (point[0] + vector[0], point[1] + vector[1])

def remove(point, vector):
    return (point[0] - vector[0], point[1] - vector[1])

def vector(a, b):
    return remove(b, a)

class Tester:
    def testNoAntenna(self):
        assertSimilars([], findAntinodes([]))

    def testTwoAntennas(self):
        assertSimilars([(0, 0), (0, 3)], findAntinodes([(0, 1), (0, 2)]))
        assertSimilars([(1, 3), (7, 6)], findAntinodes([(3, 4), (5, 5)]))

    def testThreeAntennas(self):
        assertSimilars([(1, 3), (2, 0), (6, 2), (7, 6), (3, 11), (5, 12)], findAntinodes([(3, 4), (5, 5), (4, 8)]))


class ExampleTester:
    def __init__(self):
        self.textInput = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

    def testFoundAntennas(self):
        assertEquals(14, countAntinodes(self.textInput))

    def testFoundResonnances(self):
        assertEquals(34, countResonances(self.textInput))

class PartTwoTester:
    def testPgcd(self):
        assertEquals(3, computePgcd(21, 15))

    def testTwoAntennas(self):
        assertSimilars([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)], findResonances([(0, 0), (4, 4)], 5, 6))


runTests(Tester())
runTests(ExampleTester())
runTests(PartTwoTester())
main()
