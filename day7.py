#!/usr/bin/env python3

from unittests import assert_equals
from input import readLines

def tests():
    assert_equals(0, howManyColors({}))

    d = {"light red": ["shiny gold"]}
    assert_equals(1, howManyColors(d))

    d = {"light red": ["shiny blue"]}
    assert_equals(0, howManyColors(d))

    d = {"light red": ["shiny gold"], "shiny blue": ["shiny gold"]}
    assert_equals(2, howManyColors(d))


    d = {"light red": ["shiny blue"], "shiny blue": ["shiny gold"]}
    assert_equals(2, howManyColors(d))

    d = {"light red": ["shiny blue"], "shiny blue": ["green gold"], "green gold": ["shiny gold"]}
    assert_equals(3, howManyColors(d))

    key, values = parseRule("light red bags contain 1 bright white bag, 2 muted yellow bags.")
    assert_equals("light red", key)
    assert_equals(["bright white", "muted yellow"], values)

def main():
    input = readLines("inputs/day7.txt")
    rules = parse(input)
    print(howManyColors(rules))

def parse(input):
    rules = {}
    for line in input:
        bag, treasures = parseRule(line)
        rules[bag] = treasures
    return rules

def parseRule(line):
    key, contentWords = line.split(" bags contain ")
    quantities = contentWords.split(', ')
    treasures = [ getBagColor(content) for content in quantities ]

    return key, treasures

def getBagColor(content):
    words = content.split(" ")
    return words[1] + " " + words[2]

def howManyColors(rules):
    containers = findBagsContaining(rules, ["shiny gold"])
    nextStepContainers = containers
    while not len(nextStepContainers) == 0:
        nextStepContainers = findBagsContaining(rules, nextStepContainers)
        containers = containers.union(nextStepContainers)

    return len(containers)

def findBagsContaining(rules, treasures):
    bags = set()
    for bag, items in rules.items():
        for t in treasures:
            if t in items:
                bags.add(bag)
    return bags






tests()
main()
