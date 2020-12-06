from .constants import *
from .load_step import *
from .statistics_output import *
from .productions_history import *
from .random_production import *
from .choose_production import *
from .main_graph import *
from PIL import Image, ImageTk

class Gui:
    def __init__(self, root, production_engine):
        self.root = root
        self.production_engine = production_engine

        #background and title
        self.root.title("Graph transformations")
        self.canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
        self.canvas.pack()

        #windows with widgets
        self.main_graph = MainGraph(self)
        self.loading_steps = LoadStep(self)
        self.productions_history = ProductionsHistory(self)
        self.statistics_output = StatisticsOutput(self)
        self.random_production = RandomProduction(self)
        self.choose_production = ChooseProduction(self)

        #load base state
        self.print_current_state()

        #place widgets
        self.place_everything()

    def place_everything(self):
        self.main_graph.place()
        self.loading_steps.place()
        self.productions_history.place()
        self.statistics_output.place()
        self.random_production.place()
        self.choose_production.place()

    def clear_old_output(self):
        self.productions_history.clear()
        self.statistics_output.clear()
        self.main_graph.clear()

    def print_current_state(self):
        self.clear_old_output()
        graph_path = self.production_engine.current()[0]
        list_of_productions = self.production_engine.production_list()
        production_index = self.production_engine.current_index()
        statistics = self.production_engine.get_statistics()

        self.main_graph.print_graph(graph_path)
        self.productions_history.print_history(list_of_productions, production_index)
        self.statistics_output.print_statistics(statistics)
