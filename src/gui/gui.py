from .constants import *
from .buttons import *
from .statistics_output import *
from .productions_history import *
from .random_production import *
from .choose_production import *
from PIL import Image, ImageTk

class Gui:
    def __init__(self, root, production_engine):
        self.root = root
        self.production_engine = production_engine

        #background and title
        self.root.title("Graph transformations")
        self.canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
        self.canvas.pack()

        #graph image - I don't know why, but is myst be defined as an attribute of class, because otherwise
        #doesn't render on a screen :(
        self.graph_image = None

        #frames
        self.main_graph_frame = tk.Frame(root, bg='green')
        self.loading_steps_frame = tk.Frame(root, bg='#d9ddff')
        self.action_log_frame = tk.Frame(root, bg='purple')
        self.statistics_frame = tk.Frame(root, bg='orange')
        self.choose_production_frame = tk.Frame(root, bg='white')
        self.random_production_frame = tk.Frame(root, bg = 'pink')

        #buttons
        self.buttons = Buttons(self)

        #labels
        self.main_graph_title = tk.Label(self.main_graph_frame, text="Current graph", bg='yellow', justify='center', font=("Calibri Light", 12))
        self.main_graph_label = tk.Label(self.main_graph_frame, bg='white', justify='center')

        #statistics
        self.statistics_output = StatisticsOutput(self).statistics_output

        #action log
        self.productions_history = ProductionsHistory(self).productions_history

        #choose_production
        self.choose_production = ChooseProduction(self)

        #random_production
        self.random_production = RandomProduction(self)

        #load base graph
        self.print_current()

        #place widgets
        self.place_everything()

    def place_everything(self):
        self.place_frames()
        self.place_buttons()
        self.place_labels()
        self.place_statistics_output()
        self.place_productions_history()
        self.place_listbox()

    def place_frames(self):
        self.main_graph_frame.place(relx=MAIN_GRAPH_OFFSET, rely=MAIN_GRAPH_OFFSET, relwidth=MAIN_GRAPH_WIDTH, relheight=MAIN_GRAPH_HEIGHT)
        self.loading_steps_frame.place(relx=1 - MAIN_GRAPH_OFFSET, rely=MAIN_GRAPH_OFFSET, relwidth=LOADING_STEPS_WIDTH, relheight=LOADING_STEPS_HEIGHT, anchor='ne')
        self.choose_production_frame.place(relx = 1- MAIN_GRAPH_OFFSET, rely = LOADING_STEPS_HEIGHT + 2* MAIN_GRAPH_OFFSET, relwidth = CHOOSE_PRODUCTION_WIDTH, relheight = CHOOSE_PRODUCTION_HEIGHT, anchor = 'ne')
        self.random_production_frame.place(relx = 1- MAIN_GRAPH_OFFSET, rely = LOADING_STEPS_HEIGHT + CHOOSE_PRODUCTION_HEIGHT + 3 * MAIN_GRAPH_OFFSET, relwidth = CHOOSE_RANDOM_WIDTH, relheight = CHOOSE_RANDOM_HEIGHT, anchor = 'ne')
        self.action_log_frame.place(relx=1 - MAIN_GRAPH_OFFSET, rely=LOADING_STEPS_HEIGHT + CHOOSE_PRODUCTION_HEIGHT + CHOOSE_RANDOM_HEIGHT + 4 * MAIN_GRAPH_OFFSET, relwidth=ACTION_LOG_WIDTH, relheight=ACTION_LOG_HEIGHT, anchor='ne')
        self.statistics_frame.place(relx=1 - MAIN_GRAPH_OFFSET, rely=LOADING_STEPS_HEIGHT + CHOOSE_PRODUCTION_HEIGHT + CHOOSE_RANDOM_HEIGHT + ACTION_LOG_HEIGHT + 5 * MAIN_GRAPH_OFFSET, relwidth=STATISTICS_WIDTH, relheight=STATISTICS_HEIGHT, anchor='ne')

    def place_buttons(self):
        self.buttons.next_state_button.place(relx = 0.5, rely=0.4, relwidth=0.5, relheight=0.6)
        self.buttons.previous_state_button.place(rely=0.4, relwidth=0.5, relheight=0.6)
        self.random_production.place()

    def place_labels(self):
        self.main_graph_title.place(relwidth=1, relheight=0.1)
        self.main_graph_label.place(rely=0.1, relwidth=1, relheight=0.9)

    def place_listbox(self):
        self.choose_production.place()

    def place_statistics_output(self):
        self.statistics_output.place(rely = 0.2, relheight=0.8, relwidth=1)

    def place_productions_history(self):
        self.productions_history.place(rely = 0.2, relheight=0.8, relwidth=0.9)

    def resize_image(self, image):
        if image.width > int(WIDTH*MAIN_GRAPH_WIDTH):
            image = image.resize((int(WIDTH*MAIN_GRAPH_WIDTH), image.height))
        if image.height > int(HEIGHT*MAIN_GRAPH_HEIGHT*0.9):
            image = image.resize((image.width, int(HEIGHT*MAIN_GRAPH_HEIGHT*0.9)))
        return image

    def clear_old_output(self):
        self.productions_history.delete(0.0, 'end')
        self.statistics_output.delete(0.0, 'end')
        self.main_graph_label.grid_forget()

    def print_history(self, list_of_productions, production_index):
        # list_of_productions must be changed into list containing only names of productions
        for i in range(len(list_of_productions)-1, -1, -1):
            if i == production_index:
                self.productions_history.insert('end', str(i) + "   " + list_of_productions[i][1] + "\n", "current_state")
            else:
                self.productions_history.insert('end', str(i) + "            " + list_of_productions[i][1] + "\n", "basic_state")

    def print_statistics(self, statistics):
        for statistic in statistics:
            self.statistics_output.insert('end', statistic.value + ": ", "statistic_name")
            self.statistics_output.insert('end', str(statistics[statistic]) + "\n", "statistic_value")

    def print_current(self):
        graph_path = self.production_engine.current()[0]
        self.graph_image = ImageTk.PhotoImage(self.resize_image(Image.open(graph_path)))
        list_of_productions = self.production_engine.production_list()
        production_index = self.production_engine.current_index()
        statistics = self.production_engine.get_statistics()

        self.clear_old_output()
        self.print_history(list_of_productions, production_index)
        self.print_statistics(statistics)

        # load current graph image
        self.main_graph_label = tk.Label(self.main_graph_frame,image=self.graph_image, bg='white',justify='center')