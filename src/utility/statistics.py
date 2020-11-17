import graph.py
import pydot

class Statistics:
    def __init__(self, py_graph: Graph):
        self.graph: pydot.Graph = py_graph.graph

    def no_nodes(self):
        return len(self.graph.get_node_list())

    def no_edges(self):
        return len(self.graph.get_edge_list())

    def subgraphs(self):
        return self.graph.get_subgraph_list()

    def no_subgraphs(self):
        return len(self.subgraphs())

    def averge_vertex_degree(self): 
        return self.no_edges * 2 / self.no_nodes
    
    def averge_vertex_degree_abcd(self):
        count = 0
        for edge in self.graph.graph.get_edge_list():
            if edge.get_source().get_label() in 'abcd': count += 1
            if edge.get_destination().get_label() in 'abcd': count += 1
        return count/self.no_nodes()
    




