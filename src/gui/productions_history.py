import tkinter as tk
from .constants import *

class ProductionsHistory:
    def __init__(self, gui):

        self.gui = gui
        self.action_log_frame = tk.Frame(self.gui.root, bg='purple')
        self.productions_history_title = tk.Label(self.action_log_frame, text="Action log", bg=TITLE_COLOR, justify="center", font=TITLE_FONT)
        self.productions_scrollbar = tk.Scrollbar(self.action_log_frame)
        self.productions_history = tk.Text(self.action_log_frame, bg = '#d9ddff', font = ("Calibri Light", 15), yscrollcommand = self.productions_scrollbar.set)
        self.productions_scrollbar.config(command=self.productions_history.yview)

        #define tags
        self.productions_history.tag_config("current_state", foreground='green', font=("Calibri Light", 20), justify='center')
        self.productions_history.tag_config("basic_state", font=("Times New Roman", 15), justify='center')
    
    def print_history(self, list_of_productions, production_index):
        # list_of_productions must be changed into list containing only names of productions
        for i in range(len(list_of_productions)-1, -1, -1):
            if i == production_index:
                self.productions_history.insert('end', str(i)+". " + list_of_productions[i][1] + "\n", "current_state")
            else:
                self.productions_history.insert('end', str(i)+". " + list_of_productions[i][1] + "\n", "basic_state")

    def clear(self):
        self.productions_history.delete(0.0, 'end')

    def place(self):

        self.action_log_frame.place(relx=1 - MAIN_GRAPH_OFFSET, rely=LOADING_STEPS_HEIGHT + CHOOSE_PRODUCTION_HEIGHT + CHOOSE_RANDOM_HEIGHT + 4 * MAIN_GRAPH_OFFSET, relwidth=ACTION_LOG_WIDTH, relheight=ACTION_LOG_HEIGHT, anchor='ne')
        self.productions_history_title.place(relwidth=1, relheight=0.2)
        self.productions_scrollbar.place(relx=0.9, rely=0.2, relwidth=0.1, relheight=0.8)
        self.productions_history.place(rely = 0.2, relheight=0.8, relwidth=0.9)

