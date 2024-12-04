#!/usr/bin/env python3

def tests():
    map = Map(["#"])
    assert map.tree()
    assert not map.end()

    map = Map(["."])
    assert not map.tree()

    map = Map([".#"])
    map.move(1, 0)
    assert map.tree()

    map = Map([".#"])
    map.move(2, 0)
    assert not map.tree()

    map = Map([".","#"])
    map.move(13, 1)
    assert map.tree()

    map = Map(["."])
    map.move(0, 1)
    assert not map.tree()
    assert map.end()


class Map():
    def __init__(self, l):
        self.l = l
        self.x = 0
        self.y = 0
        self.width = len(l[0])
        self.high = len(l)

    def tree(self):
        if self.y >= self.high:
            return False

        return self.l[self.y][self.x] == "#"

    def move(self, x, y):
        self.x = (self.x + x) % self.width
        self.y += y

    def end(self):
        return self.y >= self.high



tests()
