#!/usr/bin/env python3

from unittests import *
from input import *

def main():
    text = readFile("inputs/day9.txt").strip()
    print(checksum(rebalance(expand(text))))
    print(checksum(newRebalance(expand(text))))


def checksum(l):
    result = 0
    for i, element in enumerate(l):
        if element != ".":
            result += i * int(element)
    return result

def rebalance(ram):
    while not balanced(ram):
        balanceStep(ram)
    return ram

def newRebalance(ram):
    start = findHighestNumber(ram)
    for i in range(int(start), 0, -1):
        ram = shiftValue(ram, str(i))
    return ram

def findHighestNumber(l):
    n = 0
    for e in l:
        if e == ".":
            continue
        if int(e) > int(n):
            n = e
    return n

def shiftValue(l, value):
    indices = findIndices(l, value)
    newSpot = findEmptySpot(l, len(indices))
    if newSpot == -1 or newSpot > indices[0]:
        return l
    for increment, index in enumerate(indices):
        l = permute(l, newSpot + increment, index)
    return l

def findIndices(l, value):
    return [ i for i, x in enumerate(l) if x == value ]

def findEmptySpot(l, size):
    for i, element in enumerate(l):
        if nextElementsAreEmpty(l, i, size):
            return i
    return -1

def nextElementsAreEmpty(l, index, size):
    for i in range(size):
        if index + i >= len(l) or l[index + i] != ".":
            return False
    return True


def balanced(ram):
    firstPointIndex = ram.index(".")
    for i in range(firstPointIndex, len(ram)):
        if ram[i] != ".":
            return False
    return True

def balanceStep(ram):
    firstPointIndex = ram.index(".")
    lastNumber = findLastId(ram)
    return permute(ram, firstPointIndex, lastNumber)

def findLastId(l):
    for i in range(len(l) - 1, 0, -1):
        if l[i] != ".":
            return i

def permute(l, i, j):
    buffer = l[i]
    l[i] = l[j]
    l[j] = buffer
    return l

def expand(s):
    disk = True
    id = 0
    result = []
    for element in s:
        if disk:
            appendMultipleTimes(result, str(id), int(element))
            id += 1
        else:
            appendMultipleTimes(result, ".", int(element))
        disk = not disk
    return result

def appendMultipleTimes(l, element, count):
    for i in range(count):
        l.append(element)

class Tester:
    def testExpander(self):
        assertEquals(toList("0..111....22222"), expand("12345"))

    def testRebalancer(self):
        assertEquals(toList("022111222......"), toList(rebalance(expand("12345"))))

    def testNewRebalancer(self):
        assertEquals(toList("00992111777.44.333....5555.6666.....8888.."), toList(newRebalance(expand("2333133121414131402"))))



def toList(s):
    return [ e for e in s ]

runTests(Tester())
main()
