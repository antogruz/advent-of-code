#!/usr/bin/env python3

from unittests import *
from input import *

def main():
    text = readFile("inputs/day9.txt").strip()
    print(checksum(rebalance(expand(text))))

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


def toList(s):
    return [ e for e in s ]

runTests(Tester())
main()
