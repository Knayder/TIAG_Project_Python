import  tkinter as tk
from PIL import Image, ImageTk
from utility.statistics import StatisticsKeys

class Buttons:
    def __init__(self, gui):
        self.gui = gui
        self.next_state_button = tk.Button(self.gui.loading_steps_frame, text='Next', bg='grey', command=self.button_next)
        self.previous_state_button = tk.Button(self.gui.loading_steps_frame, text='Previous', bg='grey', state=tk.DISABLED)
        self.loading_steps_label = tk.Label(self.gui.loading_steps_frame, text="Load step", bg='yellow', justify="center", font=("Calibri Light", 12))
        self.loading_steps_label.place(relwidth=1, relheight=0.4)

    # button utils
    def button_previous(self):

        self.gui.production_engine.previous()

        if self.gui.production_engine.current_index() <= 0:
            self.previous_state_button = tk.Button(self.gui.loading_steps_frame, text="Previous", bg='grey', state=tk.DISABLED)
            self.previous_state_button.place(rely=0.4, relwidth=0.5, relheight=0.6)

        self.gui.print_current()

        self.gui.main_graph_label.place(rely=0.1, relwidth=1, relheight=0.9)

    def button_next(self):

        self.gui.production_engine.next()

        #allow previous button to be clicked
        self.previous_state_button = tk.Button(self.gui.loading_steps_frame, text="Previous", bg='grey', command=self.button_previous)

        self.gui.print_current()

        self.previous_state_button.place(rely=0.4, relwidth=0.5, relheight=0.6)
        self.gui.main_graph_label.place(rely=0.1, relwidth=1, relheight=0.9)