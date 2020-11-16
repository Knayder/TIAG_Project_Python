import pydot
from .production import Production

class Graph:
    def __init__(self, graph: pydot.Graph):
        self.graph = graph
    
    def apply_production(self, production: Production):
        node: pydot.Node = None
        for i_node in self.graph.get_node_list():
            if i_node.get_label() == production.get_left():
                node = i_node
                break

        if node == None:
            return
        
        
        to_reconnect = []

        for edge in self.graph.get_edge_list():
            source = edge.get_source()
            destination = edge.get_destination()
            name = node.get_name()
            if destination == name:
                to_reconnect.append(source)

            elif source == name:
                to_reconnect.append(destination)
            
            else:
                continue

            self.graph.del_edge(source, destination)
        
        self.graph.del_node(node.get_name())


        for node_i in production.get_right().get_node_list():
            self.graph.add_node(node_i) # Automagicly change name to label and add random unique name
        for edge_i in production.get_right().get_edge_list():
            self.graph.add_edge(edge_i) # Same as above
        
        transformation = production.get_transformation()
        for i in to_reconnect:
            temp = transformation[self.graph.get_node(i)[0].get_label()]
            for node_i in production.get_right().get_node_list():
                if node_i.get_label() == temp:
                    self.graph.add_edge(pydot.Edge( i, node_i.get_name() ))

            
