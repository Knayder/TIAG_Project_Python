import tkinter as tk

class ProductionsHistory:
    def __init__(self, gui):
        self.gui = gui

        self.log_label = tk.Label(self.gui.action_log_frame, text="Action log", bg='yellow', justify="center", font=("Calibri Light", 12))

        # scrollbar
        self.productions_scrollbar = tk.Scrollbar(self.gui.action_log_frame)

        #action log
        self.productions_history = tk.Text(self.gui.action_log_frame, bg = '#d9ddff', font = ("Times New Roman", 15), yscrollcommand = self.productions_scrollbar.set)

        #config scrollbar
        self.productions_scrollbar.config(command=self.productions_history.yview)

        #define tags
        self.productions_history.tag_add("current_state", "1.0", "1.0")
        self.productions_history.tag_config("current_state", foreground='green', font=("Times New Roman", 20), justify='center')
        self.productions_history.tag_add("basic_state", "1.0", "1.0")
        self.productions_history.tag_config("basic_state", font=("Times New Roman", 15), justify='center')

        #place scrollbar
        self.log_label.place(relwidth=1, relheight=0.2)
        self.productions_scrollbar.place(relx=0.9, rely=0.2, relwidth=0.1, relheight=0.8)
