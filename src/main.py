from production_engine import *
import os.path
script_dir = os.path.dirname(__file__)
script_dir = script_dir[:len(script_dir) - 4]
abs_path_file = os.path.join(script_dir, "data_lab1/transformation_p.json")
production_engine = ProductionEngine([ abs_path_file ])

production_engine.run()
