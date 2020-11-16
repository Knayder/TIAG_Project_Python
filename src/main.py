from production_engine import *
from os.path import dirname, join as path_join
script_dir = dirname(__file__)
abs_path_file = path_join(script_dir, 'data/production.json')
production_engine = ProductionEngine([abs_path_file])

production_engine.run()