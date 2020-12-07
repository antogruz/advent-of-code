#!/usr/bin/env python3

def readFile(f):
    with open(f, 'r') as fh:
        return fh.readlines()

def readLines(f):
    with open(f, 'r') as fh:
        return fh.read().splitlines()

def readFileByBlocks(f):
    with open(f) as fh:
        return fh.read().split("\n\n")

def readFileByGroups(f):
    with open(f) as fh:
        groups = fh.read().split("\n\n")
        return [splitMembers(g) for g in groups]

def splitMembers(group):
    members = group.split("\n")
    if "" in members:
        members.remove("")
    return members

