#!/usr/bin/env python3

from unittests import *
from input import *

def main():
    groups = readFileByGroups("inputs/day5.txt")
    rules = [parseRule(r) for r in groups[0]]
    reports = [parseReport(r) for r in groups[1]]
    print(computeResult(rules, reports))

def computeResult(rules, reports):
    result = 0
    for report in reports:
        if isReportValid(rules, report):
            result += int(middleElement(report))
    return result

def middleElement(l):
    return l[int(len(l) / 2)]

def parseRule(r):
    elements = r.split("|")
    return (elements[0], elements[1])

def parseReport(r):
    return r.split(",")

def isReportValid(rules, report):
    for rule in rules:
        if not check(rule, report):
            return False
    return True

def check(rule, report):
    relevantReport = [ element for element in report if element in rule]
    if len(relevantReport) < 2:
        return True

    for i in range(2):
        if rule[i] != relevantReport[i]:
            return False
    return True

class Tester:
    def testEmptyReport(self):
        assertEquals(True, isReportValid([], []))

    def testWrongReport(self):
        assertEquals(False, isReportValid([(1, 2)], [2, 1]))

    def testReportWithoutRule(self):
        assertEquals(True, isReportValid([], [2, 1]))

    def testValidReport(self):
        assertEquals(True, isReportValid([(1, 2)], [1, 2]))
        assertEquals(True, isReportValid([(1, 2)], [1, 3]))



class ExampleTester:
    def __init__(self):
        self.rules = []
        self.rules.append((47, 53))
        self.rules.append((97, 13))
        self.rules.append((97, 61))
        self.rules.append((97, 47))
        self.rules.append((75, 29))
        self.rules.append((61, 13))
        self.rules.append((75, 53))
        self.rules.append((29, 13))
        self.rules.append((97, 29))
        self.rules.append((53, 29))
        self.rules.append((61, 53))
        self.rules.append((97, 53))
        self.rules.append((61, 29))
        self.rules.append((47, 13))
        self.rules.append((75, 47))
        self.rules.append((97, 75))
        self.rules.append((47, 61))
        self.rules.append((75, 61))
        self.rules.append((47, 29))
        self.rules.append((75, 13))
        self.rules.append((53, 13))

        self.reports = []
        self.reports.append([75,47,61,53,29])
        self.reports.append([97,61,53,29,13])
        self.reports.append([75,29,13])
        self.reports.append([75,97,47,61,53])
        self.reports.append([61,13,29])
        self.reports.append([97,13,75,29,47])

    def testReports(self):
        assertEquals(True, isReportValid(self.rules, [75,47,61,53,29]))
        assertEquals(True, isReportValid(self.rules, [97,61,53,29,13]))
        assertEquals(True, isReportValid(self.rules, [75,29,13]))
        assertEquals(False, isReportValid(self.rules, [75,97,47,61,53]))
        assertEquals(False, isReportValid(self.rules, [61,13,29]))
        assertEquals(False, isReportValid(self.rules, [97,13,75,29,47]))

    def testResult(self):
        assertEquals(143, computeResult(self.rules, self.reports))





runTests(Tester())
runTests(ExampleTester())
main()
