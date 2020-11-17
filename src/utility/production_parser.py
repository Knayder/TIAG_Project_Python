import json
import pydot
from os.path import dirname, join as path_join

class ParsedProduction:
    def __init__(self, name, left, right, transformation):
        self.name = name
        self.left = left
        self.right = right
        self.transformation = transformation
    def __str__(self):
        return \
            '{\n\tName:\n' + self.name + \
            '\n\n\tLeft:\n' + self.left + \
            '\n\n\tRight:\n' + self.right.__str__() + \
            '\n\tTransformation:\n' + self.transformation.__str__() + \
            '\n}'


def parse_json_production(file_path):
    with open(file_path) as json_file:
        try:
            data = json.load(json_file)
        except json.decoder.JSONDecodeError:
            raise TypeError(file_path + 'is not a json file')

        file_dir = dirname(file_path)
        parsed_productions = []

        for key in data:
            production = data[key]

            parsed_productions.append(ParsedProduction(
                name=key, #string of production name
                left=production['left'], #single vertex
                right=pydot.graph_from_dot_file(path_join(file_dir, production['right']))[0], #pydot.Graph of right side of production
                transformation=production['transformation'] #dictionary of transformations
            )) 
        return parsed_productions


