from move   import Move
from utils  import sign, copy, Graph

# Board

class Board:
    def __init__(self):
        self.pieces = []
        self.leaves = []
        self.parent = None
        self.children = []

    # Recortar.
    def __repr__(self, for_console = False):
        s = ''

        x = max(self.pieces, key = lambda p: p.loc.x).loc.x
        y = max(self.pieces, key = lambda p: p.loc.y).loc.y

        board = [['-' for j in range(x)] for i in range(y)]

        for p in self.pieces:
            board[p.loc.y - 1][p.loc.x - 1] = p.type

        for i in range(y):
            for j in range(x):
                s += board[i][j]
                s += '\t' if for_console else ''

            s += '\n\n\n' if for_console else '\n'

        return s[:-1]

    # Creo que mejorable usando rectas.
    def is_freeway(self, start, end):
        locations = []
        loc = copy(start)

        def advance():
            loc.x += sign(end.x - loc.x)
            loc.y += sign(end.y - loc.y)

        advance()

        while loc.x != end.x or loc.y != end.y:
            locations.append(copy(loc))
            advance()

        pieces = set([tuple(p.loc) for p in self.pieces])
        locations = set([tuple(l) for l in locations])

        return pieces.isdisjoint(locations)

    def make_move(self, move):
        piece = copy(move.piece)

        f = lambda p: not p.loc in [piece.loc, move.loc]
        self.pieces = list(filter(f, self.pieces))

        piece.loc = copy(move.loc)
        self.pieces.append(piece)

    def get_tree(self):
        self.children = []

        for piece in self.pieces:
            for prey in self.pieces:
                loc = prey.loc
                move = Move(piece, loc)

                if move.is_valid(ctx = self):
                    new_board = copy(self)
                    new_board.make_move(move)
                    self.children.append(new_board)

        for child in self.children:
            child.get_tree()

    # No es un árbol, cambiale el nombre.
    def graph_tree(self):
        graph = Graph()
        graphed = set()

        def aux(board):
            for child in board.children:
                if not f'{str(board)}, {str(child)}' in graphed:
                    graph.add_edge(str(board), str(child))
                    graphed.add(f'{str(board)}, {str(child)}')

                aux(child)

        aux(self)
        graph.write_png('tree.png')

    def get_leaves(self):
        self.leaves = []

        def aux(board):
            if not len(board.children):
                self.leaves.append(board)
            else:
                for child in board.children:
                    aux(child)

        aux(self)

    # Tenés que hacerla usando get_leaves.
    def get_solutions(self):
        return []
