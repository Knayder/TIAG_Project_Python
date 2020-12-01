import tkinter as tk
from .constants import *

class StatisticsOutput:
    def __init__(self, gui):
        self.gui = gui
        self.statistics_frame = tk.Frame(self.gui.root, bg='orange')
        self.statistics_output = tk.Text(self.statistics_frame, bg = '#d9ddff')
        self.statistics_label = tk.Label(self.statistics_frame, text="Graph statistics", bg='yellow', justify="center", font=("Calibri Light", 12))

        #define tags
        self.statistics_output.tag_add("statistic_name", '1.0', '1.0')
        self.statistics_output.tag_config("statistic_name", foreground='blue', font=("Calibri Light", 12))
        self.statistics_output.tag_add("statistic_value", '1.0', '1.0')
        self.statistics_output.tag_config("statistic_value", font=("Calibri Light", 12))

    def print_statistics(self, statistics):
        for statistic in statistics:
            self.statistics_output.insert('end', statistic.value + ": ", "statistic_name")
            self.statistics_output.insert('end', str(statistics[statistic]) + "\n", "statistic_value")

    def clear(self):
        self.statistics_output.delete(0.0, 'end')

    def place(self):
        
        self.statistics_frame.place(relx=1 - MAIN_GRAPH_OFFSET, rely=LOADING_STEPS_HEIGHT + CHOOSE_PRODUCTION_HEIGHT + CHOOSE_RANDOM_HEIGHT + ACTION_LOG_HEIGHT + 5 * MAIN_GRAPH_OFFSET, relwidth=STATISTICS_WIDTH, relheight=STATISTICS_HEIGHT, anchor='ne')
        self.statistics_label.place(relwidth=1, relheight=0.2)
        self.statistics_output.place(rely = 0.2, relheight=0.8, relwidth=1)