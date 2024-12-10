#!/usr/bin/env python3

from unittests import *
from input import *

def main():
    lines = readLines("inputs/day4.txt")
    print(countXmas(lines))

def countXmas(lines):
    return countLines(lines) + countColumns(lines) + countDiagonals(lines)

def countLines(lines):
    count = 0
    for l in lines:
        count += countHorizontal(l)
    return count

def countColumns(lines):
    columns = linesToColumns(lines)
    return countLines(columns)

def linesToColumns(lines):
    if not lines:
        return lines
    columns = []
    for i in range(len(lines[0])):
        column = "".join([ line[i] for line in lines ])
        columns.append(column)
    return columns

def countDiagonals(lines):
    diags = linesToDiags(lines)
    return countLines(diags)

def linesToDiags(lines):
    if not lines:
        return lines
    diags = []
    for i in range(len(lines[0])):
        diags.append(getDownRightDiag(lines, i, 0))
        diags.append(getDownLeftDiag(lines, i, 0))
    for j in range(len(lines)):
        diags.append(getDownRightDiag(lines, 0, j))
        diags.append(getDownLeftDiag(lines, len(lines[0]) - 1, j))
    return diags

def getDownRightDiag(lines, i, j):
    return getDiag(lines, i, 1, j, 1)

def getDownLeftDiag(lines, i, j):
    return getDiag(lines, i, -1, j, 1)

def getUpRightDiag(lines, i, j):
    return getDiag(lines, i, 1, j, -1)

def getDiag(lines, i, iDirection, j, jDirection):
    diag = []
    increment = 0
    while True:
        try:
            diag.append(lines[j + increment * jDirection][i + increment * iDirection])
            increment += 1
        except IndexError:
            return "".join(diag)


import re
def countHorizontal(line):
    return line.count("XMAS") + line.count("SAMX")


class Tester:
    def testEmptyInput(self):
        assertEquals(0, countXmas([]))

    def testOneLine(self):
        assertEquals(1, countXmas(["XMAS"]))

    def testWrongSpelling(self):
        assertEquals(0, countXmas(["MXAS"]))

    def testReverseSpelling(self):
        assertEquals(1, countXmas(["SAMX"]))

    def testLongerLine(self):
        assertEquals(2, countXmas(["AXMASAMX"]))

    def testVertical(self):
        assertEquals(1, countXmas(["X", "M", "A", "S"]))

    def testDiagonal(self):
        assertEquals(1, countXmas(["...S", "..A.", ".M..", "X..."]))

    def testOfficial(self):
        assertEquals(18, countXmas(["....XXMAS.", ".SAMXMS...", "...S..A...", "..A.A.MS.X", "XMASAMX.MM", "X.....XA.A", "S.S.S.S.SS", ".A.A.A.A.A", "..M.M.M.MM", ".X.X.XMASX"]))

runTests(Tester())
main()
