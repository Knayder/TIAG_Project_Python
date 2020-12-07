import tkinter as tk
from .constants import *

class ChooseProduction:
    def __init__(self, gui):
        self.gui = gui
        self.choose_production_frame = tk.Frame(self.gui.root, bg='white')
        self.choose_production_title = tk.Label(self.choose_production_frame, text = 'Choose production', bg = TITLE_COLOR, font = TITLE_FONT)
        self.do_button = tk.Button(self.choose_production_frame, text = 'Apply Production', bg = 'grey', command = self.apply_production)
        self.choose_production_scrollbar = tk.Scrollbar(self.choose_production_frame)
        self.choose_production_listbox = tk.Listbox(self.choose_production_frame, bg = 'white', yscrollcommand = self.choose_production_scrollbar.set, font = OUTPUT_FONT)
        self.choose_production_scrollbar.config(command=self.choose_production_listbox.yview)
        self.productions = None

    def place(self):
        self.choose_production_frame.place(relx = 1- MAIN_GRAPH_OFFSET, rely = LOADING_STEPS_HEIGHT + 2* MAIN_GRAPH_OFFSET, relwidth = CHOOSE_PRODUCTION_WIDTH, relheight = CHOOSE_PRODUCTION_HEIGHT, anchor = 'ne')
        self.choose_production_title.place(relwidth = 1, relheight = 0.2)
        self.choose_production_scrollbar.place(relx=0.9, rely=0.2, relwidth=0.1, relheight=0.6)
        self.choose_production_listbox.place(rely=0.2, relwidth=0.9, relheight=0.6)
        self.do_button.place(rely = 0.8, relx = 0.5, relwidth = 1, relheight = 0.2, anchor = 'n')

    def clear(self):
        self.choose_production_listbox.delete(0, 'end')

    def update_buttons(self):
        if self.gui.status == ProgramStatus.CURRENT:
            self.do_button = tk.Button(self.choose_production_frame, text = 'Apply Production', bg = 'grey', command = self.apply_production)
        else:
            self.do_button = tk.Button(self.choose_production_frame, text = 'Apply Production', bg = 'grey', state= tk.DISABLED)
        self.place()

    def print_list_of_productions(self, available_productions):
        self.productions = list(map(lambda x: x.get_name(),available_productions))
        self.display_productions()

    def display_productions(self):
        for production in self.productions:
            self.choose_production_listbox.insert('end',production)

    def apply_production(self):
        production = self.choose_production_listbox.get(tk.ANCHOR)
        if production in self.productions:
            self.gui.production_engine.execute_production(production)
            self.gui.print_current_state()
