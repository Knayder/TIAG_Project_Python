import  tkinter as tk
from PIL import Image, ImageTk
from .constants import *
from utility.statistics import StatisticsKeys

class LoadStep:
    def __init__(self, gui):

        self.gui = gui
        self.loading_steps_frame = tk.Frame(self.gui.root, bg='#d9ddff')
        self.next_state_button = tk.Button(self.loading_steps_frame, text='Next', bg='grey', command=self.button_next)
        self.previous_state_button = tk.Button(self.loading_steps_frame, text='Previous', bg='grey', state=tk.DISABLED)
        self.loading_steps_label = tk.Label(self.loading_steps_frame, text="Load step", bg='yellow', justify="center", font=("Calibri Light", 12))

    # button utils
    def button_previous(self):

        self.gui.production_engine.previous()

        if self.gui.production_engine.current_index() <= 0:
            self.previous_state_button = tk.Button(self.loading_steps_frame, text="Previous", bg='grey', state=tk.DISABLED)

        self.gui.print_current_state()
        self.place()

    def button_next(self):

        self.gui.production_engine.next()

        #allow previous button to be clicked
        self.previous_state_button = tk.Button(self.loading_steps_frame, text="Previous", bg='grey', command=self.button_previous)

        self.gui.print_current_state()
        self.place()

    def place(self):

        self.loading_steps_frame.place(relx=1 - MAIN_GRAPH_OFFSET, rely=MAIN_GRAPH_OFFSET, relwidth=LOADING_STEPS_WIDTH, relheight=LOADING_STEPS_HEIGHT, anchor='ne')
        self.loading_steps_label.place(relwidth=1, relheight=0.4)
        self.next_state_button.place(relx = 0.5, rely=0.4, relwidth=0.5, relheight=0.6)
        self.previous_state_button.place(rely=0.4, relwidth=0.5, relheight=0.6)