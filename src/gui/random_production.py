import tkinter as tk
from .constants import *

class RandomProduction:
    def __init__(self, gui):
        self.gui = gui
        self.random_production_frame = tk.Frame(self.gui.root, bg = 'pink')
        self.entry = tk.Entry(self.random_production_frame, font = INPUT_FONT)
        self.do_button = tk.Button(self.random_production_frame, text = 'DO', bg = 'grey', command = self.generate_n_random)
        self.random_production_title = tk.Label(self.random_production_frame, text = 'Generate random', bg = TITLE_COLOR, font = TITLE_FONT)

    def place(self):
        self.random_production_frame.place(relx = 1- MAIN_GRAPH_OFFSET, rely = LOADING_STEPS_HEIGHT + CHOOSE_PRODUCTION_HEIGHT + 3 * MAIN_GRAPH_OFFSET, relwidth = CHOOSE_RANDOM_WIDTH, relheight = CHOOSE_RANDOM_HEIGHT, anchor = 'ne')
        self.random_production_title.place(relwidth = 1, relheight = 0.4)
        self.entry.place(rely = 0.4, relwidth = 0.8, relheight = 0.6)
        self.do_button.place(relx = 0.8, rely = 0.4, relwidth = 0.2, relheight = 0.6)

    def clear(self):
        self.entry.delete(0,'end')

    def generate_n_random(self):
        try:
            n = int(self.entry.get())
            if n <= 0:
                raise ValueError
        except ValueError:
            print("Number of productions must be positive integer!")
        else:
            self.gui.production_engine.execute_n_productions(n)
            self.gui.print_current_state()
        
