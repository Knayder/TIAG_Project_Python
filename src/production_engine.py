from productions_manager import *


class ProductionEngine:
    def __init__(self):
        self.productions_manager = ProductionsManager(['data/production.json'])

    def run(self):
        print('Hello World')