import json

with open("data/production.json") as json_file:
    data = json.load(json_file)
    print(data)
