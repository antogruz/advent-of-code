#!/usr/bin/env python3

from unittests import *
from input import *

def main():
    lists = parseLists()
    partA(lists)
    partB(lists)

def partA(lists):
    lists = [sorted(l) for l in lists]
    distances = [ distance(a, b) for (a, b) in zip(lists[0], lists[1]) ]
    print(sum(distances))

def partB(lists):
    score = 0
    for element in lists[0]:
        score += computeScore(element, lists[1])
    print(score)

def computeScore(e, l):
    return l.count(e) * int(e)

def parseLists():
    entries = readLines("inputs/input.txt")
    return [ [ int(line.split()[i]) for line in entries ] for i in range(2) ]

def distance(a, b):
    if a > b:
        return a - b
    return b - a

main()
