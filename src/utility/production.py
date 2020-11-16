from .production_parser import * 


class Production:
    def __init__(self, parsed_production: ParsedProduction):
        self.parsed_production = parsed_production

        
    def __str__(self):
        return self.parsed_production.__str__()
        