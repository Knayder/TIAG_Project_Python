from production_engine import *

production_engine = ProductionEngine(['data/transformation_p.json'], 'data/start_graph.dot')

for i in range(200):
    print("----")
    print(production_engine.next())