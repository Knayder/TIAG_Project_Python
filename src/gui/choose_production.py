import tkinter as tk
from .constants import *

class ChooseProduction:
    def __init__(self, gui):
        self.gui = gui
        self.choose_production_frame = tk.Frame(self.gui.root, bg='white')
        self.choose_production_label = tk.Label(self.choose_production_frame, text = 'Choose production', bg = 'yellow')
        self.do_button = tk.Button(self.choose_production_frame, text = 'Apply Production', bg = 'grey')
        self.choose_production_scrollbar = tk.Scrollbar(self.choose_production_frame)
        self.choose_production_listbox = tk.Listbox(self.choose_production_frame, bg = 'white', yscrollcommand = self.choose_production_scrollbar.set)
        self.choose_production_scrollbar.config(command=self.choose_production_listbox.yview)

    def place(self):

        self.choose_production_frame.place(relx = 1- MAIN_GRAPH_OFFSET, rely = LOADING_STEPS_HEIGHT + 2* MAIN_GRAPH_OFFSET, relwidth = CHOOSE_PRODUCTION_WIDTH, relheight = CHOOSE_PRODUCTION_HEIGHT, anchor = 'ne')
        self.choose_production_label.place(relwidth = 1, relheight = 0.2)
        self.choose_production_scrollbar.place(relx=0.9, rely=0.2, relwidth=0.1, relheight=0.6)
        self.choose_production_listbox.place(rely=0.2, relwidth=0.9, relheight=0.6)
        self.do_button.place(rely = 0.8, relx = 0.5, relwidth = 1, relheight = 0.2, anchor = 'n')