#!/usr/bin/env python3

from unittests import assert_equals
from input import readFileByGroups

def tests():
    assert_equals(0, countYesInGroup([]))
    assert_equals(1, countYesInGroup(["d"]))
    assert_equals(2, countYesInGroup(["ad"]))
    assert_equals(2, countYesInGroup(["a", "ab"]))
    assert_equals(3, countYesInGroup(["a", "bc"]))

    assert_equals(0, countAllYesInGroup([""]))
    assert_equals(1, countAllYesInGroup(["a"]))
    assert_equals(1, countAllYesInGroup(["a", "a"]))
    assert_equals(2, countAllYesInGroup(["ab", "ab", "abc"]))
    assert_equals(0, countAllYesInGroup(["a", "ab", "c"]))


def main():
    groups = readFileByGroups("inputs/day6.txt")

    print(countAnswers(groups, countYesInGroup))
    print(countAnswers(groups, countAllYesInGroup))

def countAnswers(groups, counter):
    count = 0
    for g in groups:
        count += counter(g)
    return count

def countYesInGroup(members):
    if not members:
        return 0

    answers = []
    for m in members:
        for answer in m:
            if not answer in answers:
                answers.append(answer)

    return len(answers)

def countAllYesInGroup(members):
    count = 0
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if allSaidYes(members, letter):
            count += 1

    return count

def allSaidYes(members, letter):
    for m in members:
        if not letter in m:
            return False
    return True



tests()
main()

