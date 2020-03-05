# Location

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y

    def __eq__(self, other):
        if isinstance(other, Location):
            return tuple(self) == tuple(other)

        return False

    def __hash__(self):
        return hash(tuple(self))

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def dist_x(self, loc):
        return abs(loc.x - self.x)

    def dist_y(self, loc):
        return abs(loc.y - self.y)

    def dist(self, loc):
        return self.dist_x(loc) + self.dist_y(loc)
