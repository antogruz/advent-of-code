#!/usr/bin/env python3

def tests():
    assert PasswordDownTheStreet("0-1 a: ").isValid()
    assert not PasswordDownTheStreet("0-0 a: a").isValid()

def main():
    passwords = readFile("inputs/day2.txt")
    validCount = 0
    for p in passwords:
        if PasswordDownTheStreet(p).isValid():
            validCount += 1

    print(validCount)


class PasswordDownTheStreet():
    def __init__(self, s):
        range, letter, self.pwd = s.split(" ")
        self.min, self.max = [int(s) for s in range.split("-")]
        self.letter = letter.split(":")[0]

    def isValid(self):
        n = count(self.letter, self.pwd)
        return n >= self.min and n <= self.max

    def toString(self):
        return str(self.min) + " " + str(self.max) + " " + self.letter + " " + self.pwd

def count(char, string):
    count = 0
    for c in string:
        if c == char:
            count += 1

    return count


def readFile(f):
    with open(f, 'r') as fh:
        return fh.readlines()



tests()
main()
