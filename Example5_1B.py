import math


class Point:

    def __init__(self, pointx=0, pointy=0):
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


first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
