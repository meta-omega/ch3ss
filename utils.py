import pydot
from math import copysign
from copy import deepcopy

# Utils

sign = lambda x: int(copysign(1, x)) if x != 0 else 0
copy = deepcopy

class Graph(pydot.Dot):
    def __init__(self):
        super().__init__('rt', graph_type='digraph')

        self.set_node_defaults(
            color = '#ff9f43',
            style = 'filled',
            shape = 'box',
            fontname = 'monospace',
            fontsize = '12'
        )

    def add_edge(self, start, end = 'Caca'):
        # print(
        #     '\n\nwlaalslad\n\n',
        #     self,
        #     '\n\nw\n\n',
        #     start,
        #     '\n\nw\n\n',
        #     end
        # )
        super().add_edge(pydot.Edge(start, end))
