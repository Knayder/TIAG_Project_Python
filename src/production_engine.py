from productions_manager import *
from utility.graph import Graph
from utility.rng_engine import get_unique_name
import pydot
import utility.statistics

def load_start_graph( start_graph):
    file_graph = pydot.graph_from_dot_file(start_graph)[0]
    start_production = Production(ParsedProduction('Start Production', 'S', file_graph, None))

    pydot_graph = pydot.Dot('Graph', graph_type="graph")
    start_node = pydot.Node(name=get_unique_name(), label='S')
    pydot_graph.add_node(start_node)

    graph = Graph(pydot_graph)
    graph.apply_production(start_production)
    return graph, pydot_graph

class ProductionEngine:
    def __init__(self, file_paths, start_graph_path):
        self.productions_manager = ProductionsManager(file_paths)
        self.graph, self.pydot_graph = load_start_graph(start_graph_path)


        self.legacy_index = 0
        self.legacy_graphs = []
        self.save_to_legacy('Start')

    def save_to_legacy(self, production_name):
        path = 'output/graph' + str(len(self.legacy_graphs)) + '.jpg'
        self.legacy_graphs.append( (path, production_name, utility.statistics.Statistics(self.pydot_graph).get_statistic()) )
        self.pydot_graph.write_jpg(path, prog=['dot','-Gsize=12,12', '-Gratio=1.0'])

    def current(self):
        return self.legacy_graphs[self.legacy_index]
    
    def current_index(self):
        return self.legacy_index

    def legacy_length(self):
        return len(self.legacy_graphs) - 1
    
    def production_list(self):
        return self.legacy_graphs

    def next(self):
        if self.legacy_index == len(self.legacy_graphs) - 1:
            indices = [x for x in range(self.productions_manager.size())]
            random.shuffle(indices)

            for index in indices:
                production = self.productions_manager.get_production(index)
                if self.graph.apply_production(production):
                    self.save_to_legacy(production.get_name())
                    self.legacy_index += 1
                    break
            
        else:
            self.legacy_index += 1
        return self.current()
    
    def previous(self):
        if self.legacy_index > 0:
            self.legacy_index -= 1
        return self.current()

    def get_statistics(self):
        return self.current()[2]
    
    def execute_n_productions(self, n):
        self.legacy_index = len(self.legacy_graphs) - 1
        for i in range(n):
            executable = self.get_list_of_productions()
            if len(executable) == 0:
                print("No productions can be done!")
                break
            self.graph.apply_production(executable[random.randint(0, len(executable) - 1)])
        self.save_to_legacy('execute ' + str(n) + ' productions')
        self.legacy_index += 1
        return self.current()
    
    def execute_production(self, production_name):
        production_to_execute = list(filter(lambda x: x.get_name() == production_name, self.productions_manager.production))[0]
        if self.graph.apply_production(production_to_execute):
            self.save_to_legacy(production_to_execute.get_name())
            self.legacy_index += 1
            return self.current()
        print("unable to execute production!")
        return False
    
    def get_list_of_productions(self):
        executable = []
        for production in self.productions_manager.production:
            if self.graph.can_execute_production(production):
                executable.append(production)
        return executable

        







        