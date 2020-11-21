from production_engine import *

production_engine = ProductionEngine(['data/transformation_p.json'], 'data/start_graph.dot')

print(production_engine.next())
print(production_engine.next())
print(production_engine.next())
print(production_engine.next())