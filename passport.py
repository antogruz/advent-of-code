#!/usr/bin/env python3

def tests():
    assert not SimplePassport("").isValid()
    assert SimplePassport("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm").isValid()
    assert not SimplePassport("ecl:gry").isValid()
    assert SimplePassport("ecl:gry\npid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm").isValid()
    assert SimplePassport("ecl:gry\npid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 hgt:183cm").isValid()
    assert not SimplePassport("ecl:gry\npid:860033327 eyr:2020 hcl:#fffffd cid:1937 iyr:2017 hgt:183cm").isValid()

    assert ComplexPassport("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\nhcl:#623a2f").isValid()
    assert not ComplexPassport("eyr:1972 cid:100\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926").isValid()

class SimplePassport:
    def __init__(self, s):
        self.fields = parse(s)

    def isValid(self):
        for f in ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]:
            if not f in self.fields.keys():
                return False
        return True

from validators import getValidators
class ComplexPassport:
    def __init__(self, s):
        self.fields = parse(s)
        self.validators = getValidators()

    def isValid(self):
        for key, validator in self.validators.items():
            if not key in self.fields:
                return False
            if not validator.isValid(self.fields[key]):
                return False
        return True

def parse(s):
    fields = getFields(s)

    return {getKey(f): getValue(f) for f in fields}

import re
def getFields(s):
    return re.split(" |\n", s)

def getKey(field):
    return field.split(":")[0]

def getValue(field):
    try:
        return field.split(":")[1]
    except:
        return ""




tests()
