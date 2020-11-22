from src.utility.production_parser import *
from src.utility.production import *
import random
class ProductionsManager:
    def __init__(self, file_names):
        self.production = []
        for file_name in file_names:
            parsed_productions = parse_json_production(file_name)
            for parsed_production in parsed_productions:
                self.production.append(Production(parsed_production))
    
    def get_production(self, index):
        return self.production[index]
        
    def size(self):
        return len(self.production)

    def get_random_production(self):
        return self.production[random.randrange(len(self.production))]
