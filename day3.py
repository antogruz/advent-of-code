#!/usr/bin/env python3

from unittests import *
from input import *

def main():
    text = readFile("inputs/day3.txt")
    operations = findValidMults(text)


main()
