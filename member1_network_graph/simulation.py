import matplotlib.pyplot as plt
import config
from shortest_path import dijkstra
from graph_model import EDGE

# Strategy 1: Latency Priority
config.alpha = 0.8
config.beta = 0.1
config.gamma = 0.1

latency_priority = dijkstra(EDGE)

# Strategy 2: Energy Priority
config.alpha = 0.1
config.beta = 0.1
config.gamma = 0.8

energy_priority = dijkstra(EDGE)

# Strategy 3: Balanced
config.alpha = 0.5
config.beta = 0.3
config.gamma = 0.2

balanced = dijkstra(EDGE)

nodes = list(latency_priority.keys())

plt.figure()
plt.plot(nodes, [latency_priority[n] for n in nodes], marker='o')
plt.plot(nodes, [energy_priority[n] for n in nodes], marker='o')
plt.plot(nodes, [balanced[n] for n in nodes], marker='o')

plt.legend(["Latency Priority", "Energy Priority", "Balanced"])
plt.title("Shortest Path Cost Comparison")
plt.ylabel("Total Weighted Cost")
plt.xticks(rotation=45)
plt.show()