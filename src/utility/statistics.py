from .graph import *
import pydot
import enum

class StatisticsKeys(enum.Enum):
    no_nodes = 'number of nodes'
    no_edges = 'number of edges'
    no_subgraphs = 'number of subgraphs'
    averge_vertex_degree = 'averge vertex degree'
    averge_vertex_degree_a = 'averge vertex a degree'
    averge_vertex_degree_b = 'averge vertex b degree'
    averge_vertex_degree_c = 'averge vertex c degree'
    averge_vertex_degree_d = 'averge vertex d degree'
    subgraphs_avarge_degree = 'averge number of nodes in subgraphs'
    



class Statistics:
    def __init__(self, py_graph):
        self.graph = py_graph

    def get_list_of_node(self):
        return self.graph.get_node_list()

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
        return round(self.number_of_edges() * 2 / self.number_of_nodes(),2)
    
    def averge_vertex_degree_abcd(self):
        if self.number_of_abcd_nodes() == 0: return 0 
        counter = {str(x): 0 for x in 'abcd'}
        for edge in self.graph.get_edge_list():
            source_label = self.find_node_by_name(edge.get_source()).get_label()
            destination_label = self.find_node_by_name(edge.get_destination()).get_label()
            if str(source_label) in 'abcd': counter[source_label] += 1
            if str(destination_label) in 'abcd': counter[destination_label] += 1
        return {str(i): round(counter[i]/self.number_of_abcd_nodes(),2) for i in counter.keys}
    
    def subgraphs_avarge_degree(self):
        return round(self.number_of_nodes() / self.number_of_subgraphs(),2)

    def get_statistic(self):
        return {
            StatisticsKeys.no_nodes: self.number_of_nodes(),
            StatisticsKeys.no_edges: self.number_of_edges(),
            StatisticsKeys.no_subgraphs: self.number_of_subgraphs(),
            StatisticsKeys.averge_vertex_degree: self.averge_vertex_degree(),
            StatisticsKeys.averge_vertex_degree_a: self.averge_vertex_degree_abcd()['a'],
            StatisticsKeys.averge_vertex_degree_b: self.averge_vertex_degree_abcd()['b'],
            StatisticsKeys.averge_vertex_degree_c: self.averge_vertex_degree_abcd()['c'],
            StatisticsKeys.averge_vertex_degree_d: self.averge_vertex_degree_abcd()['d'],
            StatisticsKeys.subgraphs_avarge_degree: self.subgraphs_avarge_degree(),
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




