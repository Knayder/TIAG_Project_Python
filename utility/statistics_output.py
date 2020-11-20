import tkinter as tk

class StatisticsOutput:
    def __init__(self, gui):
        self.gui = gui
        self.statistics_output = tk.Text(self.gui.statistics_frame, bg = '#d9ddff')

        #define tags
        self.statistics_output.tag_add("statistic_name", '1.0', '1.0')
        self.statistics_output.tag_config("statistic_name", foreground='blue', font=("Calibri Light", 12))
        self.statistics_output.tag_add("statistic_value", '1.0', '1.0')
        self.statistics_output.tag_config("statistic_value", font=("Calibri Light", 12))