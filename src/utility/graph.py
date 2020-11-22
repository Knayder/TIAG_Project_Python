import pydot
from .production import Production

from .rng_engine import get_unique_name

class Graph:
    def __init__(self, graph: pydot.Graph):
        self.graph = graph
    
    def find_node_of_label(self, label):
        for node in self.graph.get_node_list():
            if node.get_label() == label:
                return node
        return None
    
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
        node_to_replace: pydot.Node = self.find_node_of_label(production.get_left())
        if node_to_replace == None:
            return False
        
        try:
            names_to_reconnect = self.remove_node_of_name(node_to_replace.get_name())
        except:
            print('Wrong left production\'s side')

        new_subgraph_dict = {}

        for node in production.get_right().get_node_list():
            node_label = node.get_name()
            node_name = get_unique_name()

            self.graph.add_node( pydot.Node(
                name = node_name,
                label = node_label
            ))

            new_subgraph_dict[node_label] = node_name

        for edge in production.get_right().get_edge_list():
            source_label = edge.get_source()
            source_name = get_unique_name() if source_label not in new_subgraph_dict else new_subgraph_dict[source_label]

            destination_label = edge.get_destination()
            destination_name = get_unique_name() if destination_label not in new_subgraph_dict else new_subgraph_dict[destination_label]

            self.graph.add_node( pydot.Node(
                name=source_name,
                label=source_label
            ) )
            self.graph.add_node( pydot.Node(
                name=destination_name,
                label=destination_label
            ) )
            self.graph.add_edge( pydot.Edge(source_name, destination_name) )

            new_subgraph_dict[source_label] = source_name
            new_subgraph_dict[destination_label] = destination_name
            
        transformation = production.get_transformation()

        for name_to_reconnect in names_to_reconnect:
            label_to_reconnect = self.graph.get_node(name_to_reconnect)[0].get_label()
            try:
                self.graph.add_edge(pydot.Edge(
                    name_to_reconnect,
                    new_subgraph_dict[transformation[label_to_reconnect]]
                ))
            except:
                print('Wrong transformation settings')
        return True
