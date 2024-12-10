#!/usr/bin/env python3

from unittests import *
from input import *

def main():
    lines = readLines("inputs/day4.txt")
    print(countXmas(lines))

def countXmas(lines):
    if len(lines) < 3:
        return 0
    I = len(lines[0])
    J = len(lines)
    count = 0
    for i in range(I - 2):
        for j in range(J - 2):
            count += isXmas(sub33(lines, i, j))
    return count

def sub33(lines, iOffset, jOffset):
    subMatrix = []
    for j in range(3):
        line = []
        for i in range(3):
            line.append(lines[j + jOffset][i + iOffset])
        subMatrix.append(line)
    return subMatrix


def isXmas(lines):
    if not lines[1][1] == "A":
        return 0
    for letter in "MS":
        if edges(lines).count(letter) != 2:
            return 0
    if not "".join(mainDiag(lines)) in ["MAS", "SAM"]:
        return 0

    return 1

def mainDiag(lines):
    return [ lines[i][i] for i in range(3) ]

def edges(lines):
    return [ lines[i][j] for (i, j) in [(0, 0), (2, 2), (0, 2), (2, 0)] ]

class Tester:
    def testEmptyInput(self):
        assertEquals(0, countXmas([]))

    def testSimpleXmas(self):
        assertEquals(1, countXmas(["M.M", ".A.", "S.S"]))

    def testNoCentralA(self):
        assertEquals(0, countXmas(["M..", "...", "..S"]))

    def testNoXmas(self):
        assertEquals(0, countXmas(["...", ".A.", "..."]))

    def testMEdges(self):
        assertEquals(0, countXmas(["MMM", ".A.", "MMM"]))

    def testBadDiagonal(self):
        assertEquals(0, countXmas(["M.S", ".A.", "S.M"]))

    def testSmallGrid(self):
        assertEquals(0, countXmas(["M.", ".A"]))

    def testBigGrid(self):
        assertEquals(1, countXmas(["....", ".M.M", "..A.", ".S.S"]))

    def testExampleGrid(self):
        assertEquals(9, countXmas([".M.S......", "..A..MSMS.", ".M.S.MAA..", "..A.ASMSM.", ".M.S.M....", "..........", "S.S.S.S.S.", ".A.A.A.A..", "M.M.M.M.M.", ".........."]))


runTests(Tester())
main()
