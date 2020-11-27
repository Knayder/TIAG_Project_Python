import tkinter as tk

class RandomProduction:
    def __init__(self, gui):
        self.gui = gui
        self.entry = tk.Entry(self.gui.random_production_frame)
        self.do_button = tk.Button(self.gui.random_production_frame, text = 'DO', bg = 'grey')
        self.random_production_label = tk.Label(self.gui.random_production_frame, text = 'Generate random', bg = 'yellow')

    def place(self):
        self.random_production_label.place(relwidth = 1, relheight = 0.4)
        self.entry.place(rely = 0.4, relwidth = 0.8, relheight = 0.6)
        self.do_button.place(relx = 0.8, rely = 0.4, relwidth = 0.2, relheight = 0.6)

