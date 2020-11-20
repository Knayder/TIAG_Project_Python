from utility.gui import *
from production_engine import *

production_engine = ProductionEngine()

root = tk.Tk()
gui = Gui(root, production_engine)
root.mainloop()