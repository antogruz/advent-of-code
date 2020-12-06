#!/usr/bin/env python3

from unittests import assert_equals
from input import readFileByGroups

def tests():
    assert_equals(0, countYesInGroup([]))
    assert_equals(1, countYesInGroup(["d"]))
    assert_equals(2, countYesInGroup(["ad"]))
    assert_equals(2, countYesInGroup(["a", "ab"]))
    assert_equals(3, countYesInGroup(["a", "bc"]))


def main():
    groups = readFileByGroups("inputs/day6.txt")

    print(countAnswers(groups))

def countAnswers(groups):
    count = 0
    for g in groups:
        members = g.split("\n")
        count += countYesInGroup(members)
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



tests()
main()

