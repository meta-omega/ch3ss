# Location

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def dist(self, loc):
        return abs(loc.x - self.x) + abs(loc.y - self.y)
