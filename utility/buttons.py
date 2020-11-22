import  tkinter as tk
from PIL import Image, ImageTk
from statistics import StatisticsKeys #Statystyki Krzyśka - potrzebne do zmiany enuma na odp. stringa? linia 27

class Buttons:
    def __init__(self, gui):
        self.gui = gui
        self.next_state_button = tk.Button(self.gui.loading_steps_frame, text='Next', bg='grey', command=self.button_next)
        self.previous_state_button = tk.Button(self.gui.loading_steps_frame, text='Previous', bg='grey', state=tk.DISABLED)

    #additional functions
    def clear_old_output(self):
        self.gui.productions_history.delete(0.0, 'end')
        self.gui.statistics_output.delete(0.0, 'end')
        self.gui.main_graph_label.grid_forget()

    def print_history(self, list_of_productions, production_index):
        # list_of_productions must be changed into list containing only names of productions
        for i in range(len(list_of_productions)):
            if i == production_index:
                self.gui.productions_history.insert('end', list_of_productions[i][1] + "\n", "current_state")
            else:
                self.gui.productions_history.insert('end', list_of_productions[i][1] + "\n", "basic_state")

    def print_statistics(self, statistics):
        for statistic in statistics:
            self.gui.statistics_output.insert('end', statistic.value + ": ", "statistic_name")
            self.gui.statistics_output.insert('end', str(statistics[statistic]) + "\n", "statistic_value")

    # button utils
    def button_previous(self):

        graph_path = self.gui.production_engine.previous()  # string representing path to current graph image
        list_of_productions = self.gui.production_engine.productions_list()  #list of tuples (png_path, prod_name)
        production_index = self.gui.production_engine.current_index()  # current production index
        statistics = self.production_engine.get_statistics()  # current graph statistics in dictionary

        # clear old output
        self.clear_old_output()

        if self.gui.production_index < 0:
            self.previous_state_button = tk.Button(self.gui.loading_steps_frame, text="Previous", bg='grey', state=tk.DISABLED)
            self.previous_state_button.place(relx=0.1, rely=0.85, relwidth=0.5 - 3 / 2 * 0.1, relheight=0.5, anchor='sw')

        #load current graph image
        self.gui.main_graph_label = tk.Label(self.gui.main_graph_frame, image=ImageTk.PhotoImage(Image.open(graph_path)) ,bg='white', justify='center')

        #print productions and statistics
        self.print_history(list_of_productions, production_index)
        self.print_statistics(statistics)

        self.gui.main_graph_label.place(rely=0.1, relwidth=1, relheight=0.9)

    def button_next(self):

        graph_path = self.gui.production_engine.next() #string representing path to current graph image
        list_of_productions = self.gui.production_engine.productions_list() #list of tuples (png_path, prod_name)
        production_index = self.gui.production_engine.current_index() #current production index
        statistics = self.production_engine.get_statistics() #current graph statistics in dictionary

        #clear old output
        self.clear_old_output()

        #allow previous button to be clicked
        self.previous_state_button = tk.Button(self.gui.loading_steps_frame, text="Previous", bg='grey', command=self.button_previous)

        #load current graph image
        self.gui.main_graph_label = tk.Label(self.gui.main_graph_frame, image=ImageTk.PhotoImage(Image.open(graph_path)), bg='white', justify='center')

        #print productions and statistics
        self.print_history(list_of_productions, production_index)
        self.print_statistics(statistics)

        self.previous_state_button.place(relx=0.1, rely=0.85, relwidth=0.5 - 3 / 2 * 0.1, relheight=0.5, anchor='sw')
        self.gui.main_graph_label.place(rely=0.1, relwidth=1, relheight=0.9)