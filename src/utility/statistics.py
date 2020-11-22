from .graph import *
import pydot
import enum

class StatisticsKeys(enum.Enum):
    no_nodes = 'number of nodes'
    no_edges = 'number of edges'
    no_subgraphs = 'number of subgraphs'
    averge_vertex_degree = 'averge vertex degree'
    averge_vertex_degree_abcd = 'averge vertex abcd degree'
    subgraphs_avarge_degree = 'averge number of nodes in subgraphs'
    



class Statistics:
    def __init__(self, py_graph):
        self.graph = py_graph

    def get_list_of_node(self):
        name_sets = []
        node_sets = []
        for vertex in self.graph.get_node_list():
            if vertex.get_name() not in name_sets: 
                name_sets.append(vertex.get_name())
                node_sets.append(vertex)
        return node_sets

    def find_node_by_name(self, name): 
        return list(filter(lambda x: x.get_name() == name, self.get_list_of_node()))[0]

    def number_of_nodes(self):
        return len(self.get_list_of_node())
    
    def number_of_abcd_nodes(self):
        return len(list(filter( lambda x: str(x.get_label()) in 'abcd', self.get_list_of_node())))

    def number_of_edges(self):
        return len(self.graph.get_edge_list())

    def subgraphs(self):
        node_sets = [{i.get_name()} for i in self.get_list_of_node()]
        def marge_set(node1, node2):
            set1 = list(filter(lambda x: node1 in node_sets[x], range(len(node_sets))))[0]
            set2 = list(filter(lambda x: node2 in node_sets[x], range(len(node_sets))))[0] 
            if set1 == set2: return
            node_sets[set1] = node_sets[set1].union(node_sets[set2])
            del node_sets[set2]

        for edge in self.graph.get_edge_list():
            marge_set(edge.get_source(), edge.get_destination())
        return node_sets


    def number_of_subgraphs(self):
        return len(self.subgraphs())

    def averge_vertex_degree(self): 
        return self.number_of_edges() * 2 / self.number_of_nodes()
    
    def averge_vertex_degree_abcd(self):
        if self.number_of_abcd_nodes() == 0: return 0 
        count = 0
        for edge in self.graph.get_edge_list():
            if str(self.find_node_by_name(edge.get_source()).get_label()) in 'abcd': count += 1
            if str(self.find_node_by_name(edge.get_destination()).get_label()) in 'abcd': count += 1
        return count/self.number_of_abcd_nodes()
    
    def subgraphs_avarge_degree(self):
        return self.number_of_nodes() / self.number_of_subgraphs() 

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



