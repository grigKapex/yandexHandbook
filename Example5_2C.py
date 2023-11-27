import math


class Point:

    def __init__(self, pointx, pointy):
        self.x = pointx
        self.y = pointy

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def move(self, movex=0, movey=0):
        self.x = self.x + movex
        self.y = self.y + movey

    def length(self, two):
        lenx = self.x - two.x
        leny = self.y - two.y
        return round(math.sqrt(lenx ** 2 + leny ** 2), 2)


class PatchedPoint(Point):

    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(pointx=0, pointy=0)
        elif len(args) == 1:
            ax, ay = args[0]
            self.x = ax
            self.y = ay
        else:
            x2 = args[0]
            y2 = args[1]
            super().__init__(pointx=x2, pointy=y2)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'PatchedPoint({self.x}, {self.y})'

    def __add__(self, other):
        new_addpoint = PatchedPoint(self.x + other[0], self.y + other[1])
        return new_addpoint

    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self