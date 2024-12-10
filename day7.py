#!/usr/bin/env python3

from unittests import *
from input import *

def main():
    lines = readLines("inputs/day7.txt")
    equations = []
    for line in lines:
        equations.append(lineToEquation(line))
    print(computeResult(equations))

def lineToEquation(line):
    result, operands = line.split(": ")
    strElements = operands.split(" ")
    elements = [ int(e) for e in strElements ]
    return (int(result), elements)


def computeResult(equations):
    answer = 0
    for (result, elements) in equations:
        if isPossible(result, elements):
            answer += result
    return answer

def isPossible(result, elements):
    return stillPossible(result, elements[0], elements[1:])

def stillPossible(result, currentResult, elements):
    operations = [add, multiply, concat]
    if not elements:
        return result == currentResult
    for operation in operations:
        if stillPossible(result, operation(currentResult, elements[0]), elements[1:]):
            return True
    return False

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def concat(a, b):
    return int(str(a) + str(b))

class Tester:
    def testNoOperation(self):
        assertEquals(True, isPossible(10, [10]))
        assertEquals(False, isPossible(6, [9]))

    def testOneOperation(self):
        assertEquals(True, isPossible(10, [6, 4]))
        assertEquals(True, isPossible(10, [5, 2]))


class ExampleTester:
    def __init__(self):
        self.equations = []
        self.equations.append((190, [10,19]))
        self.equations.append((3267, [81,40,27]))
        self.equations.append((83, [17,5]))
        self.equations.append((156, [15,6]))
        self.equations.append((7290, [6,8,6,15]))
        self.equations.append((161011, [16,10,13]))
        self.equations.append((192, [17,8,14]))
        self.equations.append((21037, [9,7,18,13]))
        self.equations.append((292, [11,6,16,20]))

    def testComputation(self):
        #assertEquals(3749, computeResult(self.equations))
        assertEquals(11387, computeResult(self.equations))



runTests(Tester())
runTests(ExampleTester())
main()
