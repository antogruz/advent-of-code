#!/usr/bin/env python3

from unittests import *
from input import *

import sys
def main():
    sys.set_int_max_str_digits(100000)
    stones = "112 1110 163902 0 7656027 83039 9 74".split()
    stones = [ int(s) for s in stones ]
    print(stones)
    print(countStonesAfterBlinks(stones, 40))
#    print(countStonesAfterBlinks(stones, 75))


def countStonesAfterBlinks(stones, stepsLeft):
    if stepsLeft == 0:
        return len(stones)
    d = getCountOfEachOccurence(stones)
    result = 0
    for stone, count in d.items():
        result += count * countStonesAfterBlinks(blink([stone]), stepsLeft - 1)
    return result

def getCountOfEachOccurence(l):
    d = {}
    for element in list(set(l)):
        d[element] = l.count(element)
    return d


def countAfterBlink(stone, count):
    stones = [stone]
    for i in range(count):
        stones = blink(stones)
        limit = 1000
        if len(stones) > limit:
            return countStonesAfterBlinks(stones[0:int(limit/2)], count - i - 1) + countStonesAfterBlinks(stones[int(limit/2):], count -i - 1)
    return len(stones)


def blink(stones):
    result = []
    for s in stones:
        result += evolve(s)
    return result

def evolve(stone):
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        return splitInTwo(str(stone))
    return [stone * 2024]

def splitInTwo(string):
    half = int(len(string) / 2)
    return [int(string[0:half]), int(string[half:])]



class Tester:
    def testOneBlink(self):
        assertEquals([1, 2024, 1, 0, 9, 9, 2021976], blink([0, 1, 10, 99, 999]))

    def testExample(self):
        stones = [125, 17]
        assertEquals(22, countStonesAfterBlinks(stones, 6))
        assertEquals(55312, countStonesAfterBlinks(stones, 25))



runTests(Tester())
main()
