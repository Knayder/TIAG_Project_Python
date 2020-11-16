from utility.production_parser import *
from utility.production import *
from os.path import dirname, join

class ProductionsManager:
    def __init__(self, file_names):
        self.production = []
        script_dir = dirname(__file__)
        for file_name in file_names:
            parsed_productions = parse_json_production(join(script_dir, file_name))
            for parsed_production in parsed_productions:
                self.production.append(Production(parsed_production))
    
    def get_production(self, index):
        return self.production[index]