#!/usr/bin/env python3

def getValidators():
    v = {}
    v["byr"] = DateValidator(1920, 2002)
    v["iyr"] = DateValidator(2010, 2020)
    v["eyr"] = DateValidator(2020, 2030)
    v["hgt"] = Height()
    v["hcl"] = Hair()
    v["ecl"] = Eye()
    v["pid"] = Pid()
    return v


def tests():
    testDates()
    testHeight()
    testHairColor()
    testEye()
    testPid()

def testPid():
    p = Pid()
    assert not p.isValid("")
    assert p.isValid("123456789")
    assert not p.isValid("invalid00")

class Pid():
    def isValid(self, s):
        if len(s) != 9:
            return False
        for c in s:
            if not digit(c):
                return False
        return True

def digit(c):
    return c in "0123456789"

def testEye():
    e = Eye()
    assert not e.isValid("")
    assert e.isValid("amb")
    assert not e.isValid("tot")

class Eye():
    def isValid(self, s):
        return s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def testHairColor():
    h = Hair()
    assert not h.isValid("")
    assert h.isValid("#123acf")
    assert not h.isValid("1234567")
    assert not h.isValid("##aaaaa")
    assert not h.isValid("#gggggg")

class Hair:
    def isValid(self, s):
        if len(s) != 7:
            return False
        if s[0] != "#":
            return False
        color = s[1:6]
        for c in color:
            if not hexa(c):
                return False

        return True

def hexa(c):
    return c in "0123456789abcdef"

def testHeight():
    h = Height()
    assert not h.isValid("")
    assert h.isValid("60in")
    assert not h.isValid("1999")
    assert h.isValid("190cm")
    assert not h.isValid("in60")
    assert not h.isValid("140cm")
    assert not h.isValid("140in")


class Height():
    def isValid(self, s):
        value, unit = parseHeight(s)
        if unit == "in":
            return inRange(value, 59, 76)
        if unit == "cm":
            return inRange(value, 150, 193)
        return False

import re
def parseHeight(s):
    if not s or letter(s[0]):
        return invalid()
    n = int(re.sub("[a-z]", "", s))
    unit = re.sub("[0-9]", "", s)
    return n, unit


def letter(c):
    return c in "abcdefghijklmnopqrstuvwxyz"

def invalid():
    return 0, "invalid"

def testDates():
    byr = DateValidator(1920, 2002)
    assert not byr.isValid("")
    assert byr.isValid("2002")
    assert not byr.isValid(2003)
    assert not byr.isValid("300")


class DateValidator:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def isValid(self, date):
        return date and inRange(int(date), self.min, self.max)

def inRange(value, min, max):
    return value >= min and value <= max

tests()

