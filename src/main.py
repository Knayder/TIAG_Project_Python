from gui.gui import *
from production_engine import *

production_engine = ProductionEngine(['data/transformation_p.json'], 'data/start_graph.dot')

root = tk.Tk()
gui = Gui(root, production_engine)
root.mainloop()