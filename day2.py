#!/usr/bin/env python3

def tests():
    assert PasswordDownTheStreet("0-1 a: ").isValid()
    assert not PasswordDownTheStreet("0-0 a: a").isValid()

    assert Toboggan("1-2 a: ab").isValid()
    assert not Toboggan("1-2 a: bb").isValid()
    assert not Toboggan("1-2 a: bba").isValid()
    assert not Toboggan("1-2 a: aa").isValid()
    assert Toboggan("1-2 a: a").isValid()


def main():
    passwords = readFile("inputs/day2.txt")
    downTheStreet = [PasswordDownTheStreet(p) for p in passwords]

    print(countValids(downTheStreet))

    toboggans = [Toboggan(p) for p in passwords]
    print(countValids(toboggans))


def countValids(passwords):
    count = 0
    for p in passwords:
        if p.isValid():
            count += 1
    return count


class PasswordDownTheStreet():
    def __init__(self, s):
        self.min, self.max, self.letter, self.pwd = parsePassword(s)

    def isValid(self):
        n = count(self.letter, self.pwd)
        return n >= self.min and n <= self.max

    def toString(self):
        return str(self.min) + " " + str(self.max) + " " + self.letter + " " + self.pwd


class Toboggan():
    def __init__(self, s):
        a, b, self.letter, self.pwd = parsePassword(s)
        self.positions = [a, b]

    def isValid(self):
        count = 0
        for p in self.positions:
            if len(self.pwd) > p:
                if self.pwd[p] == self.letter:
                    count += 1

        return count == 1

def parsePassword(s):
    firstPart, pwd = s.split(":")
    range, letter = firstPart.split(" ")
    i, j = [int(s) for s in range.split("-")]
    return i, j, letter, pwd


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
