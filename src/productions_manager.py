from utility.production_parser import *
from utility.production import *

class ProductionsManager:
    def __init__(self, file_names):
        self.production = []
        for file_name in file_names:
            parsed_productions = parse_json_production(file_name)
            for parsed_production in parsed_productions:
                self.production.append(Production(parsed_production))