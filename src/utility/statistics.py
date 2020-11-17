import graph
import pydot
import enum.Enum

#class StatisticsKeys(enum.Enum):
    



class Statistics:
    def __init__(self, py_graph: graph.Graph):
        self.graph: pydot.Graph = py_graph.graph

    def number_of_nodes(self):
        return len(self.graph.get_node_list())

    def number_of_edges(self):
        return len(self.graph.get_edge_list())

    def subgraphs(self):
        return self.graph.get_subgraph_list()

    def number_of_subgraphs(self):
        return len(self.subgraphs())

    def averge_vertex_degree(self): 
        return self.number_of_edges * 2 / self.number_of_nodes
    
    def averge_vertex_degree_abcd(self):
        count = 0
        for edge in self.graph.graph.get_edge_list():
            if edge.get_source().get_label() in 'abcd': count += 1
            if edge.get_destination().get_label() in 'abcd': count += 1
        return count/self.number_of_nodes()
    
    def subgraphs_avarge_degree(self):
        return self.number_of_subgraphs() / self.number_of_nodes()

    def get_statistic(self):
        return {
            'number of nodes': self.number_of_nodes(),
            'number of edges': self.number_of_edges(),
            'number of subgraphs': self.number_of_subgraphs(),
            'averge vertex degree': self.averge_vertex_degree(),
            'averge vertex abcd degree': self.averge_vertex_degree_abcd(),
            'averge number of nodes in subgraphs': self.subgraphs_avarge_degree(),
        }

    def __repr__(self):
        return """
    number of nodes: {no_nodes}
    number of edges: {no_edges}
    number of subgraphs: {no_subgraphs}
    averge vertex degree: {averge}
    averge vertex like: (a, b, c, d) degree: {averge_abcd}
    averge number of nodes in subgraphs: {averge_in_subgraphs}
        """.format(
            no_nodes = self.number_of_nodes(),
            no_edges = self.number_of_edges(), 
            no_subgraphs = self.number_of_subgraphs(), 
            averge = self.averge_vertex_degree(), 
            averge_abcd = self.averge_vertex_degree_abcd(),
            averge_in_subgraphs = self.subgraphs_avarge_degree()
            )




