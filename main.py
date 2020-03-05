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
l2 = Location(3, 1)
l3 = Location(4, 1)
l4 = Location(3, 2)
l5 = Location(1, 3)
l6 = Location(4, 3)
l7 = Location(2, 4)
l8 = Location(3, 4)

p1 = Piece('A', l1)
p2 = Piece('T', l2)
p3 = Piece('C', l3)
p4 = Piece('P', l4)
p5 = Piece('C', l5)
p6 = Piece('T', l6)
p7 = Piece('A', l7)
p8 = Piece('P', l8)

b.pieces = [p1, p2, p3, p4, p5, p6, p7, p8]

print(b)
b.get_tree()
b.graph_tree()

'''
b.get_leaves()

for index, leaf in enumerate(b.leaves):
    print(f'\n{index}')
    print(leaf)
'''
