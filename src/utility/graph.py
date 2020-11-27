import pydot
from .production import Production

from .rng_engine import get_unique_name

class Graph:
    def __init__(self, graph: pydot.Graph):
        self.graph = graph
    
    def find_nodes_of_label(self, label):
        nodes = []
        for node in self.graph.get_node_list():
            if node.get_label() == label:
                nodes.append(node)
        return nodes
    
    def remove_node_of_name(self, name):
        names_to_reconnect = []
        for edge in self.graph.get_edge_list():
            source = edge.get_source()
            destination = edge.get_destination()
            if destination == name:
                names_to_reconnect.append(source)

            elif source == name:
                names_to_reconnect.append(destination)
            
            else:
                continue

            self.graph.del_edge(source, destination)
        self.graph.del_node(name)
        return names_to_reconnect
    
        

    def apply_production(self, production: Production):
        nodes_to_replace: [] = self.find_nodes_of_label(production.get_left())
        if len(nodes_to_replace) == 0:
            return False
        
        node_to_replace: pydot.Node = nodes_to_replace[0]
        try:
            names_to_reconnect = self.remove_node_of_name(node_to_replace.get_name())
        except:
            print('Wrong left production\'s side')

        name_links = {}

        for node in production.get_right().get_node_list():
            node_label = node.get_label()
            node_name = get_unique_name()
            name_links[node.get_name()] = node_name

            self.graph.add_node( pydot.Node(
                name = node_name,
                label = node_label
            ))


        for edge in production.get_right().get_edge_list():
            #---
            source_label = production.get_right().get_node(edge.get_source())[0].get_label()  
            source_name = name_links[edge.get_source()]

            #--
            destination_label = production.get_right().get_node(edge.get_destination())[0].get_label()
            destination_name = name_links[edge.get_destination()]

            self.graph.add_edge( pydot.Edge(source_name, destination_name) )

            
            
            
        transformation = production.get_transformation()

        for name_to_reconnect in names_to_reconnect:
            label_to_reconnect = self.graph.get_node(name_to_reconnect)[0].get_label()
            try:
                target_label = production.get_transformation()[label_to_reconnect]
            except:
                print('Wrong transformation settings')
            for node in filter( lambda x: x.get_name() in name_links, self.find_nodes_of_label(target_label)):
                self.graph.add_edge(name_to_reconnect, node.get_name())

        return True
