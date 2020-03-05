from move       import Move
from piece      import Piece
from board      import Board
from location   import Location

# C3 Chess Solver

'''

A   Alfil
T   Torre
C   Caballo
P   Peón
D   Dama
R   Rey

'''

b = Board()

l1 = Location(1, 1)
l2 = Location(3, 3)
l3 = Location(4, 4)
l4 = Location(1, 2)

p1 = Piece('A', l1)
p2 = Piece('P', l2)
p3 = Piece('R', l3)
p4 = Piece('C', l4)

b.pieces = [p1, p2, p3, p4]

print(b)
b.get_tree()
b.graph_tree()

b.get_leaves()

for index, leaf in enumerate(b.leaves):
    print(f'\n{index}')
    print(leaf)
