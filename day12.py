#!/usr/bin/env python3

from unittests import *
from input import *

def getPrice(lines):
    total = 0
    for parcel in getParcels(lines):
        area = len(parcel)
        perimeter = getPerimeter(parcel)
        total += area * perimeter
    return total

def getPerimeter(parcel):
    perimeter = 0
    for point in parcel:
        for n in neighbors(point):
            if n not in parcel:
                perimeter += 1
    return perimeter

def neighbors(p):
    (a, b) = p
    return [(a, b - 1), (a, b + 1), (a - 1, b), (a + 1, b)]

def getParcels(lines):
    parcels = {}
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            letter = lines[i][j]
            if letter not in parcels.keys():
                parcels[letter] = []
            if not appendToExistingParcel(parcels[letter], (i, j)):
                parcels[letter].append([(i, j)])

    for letter in parcels.keys():
        tryToMergeParcels(parcels[letter])

    return concat(parcels.values())

def tryToMergeParcels(parcelsList):
    while True:
        if not mergeTwoParcels(parcelsList):
            return


def mergeTwoParcels(parcelsList):
    for i, parcel in enumerate(parcelsList):
        for j, other in enumerate(parcelsList[i:]):
            if i == j:
                continue
            if contiguous(parcel, other):
                parcelsList[i] += other
                del parcelsList[j]
                return True
    return False

def contiguous(a, b):
    for x in a:
        for y in b:
            if distance(x, y) == 1:
                return True
    return False

def concat(listOfLists):
    result = []
    for l in listOfLists:
        result += l
    return result

def appendToExistingParcel(sameKindParcels, point):
    for parcel in sameKindParcels:
        if isNearby(parcel, point):
            parcel.append(point)
            return True
    return False

def isNearby(parcel, newPoint):
    for point in parcel:
        if distance(point, newPoint) == 1:
            return True
    return False

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

class Tester:
    def __init__(self):
        self.input = ["AAAA", "BBCD", "BBCC", "EEEC"]

    def testParcels(self):
        assertContains([(0, 0), (0, 1), (0, 2), (0, 3)], getParcels(self.input))
        assertSimilars([[(0, 0)], [(0, 1)], [(0,2)]], getParcels(["AXA"]))

    def testPrice(self):
        assertEquals(140, getPrice(self.input))

    def testExample(self):
        input = [ "RRRRIICCFF", "RRRRIICCCF", "VVRRRCCFFF", "VVRCCCJFFF", "VVVVCJJCFE", "VVIVCCJJEE", "VVIIICJJEE", "MIIIIIJJEE", "MIIISIJEEE", "MMMISSJEEE"]
        assertEquals(1930, getPrice(input))

runTests(Tester())
