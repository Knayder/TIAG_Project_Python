from productions_manager import *
from utility.graph import Graph
import pydot

class ProductionEngine:
    def __init__(self):
        self.productions_manager = ProductionsManager(['data/transformation_p.json'])

    def run(self):
        production = self.productions_manager.get_production(0)
        pydot_graph = pydot.Dot('test', graph_type="graph")
        pydot_graph.add_node(pydot.Node(name='j1', label='X'))
        #pydot_graph.add_node(pydot.Node(name='j1', label='A'))
        #pydot_graph.add_node(pydot.Node(name='j2', label='B'))
        #pydot_graph.add_node(pydot.Node(name='j3', label='X'))
        #pydot_graph.add_edge(pydot.Edge('j1', 'j2'))
        #pydot_graph.add_edge(pydot.Edge('j1', 'j3'))
        #pydot_graph.add_edge(pydot.Edge('j2', 'j3'))


        graph = Graph(pydot_graph)

        graph.apply_production(production)
        pydot_graph.write_png('test.png')


        