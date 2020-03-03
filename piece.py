# Piece

class Piece:
    def __init__(self, type, loc):
        self.loc = loc
        self.type = type

    def __repr__(self):
        return f'[{self.type}, {self.loc}]'
