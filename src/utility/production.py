from .production_parser import * 


class Production:
    def __init__(self, parsed_production: ParsedProduction):
        self.parsed_production = parsed_production

    def get_name(self):
        return self.parsed_production.name

    def get_transformation(self):
        return self.parsed_production.transformation
    
    def get_left(self):
        return self.parsed_production.left
    
    def get_right(self):
        return self.parsed_production.right
        
    def __str__(self):
        return self.parsed_production.__str__()
    

        