import pydot
from .production import Production

from .rng_engine import get_unique_name

class Graph:
    def __init__(self, graph: pydot.Graph):
        self.graph = graph

        self.nodes_by_labels = {}
        for node in self.graph.get_node_list():
            if node not in self.nodes_by_labels.keys(): self.nodes_by_labels[node.get_label()] = [node]
            else: self.nodes_by_labels[node.get_label()] += [node]
        
        self.nodes_to_edges = {node.get_name(): [] for node in self.graph.get_node_list()}
        for edge in self.graph.get_edge_list():
            for node in self.graph.get_node_list():
                if edge.get_source() == node.get_name() or edge.get_destination() == node.get_name():
                    self.nodes_to_edges[node.get_name()] += [edge]
    
    def find_node_of_label(self, label):
        if label in self.nodes_by_labels.keys(): return self.nodes_by_labels[label][0]
        return None
    
    def add_edge(self, edge: pydot.Edge):
        self.nodes_to_edges[edge.get_source()] += [edge]
        self.nodes_to_edges[edge.get_destination()] += [edge]
        self.graph.add_edge(edge)
    
    def delete_edge(self, edge: pydot.Edge):
        self.nodes_to_edges[edge.get_source()].remove(edge)
        self.nodes_to_edges[edge.get_destination()].remove(edge)
        self.graph.del_edge(edge.get_source(), edge.get_destination())

    def add_node(self, node: pydot.Node):
        self.nodes_to_edges[node.get_name()] = []
        if node.get_label() not in self.nodes_by_labels.keys(): self.nodes_by_labels[node.get_label()] = [node]
        self.nodes_by_labels[node.get_label()] += [node]
        self.graph.add_node(node)

    def remove_node_of_name(self, node):
        names_to_reconnect = []
        for edge in self.nodes_to_edges[node.get_name()]:
            source = edge.get_source()
            destination = edge.get_destination()
            if destination == node.get_name():
                self.nodes_to_edges[edge.get_source()].remove(edge)
                names_to_reconnect.append(source)

            elif source == node.get_name():
                self.nodes_to_edges[edge.get_destination()].remove(edge)
                names_to_reconnect.append(destination)
            
            else:
                continue

            self.graph.del_edge(edge.get_source(), edge.get_destination())
        del self.nodes_to_edges[node.get_name()]
        try:
            while True: self.nodes_by_labels[node.get_label()].remove(node)
        except ValueError:
            None
        if len(self.nodes_by_labels[node.get_label()]) == 0: del self.nodes_by_labels[node.get_label()]
        self.graph.del_node(node.get_name())
        return names_to_reconnect
    
    def can_execute_production(self, production: Production):
        if self.find_node_of_label(production.get_left()) == None: return False
        return True

    def apply_production(self, production: Production):
        node_to_replace: pydot.Node = self.find_node_of_label(production.get_left())
        if node_to_replace == None:
            return False
        
        names_to_reconnect = self.remove_node_of_name(node_to_replace)

        name_links = {}


        transformation = production.get_transformation()

        labels_dic = {}

        for node in production.get_right().get_node_list():
            node_label = node.get_label()
            node_name = get_unique_name()
            name_links[node.get_name()] = node_name

            if node_label not in labels_dic:
                labels_dic[node_label] = [node_name]
            else:
                labels_dic[node_label] += [node_name]
            
            self.add_node( pydot.Node(
                name = node_name,
                label = node_label
            ))


        for edge in production.get_right().get_edge_list():
            #---  
            source_name = name_links[edge.get_source()]

            #--
            destination_name = name_links[edge.get_destination()]

            self.add_edge( pydot.Edge(source_name, destination_name) )

            
            
            
        

        for name_to_reconnect in names_to_reconnect:
            label_to_reconnect = self.graph.get_node(name_to_reconnect)[0].get_label()

            try:
                target_label = production.get_transformation()[label_to_reconnect]
            except:
                print('Wrong transformation settings')
            
            if label_to_reconnect in labels_dic:
                for name in labels_dic[label_to_reconnect]:
                    self.add_edge(pydot.Edge(name_to_reconnect, name))
        return True
