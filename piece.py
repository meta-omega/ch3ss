# Piece

class Piece:
    def __init__(self, type, loc):
        self.loc = loc
        self.type = type

    def __iter__(self):
        yield self.type
        yield self.loc

    def __eq__(self, other):
        if isinstance(other, Piece):
            return tuple(self) == tuple(other)

        return False

    def __repr__(self):
        return f'[{self.type}, {self.loc}]'
