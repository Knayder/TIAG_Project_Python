from productions_manager import *
from utility.graph import Graph
import pydot

class ProductionEngine:
    def __init__(self):
        self.productions_manager = ProductionsManager(['data/production.json'])

    def run(self):
        print('Hello World')
        production = self.productions_manager.get_production(0)

        pydot_graph = pydot.Dot('test', graph_type="graph")
        pydot_graph.add_node(pydot.Node(name='n1', label='A'))
        pydot_graph.add_node(pydot.Node(name='n2', label='B'))
        pydot_graph.add_node(pydot.Node(name='n3', label='X'))
        pydot_graph.add_edge(pydot.Edge('n1', 'n2'))
        pydot_graph.add_edge(pydot.Edge('n1', 'n3'))
        pydot_graph.add_edge(pydot.Edge('n2', 'n3'))


        graph = Graph(pydot_graph)

        graph.apply_production(production)
        pydot_graph.write_png('test.png')


        