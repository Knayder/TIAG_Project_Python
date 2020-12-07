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
        self.status = ProgramStatus.CURRENT
        self.current_index = None

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
        self.choose_production.clear()
        self.random_production.clear()

    def update_program_status(self, latest_production_index):
        if self.current_index == latest_production_index:
            self.status = ProgramStatus.CURRENT
        else:
            self.status = ProgramStatus.HISTORY

    def print_current_state(self):
        self.clear_old_output()
        self.current_index = self.production_engine.current_index()
        graph_path = self.production_engine.current()[0]
        list_of_productions = self.production_engine.production_list()
        production_index = self.production_engine.current_index()
        statistics = self.production_engine.get_statistics()
        available_productions = self.production_engine.get_list_of_productions()

        self.update_program_status(self.production_engine.legacy_length())
        self.main_graph.print_graph(graph_path)
        self.productions_history.print_history(list_of_productions, production_index)
        self.statistics_output.print_statistics(statistics)
        self.choose_production.print_list_of_productions(available_productions)
        self.choose_production.update_buttons()
        self.loading_steps.update_buttons()
