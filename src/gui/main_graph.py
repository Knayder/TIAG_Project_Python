import tkinter as tk
from .constants import *
from PIL import Image, ImageTk

class MainGraph:
    def __init__(self, gui):

        self.gui = gui
        self.main_graph_frame = tk.Frame(gui.root, bg='green')
        self.graph_image = None
        self.graph_image_tk = None
        self.main_graph_title = tk.Label(self.main_graph_frame, text="Current graph", bg='yellow', justify='center', font=("Calibri Light", 12))
        self.main_graph_label = tk.Label(self.main_graph_frame, bg='white', justify='center')

    def place(self):

        self.main_graph_frame.place(relx=MAIN_GRAPH_OFFSET, rely=MAIN_GRAPH_OFFSET, relwidth=MAIN_GRAPH_WIDTH, relheight=MAIN_GRAPH_HEIGHT)
        self.main_graph_title.place(relwidth=1, relheight=0.1)
        self.main_graph_label.place(rely=0.1, relwidth=1, relheight=0.9)

    def print_graph(self, graph_path):
        self.graph_image = Image.open(graph_path)
        self.graph_image_tk = ImageTk.PhotoImage(self.resize_image(self.graph_image))
        self.main_graph_label = tk.Label(self.main_graph_frame,image=self.graph_image_tk, bg='white',justify='center')
        self.place()

    def clear(self):
        self.main_graph_label.grid_forget()
        if self.graph_image != None:
            self.graph_image.close()

    def resize_image(self, image):
        if image.width > int(WIDTH*MAIN_GRAPH_WIDTH):
            image = image.resize((int(WIDTH*MAIN_GRAPH_WIDTH), image.height))
        if image.height > int(HEIGHT*MAIN_GRAPH_HEIGHT*0.9):
            image = image.resize((image.width, int(HEIGHT*MAIN_GRAPH_HEIGHT*0.9)))
        return image