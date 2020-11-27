import tkinter as tk

class ChooseProduction:
    def __init__(self, gui):
        self.gui = gui

        #title
        self.choose_production_label = tk.Label(self.gui.choose_production_frame, text = 'Choose production', bg = 'yellow')

        #do button
        self.do_button = tk.Button(self.gui.choose_production_frame, text = 'Apply Production', bg = 'grey')

        # scrollbar
        self.choose_production_scrollbar = tk.Scrollbar(self.gui.choose_production_frame)

        #listbox
        self.choose_production_listbox = tk.Listbox(self.gui.choose_production_frame, bg = 'white', yscrollcommand = self.choose_production_scrollbar.set)

        #config scrollbar
        self.choose_production_scrollbar.config(command=self.choose_production_listbox.yview)

    def place(self):
        #place label
        self.choose_production_label.place(relwidth = 1, relheight = 0.2)

        #place scrollbar
        self.choose_production_scrollbar.place(relx=0.9, rely=0.2, relwidth=0.1, relheight=0.6)

        #place listbox
        self.choose_production_listbox.place(rely=0.2, relwidth=0.9, relheight=0.6)

        #place button
        self.do_button.place(rely = 0.8, relx = 0.5, relwidth = 1, relheight = 0.2, anchor = 'n')